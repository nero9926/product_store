import os
import sys

import email_service
import pika
from dotenv import load_dotenv

# import email_service
load_dotenv()


def main():
    # rabbitmq connection
    credentials = pika.PlainCredentials(
        os.environ.get("RABBITMQ_USER"), os.environ.get("RABBITMQ_PASSWORD"))

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=os.environ.get("RABBITMQ_HOST"), port=os.environ.get("RABBITMQ_PORT"),
        credentials=credentials))

    channel = connection.channel()

    def callback(ch, method, properties, body):
        try:
            err = email_service.notification(body)
            if err:
                ch.basic_nack(delivery_tag=method.delivery_tag)
            else:
                ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"Error processing message: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue="orders_queue", on_message_callback=callback
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
