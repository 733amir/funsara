import pymysql as db


class Database:
    def __init__(self):
        """Variables used to connect to correct database with correct username and password."""
        self.DB_SERVER = self.DB_NAME = self.DB_USER = self.DB_PASS = self.connection = None
        self.config()

        # Queries for creating tables of database
        self.create_queries = (
        'CREATE DATABASE {}'.format(self.DB_NAME),
       'USE {}'.format(self.DB_NAME),
        '''CREATE TABLE videos (
        id INT AUTO_INCREMENT,
        img_url VARCHAR(255) NOT NULL,
        blurred_img_url VARCHAR(255) NOT NULL,
        title VARCHAR(255) NOT NULL,
        short_description TEXT NOT NULL,
        full_description LONGTEXT NOT NULL,
        time INT NOT NULL,
        video_url VARCHAR(255) NOT NULL,
        PRIMARY KEY (id),
        CHECK (time>0)
        )''',
            '''CREATE TABLE batches (
        id INT AUTO_INCREMENT,
        number INT NOT NULL,
        video_id INT NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (video_id) REFERENCES videos(id)
        )'''
        )

        # Queries for deleting tables and database
        self.delete_queries = (
        'DROP DATABASE {}'.format(self.DB_NAME),
        )

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
        cursor = self.connection.cursor()  # Getting a cursor object to execute the queries.
        # Execute each query with order that saved in `queries`.
        for query in queries:
            cursor.execute(query)
            res.append(cursor.fetchall())
        cursor.close()
        # todo map query to its result
        return res

    def created(self):
        """Check existence of the database in MySQL."""
        try:
            db.connect(self.DB_SERVER, self.DB_USER, self.DB_PASS, self.DB_NAME).close()  # Just try to connect to the database.
        except db.InternalError:  # This exception means the database doesn't exist.
            return False
        except db.OperationalError:  # This exception means the username or password or both was wrong.
            return None
        # todo Consider checking tables and columns of database.
        else:  # This means everything is okay. Database exist, username and password was correct.
            print('created')
            return True

    def create(self):
        self.run(self.create_queries)
        # todo check exceptions

    def delete(self):
        self.run(self.delete_queries)
        # todo check exceptions

    def execute(self):
        pass


if __name__ == '__main__':
    database = Database()
    print(database.run(['select @@version']))  # return mysql version
