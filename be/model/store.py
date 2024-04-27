import logging
import os
import sqlite3 as sqlite
import threading
import pymongo
import pymongo.errors

class Store:
    database: str

    def __init__(self):
        #self.database = os.path.join(db_path, "be.db")
        self.init_tables()

    def init_tables(self):
        '''
        try:
            conn = self.get_db_conn()
            conn.execute(
                "CREATE TABLE IF NOT EXISTS user ("
                "user_id TEXT PRIMARY KEY, password TEXT NOT NULL, "
                "balance INTEGER NOT NULL, token TEXT, terminal TEXT);"
            )

            conn.execute(
                "CREATE TABLE IF NOT EXISTS user_store("
                "user_id TEXT, store_id, PRIMARY KEY(user_id, store_id));"
            )

            conn.execute(
                "CREATE TABLE IF NOT EXISTS store( "
                "store_id TEXT, book_id TEXT, book_info TEXT, stock_level INTEGER,"
                " PRIMARY KEY(store_id, book_id))"
            )

            conn.execute(
                "CREATE TABLE IF NOT EXISTS new_order( "
                "order_id TEXT PRIMARY KEY, user_id TEXT, store_id TEXT)"
            )

            conn.execute(
                "CREATE TABLE IF NOT EXISTS new_order_detail( "
                "order_id TEXT, book_id TEXT, count INTEGER, price INTEGER,  "
                "PRIMARY KEY(order_id, book_id))"
            )

            conn.commit()(variable) db: Unbound
        except sqlite.Error as e:
            logging.error(e)
            conn.rollback()
        '''
        try:
            db = self.get_db_conn()

            collection = db['user']
            collection.create_index('user_id', unique=True)
            collection = db['user_store']
            collection.create_index('user_id')
            collection = db['store']
            collection = db['new_order']
            collection = db['new_order_detail']
        except pymongo.errors.PyMongoError as e:
            logging.error(e)


    def get_db_conn(self) -> pymongo.MongoClient:
        #return sqlite.connect(self.database)
        client = pymongo.MongoClient('mongodb://localhost:27017')
        return client['bookstore_be']


database_instance: Store = None
# global variable for database sync
init_completed_event = threading.Event()


def init_database():
    global database_instance
    database_instance = Store()


def get_db_conn():
    global database_instance
    return database_instance.get_db_conn()