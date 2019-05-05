import sqlite3 as sqlite

class ConnectionClass():

    def __init__(self):
        self.database = "dbChallenge.db"
        self.conn = None
        self.cur = None
        self.connected = False

    def connect(self):
        self.conn = sqlite.connect(self.database)
        self.cur = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        self.conn.close()
        self.connected = False

    def persist(self):
        if self.connected:
            self.conn.commit()
            return True
        else:
            return False

    def execute(self, sql, parms=None):
        if self.connected:
            if parms == None:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, parms)
            return self.persist()
        else:
            return False

    def execute_select(self,sql):
        if self.connected:
            self.cur.execute(sql)
            return self.cur.fetchall()
        else:
            return False


