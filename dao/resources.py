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


    #4
    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from orders where orders.ord_id = order_requests_resource.ord_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
            print(row)
            print("\n")
        return result

    #6
    def getPurchasesByID(self, userID):
        cursor = self.conn.cursor()
        query = "select * from orders, firstname, lastname from users, rid, rname from resource, price from order_buys_resource as buy" \
                "where orders.uid = %d and users.uid = %d and orders.ord_id = buy.ord_id and buy.rid = resource.rid;"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
            print(row)
            print("\n")
        return result

    def getReservesByID(self, userID):
        cursor = self.conn.cursor()
        query = "select * from orders, firstname, lastname from users, rid, rname from resource" \
            "where orders.uid = %d and users.uid = %d and orders.ord_id = order_reserves_resource.ord_id and order_reserves_resource.rid = resource.rid;"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
            print(row)
            print("\n")
        return result

    #6
    def getRequestsByID(self, userID):
        cursor = self.conn.cursor()
        query = "select * from orders, firstname, lastname from users, rid, rname from resource" \
            "where orders.uid = %d and users.uid = %d and orders.ord_id = order_requests_resource.ord_id and order_requests_resource.rid = resource.rid;"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
            print(row)
            print("\n")
        return result

    #7
    def getResourceRequestedByRequestID(self, resourceID, orderID):
        cursor = self.conn.cursor()
        query = "select * from resource where resource.rid = %d AND order_requests_resource.ord_id = %d;"
        cursor.execute(query, (resourceID,), (orderID,))
        result = cursor.fetchone()
        return result

    #5,8
    def getAllResourcesAvailable(self):
        cursor = self.conn.cursor()
        query = "select * from resource where resource.quantity > 0 ;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
            print(row)
            print("\n")
        return result

    #9
    def getResourceByID(self, resourceID):
        cursor = self.conn.cursor()
        query = "select * from resource where resource.rid = %d;"
        cursor.execute(query, (resourceID,))
        result = cursor.fetchone()
        return result

    #10
    def getResourceRequestedByName(self, resourceName):
        cursor = self.conn.cursor()
        query = "select * from resource, order_requests_resource as req where resource.rid = req.rid and resource.name like %s and req.needed=1 order by resource.name ASC;"
        cursor.execute(query, (resourceName,))
        result = []
        for row in cursor:
            result.append(row)
            print(row)
            print("\n")
        return result

    #11
    def getResourceAvailableByName(self, resourceName):
        cursor = self.conn.cursor()
        query = "select * from resource where resource.quantity > 0  and resource.name like %s order by resource.name ASC;"
        cursor.execute(query, (resourceName,))
        result = []
        for row in cursor:
            result.append(row)
            print(row)
            print("\n")
        return result
