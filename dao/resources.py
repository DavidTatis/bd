from config.dbconfig import pg_config
import psycopg2
class ResourcesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%d" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            pg_config['host'],
                                                            pg_config['port'])
        self.conn = psycopg2._connect(connection_url)


    def getResourceRequestedByResourceID(self, resourceID):
        cursor = self.conn.cursor()
        query = "select * from resource, order_requests_resource where resource.rid = %s AND order_requests_resource.rid=resource.rid AND order_requests_resource.needed = 1;"
        cursor.execute(query, (resourceID,))
        result = cursor.fetchone()
        return result


    #7
    def getResourceRequestedByRequestID(self, resourceID, orderID):
        cursor = self.conn.cursor()
        query = "select * from resource, order_requests_resource where resource.rid = %s AND order_requests_resource.rid=resource.rid AND order_requests_resource.ord_id=%s AND order_requests_resource.needed = 1;"
        cursor.execute(query, (resourceID,orderID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #5,8
    def getAllResourcesAvailable(self):
        cursor = self.conn.cursor()
        query = "select * from resource where resource.quantity > 0 ;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #9
    def getResourceByID(self, resourceID):
        cursor = self.conn.cursor()
        query = "select * from resource where resource.rid = %s;"
        cursor.execute(query, (resourceID,))
        result = cursor.fetchone()
        return result

    #10
    def getResourceRequestedByName(self, resourceName):
        resourceName="%"+resourceName+"%"
        cursor = self.conn.cursor()
        query = "select * from resource, order_requests_resource as req where resource.rid = req.rid and resource.rname like %s  and req.needed=1 order by resource.rname ASC;"
        cursor.execute(query, (resourceName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #11
    def getResourceAvailableByName(self, resourceName):
        resourceName = "%" + resourceName + "%"
        cursor = self.conn.cursor()
        query = "select * from resource where resource.quantity > 0  and resource.rname like %s order by resource.rname ASC;"
        cursor.execute(query, (resourceName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertWater(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, calories, speciality, ounces):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, date, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into water(calories, speciality, ounces, rid) values (%s, %s, %s, %s)"
        cursor.execute(query,(calories, speciality, ounces, rid,))
        self.conn.commit()
        return rid

    def insertCannedFood(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, calories, nutritionfacts, size, foodtype):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, date, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into cannedfood(calories, nutritionfacts, size, foodtype, rid) values " \
              "(%s, %s, %s, %s, %s)"

        cursor.execute(query,(calories, nutritionfacts, size,foodtype, rid,))
        self.conn.commit()
        return rid

    def insertDryFood(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, calories, nutritionfacts, size, foodtype):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, date, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into dryfood(calories, nutritionfacts, size, foodtype, rid) values " \
              "(%s, %s, %s, %s, %s)"

        cursor.execute(query,(calories, nutritionfacts, size,foodtype, rid,))
        self.conn.commit()
        return rid

    def insertBabyFood(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, calories, nutritionfacts, size, foodtype):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, date, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into babyfood(calories, nutritionfacts, size, foodtype, rid) values " \
              "(%s, %s, %s, %s, %s)"

        cursor.execute(query,(calories, nutritionfacts, size,foodtype, rid,))
        self.conn.commit()
        return rid

    def insertMedication(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, type, servingspercontainer):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, date, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into medications(type, servingspercontainer, rid) values " \
              "(%s, %s, %s)"

        cursor.execute(query,(type, servingspercontainer, rid,))
        self.conn.commit()
        return rid
