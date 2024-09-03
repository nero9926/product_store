from datetime import datetime

from sqlalchemy import (CheckConstraint, Column, DateTime, ForeignKey, Integer,
                        MetaData, Numeric, String, Table, create_engine, func,
                        insert, select, update)

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


metadata = MetaData()


customers = Table('customers', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('first_name', String(100), nullable=False),
                  Column('last_name', String(100), nullable=False),
                  Column('username', String(50), nullable=False),
                  Column('email', String(200), nullable=False),
                  Column('address', String(200), nullable=False),
                  Column('town', String(50), nullable=False),
                  Column('created_on', DateTime(), default=datetime.now),
                  Column('updated_on', DateTime(),
                         default=datetime.now, onupdate=datetime.now)
                  )


items = Table('items', metadata,
              Column('id', Integer(), primary_key=True),
              Column('name', String(200), nullable=False),
              Column('cost_price', Numeric(10, 2), nullable=False),
              Column('selling_price', Numeric(10, 2),  nullable=False),
              Column('quantity', Integer(), nullable=False),
              CheckConstraint('quantity > 0', name='quantity_check')
              )


orders = Table('orders', metadata,
               Column('id', Integer(), primary_key=True),
               Column('customer_id', ForeignKey('customers.id')),
               Column('date_placed', DateTime(), default=datetime.now),
               Column('date_shipped', DateTime())
               )


order_lines = Table('order_lines', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('order_id', ForeignKey('orders.id')),
                    Column('item_id', ForeignKey('items.id')),
                    Column('quantity', Integer())
                    )


metadata.drop_all(engine)
# metadata.create_all(engine)

# ins = insert(customers).values(
#     first_name='Dmitriy',
#     last_name='Yatsenko',
#     username='Moseend',
#     email='moseend@mail.com',
#     address='Shemilovskiy 2-Y Per., bld. 8/10, appt. 23',
#     town=' Vladivostok'
# )
# compiled = ins.compile()
# conn = engine.connect()

# with engine.connect() as conn:
#     result = conn.execute(ins, [
#         {
#             "first_name": "Vladimir",
#             "last_name": "Belousov",
#             "username": "Andescols",
#             "email": "andescols@mail.com",
#             "address": "Ul. Usmanova, bld. 70, appt. 223",
#             "town": " Naberezhnye Chelny"
#         },
#         {
#             "first_name": "Tatyana",
#             "last_name": "Khakimova",
#             "username": "Caltin1962",
#             "email": "caltin1962@mail.com",
#             "address": "Rossiyskaya, bld. 153, appt. 509",
#             "town": "Ufa"
#         },
#         {
#             "first_name": "Pavel",
#             "last_name": "Arnautov",
#             "username": "Lablen",
#             "email": "lablen@mail.com",
#             "address": "Krasnoyarskaya Ul., bld. 35, appt. 57",
#             "town": "Irkutsk"
#         },
#     ])
#     items_list = [
#         {
#             "name": "Chair",
#             "cost_price": 9.21,
#             "selling_price": 10.81,
#             "quantity": 6
#         },
#         {
#             "name": "Pen",
#             "cost_price": 3.45,
#             "selling_price": 4.51,
#             "quantity": 3
#         },
#         {
#             "name": "Headphone",
#             "cost_price": 15.52,
#             "selling_price": 16.81,
#             "quantity": 50
#         },
#         {
#             "name": "Travel Bag",
#             "cost_price": 20.1,
#             "selling_price": 24.21,
#             "quantity": 50
#         },
#         {
#             "name": "Keyboard",
#             "cost_price": 20.12,
#             "selling_price": 22.11,
#             "quantity": 50
#         },
#         {
#             "name": "Monitor",
#             "cost_price": 200.14,
#             "selling_price": 212.89,
#             "quantity": 50
#         },
#         {
#             "name": "Watch",
#             "cost_price": 100.58,
#             "selling_price": 104.41,
#             "quantity": 50
#         },
#         {
#             "name": "Water Bottle",
#             "cost_price": 20.89,
#             "selling_price": 25.00,
#             "quantity": 50
#         },
#     ]

#     order_list = [
#         {
#             "customer_id": 1
#         },
#         {
#             "customer_id": 1
#         }
#     ]

#     order_line_list = [
#         {
#             "order_id": 1,
#             "item_id": 1,
#             "quantity": 5
#         },
#         {
#             "order_id": 1,
#             "item_id": 2,
#             "quantity": 2
#         },
#         {
#             "order_id": 1,
#             "item_id": 3,
#             "quantity": 1
#         },
#         {
#             "order_id": 2,
#             "item_id": 1,
#             "quantity": 5
#         },
#         {
#             "order_id": 2,
#             "item_id": 2,
#             "quantity": 5
#         },
#     ]

#     r = conn.execute(insert(items), items_list)
#     print(r.rowcount)
#     r = conn.execute(insert(orders), order_list)
#     print(r.rowcount)
#     r = conn.execute(insert(order_lines), order_line_list)
#     print(r.rowcount)
#     conn.commit()
#     # dispatch_order(1)
#     # dispatch_order(2)
#     # s = select(customers.c.town).where(customers.c.id < 3)
#     # print(s)
#     rs = conn.execute(select(func.count("*")).where(orders.c.id == 2))
#     print(rs.fetchall())
