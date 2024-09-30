import json
import os
import sys
import uuid as uuid_pkg
from datetime import date, datetime, timedelta
from typing import Any, Dict

import pika
from dotenv import load_dotenv
from sqlalchemy import (UUID, Column, Date, DateTime, Double, ForeignKey,
                        MetaData, String, create_engine)
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Session, relationship

postgres_metadata = MetaData()


@as_declarative(metadata=postgres_metadata)
class Base:
    id: Any

    def __init__(self, **kwargs: Dict) -> None:
        pass


# import app.services.order as service
# from ..api.deps import get_db_pg
# from ..services.order import patch_order

load_dotenv()


class Order(Base):
    __tablename__ = "order"

    id = Column(UUID, default=uuid_pkg.uuid4, primary_key=True)
    customer_id = Column(UUID, ForeignKey('user.id'))
    total = Column(Double, nullable=False)
    date_placed = Column(DateTime(), default=datetime.now)
    deliver_date = Column(Date(), default=date.today() +
                          timedelta(days=7), nullable=False)
    status = Column(String(30), default='created')
    products = relationship("Order_Product", backref="order")
    payment_details_id = relationship(
        "PaymentDetails", backref="order", uselist=False)


def main():
    POSTGRES_USER = os.environ.get("POSTGRES_USER")[0],
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")[0],
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST")[0],
    POSTGRES_PORT = int(os.environ["POSTGRES_PORT"]),
    POSTGRES_DB = os.environ.get("POSTGRES_DB")[0],

    print(POSTGRES_PORT[0])
    POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"  # noqa

    engine = create_engine(POSTGRES_URL)
    session = Session(bind=engine)

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
