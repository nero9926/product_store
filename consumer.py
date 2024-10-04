import json
import os
import sys

import pika
from dotenv import load_dotenv

from app.db.session import SessionLocalPG
from app.main import app
from app.models.order import Order

load_dotenv()


def main():
    session = SessionLocalPG()

    # rabbitmq connection
    credentials = pika.PlainCredentials(
        os.environ.get("RABBITMQ_USER"), os.environ.get("RABBITMQ_PASSWORD"))

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=os.environ.get("RABBITMQ_HOST"), port=os.environ.get("RABBITMQ_PORT"),  # noqa
        credentials=credentials))

    channel = connection.channel()

    def check_order_status(ch, method, properties, body):
        try:
            order = json.loads(body)
            print(f"Received order: {order['order_uuid']}")
            db_instance = session.query(Order).get(order['order_uuid'])
            db_instance.status = 'in_work'
            session.add(db_instance)
            session.commit()
            print(f'order {order["order_uuid"]} in work!')
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"Error processing message: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue="orders_queue", on_message_callback=check_order_status
    )

    print("Waiting for messages. To exit press CTRL+C")

    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
