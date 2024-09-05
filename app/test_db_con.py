from datetime import datetime

from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        SmallInteger, String, create_engine)
from sqlalchemy.orm import declarative_base, relationship

# from sqlalchemy.exc import IntegrityError
# from sqlalchemy.sql import func

# def dispatch_order(order_id):
#     #  проверка того, правильно ли указан order_id
#     r = conn.execute(select(func.count("*")).where(orders.c.id == order_id))
#     if not r.scalar():
#         raise ValueError("Недействительный order_id: {}".format(order_id))

#     # брать товары в порядке очереди
#     s = select(order_lines.c.item_id, order_lines.c.quantity).where(
#         order_lines.c.order_id == order_id
#     )

#     rs = conn.execute(s)
#     ordered_items_list = rs.fetchall()
#     conn.commit()
#     # начало транзакции
#     t = conn.begin()

#     try:
#         for i in ordered_items_list:
#             u = update(items).where(
#                 items.c.id == i.item_id
#             ).values(quantity=items.c.quantity - i.quantity)

#             rs = conn.execute(u)

#         u = update(orders).where(orders.c.id == order_id).values(
#             date_shipped=datetime.now())
#         rs = conn.execute(u)
#         t.commit()
#         print("Транзакция завершена.")

#     except IntegrityError as e:
#         print(e)
#         t.rollback()
#         print("Транзакция не удалась.")


engine = create_engine(
    url="postgresql://postgres:admin@localhost:5433/sqlalchemy_tuts")


Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
    orders = relationship("Order", backref='customer')


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2),  nullable=False)
    quantity = Column(Integer())


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    line_items = relationship("OrderLine", backref='order')


class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    item = relationship("Item")


Base.metadata.create_all(engine)
