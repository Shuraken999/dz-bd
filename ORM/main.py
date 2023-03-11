import sqlalchemy
import json
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Sale, Stock
from settings import DSN

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open("bd.json") as f:
    json_data = json.load(f)
for model in json_data:
    if model["model"] == 'publisher':
        pb = Publisher(name=model["fields"]["name"])
        session.add(pb)
    elif model["model"] == 'book':
        bk = Book(title=model["fields"]["title"], id_publisher=model["fields"]["id_publisher"])
        session.add(bk)
    elif model["model"] == 'shop':
        sp = Shop(name=model["fields"]["name"])
        session.add(sp)
    elif model["model"] == 'stock':
        sk = Stock(id_shop=model["fields"]["id_shop"], id_book=model["fields"]["id_book"],
                   count=model["fields"]["count"])
        session.add(sk)
    elif model["model"] == 'sale':
        sl = Sale(price=float(model["fields"]["price"]), date_sale=model["fields"]["date_sale"],
                  count=model["fields"]["count"], id_stock=model["fields"]["id_stock"])
        session.add(sl)
publisher = input('Введите идентификатор издателя: ')
for name_book in session.query(Book).join(Book.publisher).filter(Publisher.id == publisher).all():
    title_book = session.query(Book.id).join(Book.publisher).filter(Publisher.id == publisher).subquery()
    stock_id = session.query(Stock.id).join(title_book, Stock.id_book == title_book.c.id).subquery()
    shop_id = session.query(Stock.id_shop).join(title_book, Stock.id_book == title_book.c.id).subquery()
    for name_shop in session.query(Shop).join(shop_id, Shop.id == shop_id.c.id_shop).all():
        for sale_info in session.query(Sale).join(stock_id, Sale.id_stock == stock_id.c.id).all():
            print(f' {name_book} | {name_shop} | {sale_info}')
session.commit()

session.close()
