from be.model import store


class DBConn:
    def __init__(self):
        self.conn = store.get_db_conn()
        self.users_col = self.conn['user']
        self.store_col = self.conn['store']
        self.user_store_col = self.conn['user_store']

    def user_id_exist(self, user_id):
        result = self.users_col.find({'user_id':user_id})

        if result is None:
            return False
        else:
            return True

    def book_id_exist(self, store_id, book_id):
        result = self.store_col.find({'store_id':store_id},{'book_id':book_id})

        if result is None:
            return False
        else:
            return True

    def store_id_exist(self, store_id):
        result = self.user_store_col.find({'store_id':store_id})

        if result is None:
            return False
        else:
            return True
