from config.dbconfig import pg_config
import psycopg2
class RequestsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%d" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            pg_config['host'],
                                                            pg_config['port'])
        self.conn = psycopg2._connect(connection_url)

    # 4
    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from orders,order_requests_resource where orders.ord_id = order_requests_resource.ord_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # 6
    def getPurchasesByID(self, userID):
        cursor = self.conn.cursor()
        query = "select users.firstname, users.lastname, resource.rid,resource.rname, buy.price, orders.ord_id, orders.quantity, orders.date, orders.uid " \
                "FROM orders, users, resource, order_buys_resource as buy " \
                "WHERE orders.uid = %s and users.uid=orders.uid and orders.ord_id = buy.ord_id and buy.rid = resource.rid;"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # 6
    def getRequestsByID(self, userID):
        cursor = self.conn.cursor()
        query = "select users.firstname, users.lastname, resource.rid, resource.rname, orders.ord_id, orders.quantity, orders.date, orders.uid " \
                "from orders, users, resource, order_requests_resource as req " \
                "where orders.uid = %s and users.uid = orders.uid and orders.ord_id = req.ord_id and req.rid = resource.rid;"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #6
    def getReservesByID(self, userID):
        cursor = self.conn.cursor()
        query = "select users.firstname, users.lastname, resource.rid, resource.rname, orders.ord_id, orders.quantity, orders.date, orders.uid " \
                "from orders, users, resource, order_reserves_resource as res " \
                "where orders.uid = %s and users.uid = orders.uid and orders.ord_id = res.ord_id and res.rid = resource.rid;"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result
