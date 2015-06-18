import sqlite3
import os

class DatabaseManager(object):
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def query(self, arg):
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def executescript(self, sql):
        self.cur.executescript(sql)
        self.conn.commit()
        return self.cur

    def execute_with_params(self, sql, values):
        self.cur.execute(sql,values)
        self.conn.commit()
        return self.cur

    def __del__(self):
        self.conn.close()


