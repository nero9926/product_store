import json
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
        self.notifications_queue = "notifications_queue"
        self.orders_queue = "orders_queue"

        self.channel.exchange_declare(
            exchange=self.exchange, exchange_type="fanout")

        self.channel.queue_declare(queue=self.notifications_queue)
        self.channel.queue_declare(queue=self.orders_queue)

        self.channel.queue_bind(
            exchange=self.exchange,
            queue=self.notifications_queue,
            routing_key="notification"
        )
        self.channel.queue_bind(
            exchange=self.exchange,
            queue=self.orders_queue,
            routing_key="order"
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

    def send_notification(self, message: dict):
        try:
            self.channel.basic_publish(
                exchange=self.exchange,
                routing_key="notification",
                body=json.dumps(message, indent=4, sort_keys=True,
                                default=str, cls=UUIDEncoder),
            )
            return True
        except pika.exceptions.StreamLostError:
            self.connect()

    def send_order(self, message: dict):
        try:
            self.channel.basic_publish(
                exchange=self.exchange,
                routing_key="order",
                body=json.dumps(message, indent=4, sort_keys=True,
                                default=str, cls=UUIDEncoder),
            )
            return True
        except pika.exceptions.StreamLostError:
            self.connect()


mq = MessageQueue()
