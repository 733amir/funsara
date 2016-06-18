import pymysql as db


class Database:
    def __init__(self):
        """Variables used to connect to correct database with correct username and password."""
        self.DB_SERVER = self.DB_NAME = self.DB_USER = self.DB_PASS = self.connection = None
        self.config()
        self.connect()

    def config(self, server='localhost', name='funsara', username='funsara', password='funsara'):
        """config the server and name and username and password from input or set default"""
        self.DB_SERVER = server
        self.DB_NAME = name
        self.DB_USER = username
        self.DB_PASS = password

    def connect(self):
        """create a connection to mysql"""
        self.connection = db.connect(self.DB_SERVER, self.DB_USER, self.DB_PASS)
        # todo check the connection

    def disconnect(self):
        """close connection from mysql"""
        self.connection.close()

    def run(self, queries):
        """run queries and return result"""
        res = []
        cursor = self.connection.cursor()
        for query in queries:
            cursor.execute(query)
            res.append(cursor.fetchall())
        cursor.close()
        # todo map query to its result
        return res

if __name__ == '__main__':
    database = Database()
    print(database.run(['select @@version']))  # return mysql version