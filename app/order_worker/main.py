import json
import os
import sys

import pika
from dotenv import load_dotenv

# import app.services.order as service
# from ..api.deps import get_db_pg
# from ..services.order import patch_order

load_dotenv()


def main():
    # rabbitmq connection
    credentials = pika.PlainCredentials(
        os.environ.get("RABBITMQ_USER"), os.environ.get("RABBITMQ_PASSWORD"))

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=os.environ.get("RABBITMQ_HOST"), port=os.environ.get("RABBITMQ_PORT"),
        credentials=credentials))

    channel = connection.channel()

    def check_order_status(ch, method, properties, body):
        try:
            order = json.loads(body)
            print(f"Received order: {order['order_uuid']}")
            # Проверка наличия
            # payload = {
            #     'status': 'in_work'
            # }
            print('cheking....')
            order['order_status'] = 'in_work'
            # changed_order = patch_order(order_uuid=order.order_uuid,
            #                             payload=payload, db=get_db_pg)
            print(order)
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
