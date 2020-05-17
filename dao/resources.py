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


    def insertIce(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, weight):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, date, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into ice(weight,rid) values (%s, %s)"
        cursor.execute(query,(weight, rid,))
        self.conn.commit()
        return rid

    def insertMedicalDevices(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, type):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, date, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into medicaldevices(type,rid) values (%s, %s)"
        cursor.execute(query,(type, rid,))
        self.conn.commit()
        return rid

    def insertFuel(self,rname, description, brand, quantity, price, latitude, longitude, date, uid, initial_quantity, type,amount):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, date, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query = "insert into fuel(type,amount,rid) values (%s,%s, %s)"
        cursor.execute(query, (type,amount, rid,))
        self.conn.commit()
        return rid

    def buyResources(self,uid,rids,quantities,date_milliseconds,method):
        cursor = self.conn.cursor()
        quantityError=False
        for i in range(0,len(rids)):#FOR EACH RESOURCE THAT THE USER BUYS
            query= "select rid,quantity,cast(price as NUMERIC) from resource where rid=%s" #SELECT THE INFO OF THE RESOURCE
            cursor.execute(query, (rids[i],))
            rid,qty,price= cursor.fetchone()
            if(qty>=quantities[i]): #VALIDATION OF QUANTITY
                amount=price*quantities[i] #CALCULATE THE PAYMENT AMOUNT QUANTITY*PRICE
                queryPayment="insert into payment(method,amount,date,uid) values (%s,%s,%s,%s) returning pay_id;"
                cursor.execute(queryPayment,(method,amount,date_milliseconds,uid,))
                pay_id=cursor.fetchone()[0] #GET THE ID OF THE CREATED PAYMENT
                queryOrder="insert into orders(quantity, date, pay_id,uid) values (%s,%s,%s,%s) returning ord_id;"
                cursor.execute(queryOrder,(quantities[i],date_milliseconds,pay_id,uid))
                ord_id=cursor.fetchone()[0]#GET THE ID OF THE ORDER CREATED
                newResourceQty=qty-quantities[i]
                queryUpdateResource="update resource SET quantity=%s where rid=%s;"
                cursor.execute(queryUpdateResource,(newResourceQty,rids[i])) #UPDATE THE QUANTITY OF THE RESOURCE AFTER BUY
                if(price==0): #IF THE PRICE IS 0, CREATE IT IN THE TABLE OF RESERVES
                    queryBuy = "insert into order_reserves_resource(ord_id,rid) values (%s,%s);"
                    cursor.execute(queryBuy, (ord_id, rids[i]))  # CREATE THE ORDER_RESERVEA_RESOURCE
                else:
                    queryBuy="insert into order_buys_resource(ord_id,rid,price) values (%s,%s,%s);"
                    cursor.execute(queryBuy,(ord_id,rids[i],amount))#CREATE THE ORDER_BUY_RESOURCE
            else:
                quantityError=True
        if(not quantityError):
            self.conn.commit()
            return True
        else:
            return False

    def reserveResources(self,uid,rids,quantities,date_milliseconds):
        cursor = self.conn.cursor()
        quantityError=False
        for i in range(0,len(rids)):#FOR EACH RESOURCE THAT THE USER RESERVES
            query= "select rid,quantity,cast(price as NUMERIC) from resource where rid=%s" #SELECT THE INFO OF THE RESOURCE
            cursor.execute(query, (rids[i],))
            rid,qty,price= cursor.fetchone()
            if(price!=0):
                return 1
            if(qty>=quantities[i]): #VALIDATION OF QUANTITY
                queryOrder="insert into orders(quantity, date,uid) values (%s,%s,%s) returning ord_id;"
                cursor.execute(queryOrder,(quantities[i],date_milliseconds,uid))
                ord_id=cursor.fetchone()[0]#GET THE ID OF THE ORDER CREATED
                newResourceQty=qty-quantities[i]
                queryUpdateResource="update resource SET quantity=%s where rid=%s;"
                cursor.execute(queryUpdateResource,(newResourceQty,rids[i])) #UPDATE THE QUANTITY OF THE RESOURCE AFTER RESERVE
                queryBuy="insert into order_reserves_resource(ord_id,rid) values (%s,%s);"
                cursor.execute(queryBuy,(ord_id,rids[i]))#CREATE THE ORDER_RESERVEA_RESOURCE
            else:
                quantityError=True
        if(not quantityError):
            self.conn.commit()
            return 0
        else:
            return 2

    def requestResources(self,uid,rids,quantities,date_milliseconds):
        cursor = self.conn.cursor()
        quantityError=False
        for i in range(0,len(rids)):#FOR EACH RESOURCE THAT THE USER RESERVES
            query= "select rid,quantity from resource where rid=%s" #SELECT THE INFO OF THE RESOURCE
            cursor.execute(query, (rids[i],))
            rid,qty= cursor.fetchone()

            if(qty==0): #VALIDATION OF QUANTITY
                queryOrder="insert into orders(quantity, date,uid) values (%s,%s,%s) returning ord_id;"
                cursor.execute(queryOrder,(quantities[i],date_milliseconds,uid))
                ord_id=cursor.fetchone()[0]#GET THE ID OF THE ORDER CREATED
                queryBuy="insert into order_requests_resource(ord_id,rid,needed) values (%s,%s,%s);"
                cursor.execute(queryBuy,(ord_id,rids[i],1,))#CREATE THE ORDER_RESERVEA_RESOURCE
            else:
                quantityError=True
        if(not quantityError):
            self.conn.commit()
            return 0
        else:
            return 2