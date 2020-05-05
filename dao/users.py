from config.dbconfig import pg_config
import psycopg2
class UsersDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%d" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            pg_config['host'],
                                                            pg_config['port'])
        self.conn = psycopg2._connect(connection_url)



    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAdminUsers(self):
        cursor = self.conn.cursor()
        query = "select * from admin"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllSupplierUsers(self):
        cursor = self.conn.cursor()
        query = "select * from supplier"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllConsumerUsers(self):
        cursor = self.conn.cursor()
        query = "select * from consumer"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result