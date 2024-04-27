from be.model import store


class DBConn:
    def __init__(self):
        self.db = store.get_db_conn()

    def user_id_exist(self, user_id):
        user_col = self.db['user']
        doc = user_col.find_one({'user_id': user_id})
        if doc is None:
            return False
        else:
            return True

    def book_id_exist(self, store_id, book_id):
        store_col = self.db['store']
        doc = store_col.find_one({'store_id': store_id, 'book_id': book_id})
        if doc is None:
            return False
        else:
            return True

    def store_id_exist(self, store_id):
        user_store_col = self.db['user_store']
        doc = user_store_col.find_one({'store_id': store_id})
        if doc is None:
            return False
        else:
            return True
