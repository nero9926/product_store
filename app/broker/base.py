import json
import os
import sys
import time

import pika
import pika.exceptions

# from asgiref.sync import async_to_sync
from app.core.config import settings
from app.helpers.encoders import UUIDEncoder


class MessageQueue:
    def __init__(self) -> None:
        self.credentials = pika.PlainCredentials(
            settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST, port=settings.RABBITMQ_PORT,
            credentials=self.credentials))

        self.channel = self.connection.channel()
        self.exchange = "orders"
        self.queue = "orders_queue"
        self.channel.exchange_declare(
            exchange=self.exchange, exchange_type="fanout")
        self.channel.queue_declare(queue=self.queue)
        self.channel.queue_bind(
            exchange=self.exchange, queue=self.queue, routing_key="order"
        )
        self.channel.basic_qos(prefetch_count=1)

    def connect_to_rabbitmq(self):
        # Connect to RabbitMQ
        while True:
            try:
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(
                        host=settings.RABBITMQ_HOST,
                        port=settings.RABBITMQ_PORT,
                        credentials=self.credentials
                    )
                )
            except pika.exceptions.AMQPConnectionError:
                print("Failed to connect to RabbitMQ. Retrying in 5 seconds...")
                time.sleep(5)

    # PUBLISHING MESSAGES TO THE QUEUE
    def publish_order(self, message: dict):
        try:
            # publishing to the queue
            self.channel.basic_publish(
                exchange=self.exchange,
                routing_key="order",
                body=json.dumps(message, indent=4, sort_keys=True,
                                default=str, cls=UUIDEncoder),
            )
            return True
        except pika.exceptions.StreamLostError:
            self.connect()

    # CONSUMER (BUT LARGELY INACTIVE)

    def consume_messages(self):
        try:
            print("messages are now consumed")

            def callback_func(ch, method, properties, body):
                print(f" [x] Recieved {body}")
                # parse the message from the queue
                # if self.wsok_manager.active_connections:
                #     message_status =
                # await self.wsok_manager.send_personal_message(
                #         json.loads(body)
                #     )
                #     if message_status:
                # ch.basic_ack(delivery_tag=method.delivery_tag)

                # else:
                #     ch.basic_nack(
                #         delivery_tag=method.delivery_tag, requeue=False)

                # async_tosyn

            self.channel.basic_consume(
                queue=self.queue,
                on_message_callback=callback_func,
                auto_ack=True,
            )
            self.channel.start_consuming()

        except KeyboardInterrupt:
            print("Consumer closed")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

    # FETCH ALL THE MESSAGES
    def fetch_all_messages(self):
        messages = []
        method_frame, header_frame, body = self.channel.basic_get(
            queue=self.queue)
        while method_frame:
            method_frame, header_frame, body = self.channel.basic_get(
                queue=self.queue)

            if body:
                messages.append((method_frame, json.loads(body)))

        return messages

    # USERS MESSAGE FILTER
    def get_user_messages(self, user_id: int):
        messages = self.fetch_all_messages()
        if messages:
            user_messages = [
                {"message": message, "delivery_tag": method_frame.delivery_tag}
                for method_frame, message in messages
                if message["user_id"] == user_id
            ]
            if user_messages:
                return user_messages
            else:
                return None
        return None

    # CLOSING CONNECTIONS

    # def __del__(self):
    #     # try catch exceptions
    #     self.connection.close()


mq = MessageQueue()
