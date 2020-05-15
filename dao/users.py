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

    def getAllUsersInneed(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM users, consumer, orders, order_requests_resource as req " \
                "WHERE orders.ord_id=req.rid AND req.needed=1 AND orders.uid=consumer.uid AND users.uid=orders.uid"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAllAdminUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users, admin WHERE users.uid=admin.uid" #TODO: check if its correct
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllSupplierUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users, supplier WHERE users.uid=supplier.uid" #TODO: check if its correct
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllConsumerUsers(self):
        cursor = self.conn.cursor()
        query = "select * from consumer, users WHERE users.uid=consumer.uid" #TODO: check if its correct
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertAdmin(self,firstname, lastname, username,password,email,phone,dateofbirth,address,zipcode,salary):
        cursor = self.conn.cursor()
        query = "insert into users(firstname, lastname, username,password,email,phone,dateofbirth,address,zipcode) values (%s, %s, %s, %s,%s, %s, %s,%s,%s) returning uid;" #TODO: glob variable
        cursor.execute(query, (firstname, lastname, username,password,email,phone,dateofbirth,address,zipcode,))
        uid = cursor.fetchone()[0]

        query="insert into admin(uid,salary) values (%s, %s)"
        cursor.execute(query,(uid,salary,))
        self.conn.commit()
        return uid

    def insertSupplier(self, firstname, lastname, username,password,email,phone,dateofbirth,address,zipcode,country,occupation,org_id):
        cursor = self.conn.cursor()
        query = "insert into users(firstname, lastname, username,password,email,phone,dateofbirth,address,zipcode) values (%s, %s, %s, %s,%s, %s, %s,%s,%s) returning uid;"
        cursor.execute(query, (firstname, lastname, username, password, email, phone, dateofbirth, address, zipcode,))
        uid = cursor.fetchone()[0]

        query = "insert into supplier(uid,country,occupation,org_id) values (%s,%s, %s,%s)"
        cursor.execute(query, (uid,country,occupation,org_id))
        self.conn.commit()
        return uid

    def insertConsumer(self, firstname, lastname, username,password,email,phone,dateofbirth,address,zipcode,priority):
        cursor = self.conn.cursor()
        query = "insert into users(firstname, lastname, username,password,email,phone,dateofbirth,address,zipcode) values (%s, %s, %s, %s,%s, %s, %s,%s,%s) returning uid;"
        cursor.execute(query, (firstname, lastname, username, password, email, phone, dateofbirth, address, zipcode,))
        uid = cursor.fetchone()[0]

        query = "insert into consumer(uid,priority) values (%s,%s)"
        cursor.execute(query, (uid,priority))
        self.conn.commit()
        return uid