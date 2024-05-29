import psycopg2
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

db_params = {
    'database': os.getenv('database'),
    'user': os.getenv('user'),
    'password': os.getenv('password'),
    'host': os.getenv('host'),
    'port':os.getenv('port'),
}
# conn = psycopg2.connect(**db_params)
# cur.conn.cursor()
# cur.execute("""select * from products;""")
# print(cur.fetchall())


class ConnectDB:
    def __init__(self, db_params: dict):
        self.db_params = db_params

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_params)
        self.cur = self.conn.cursor()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        if self.conn:
            self.cur.close()
            self.conn.close()

    def commit(self):
        self.conn.commit()


class product:
    def __init__(self, name,price):
        self.name = name
        self.price = price

    def save(self):
        with ConnectDB(db_params) as db:
            insert_into_product = """INSERT INTO product(name,price)
            values (%s,%s);
            """
            db.cur.execute(insert_into_product, (self.name,self.price))
            db.commit()
            print('Successfully saved')


car = product('samsung',600)
car.save()
