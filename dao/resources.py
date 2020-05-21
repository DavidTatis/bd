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
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
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
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into canned_food(calories, nutrition_facts, cfsize, food_type, rid) values " \
              "(%s, %s, %s, %s, %s)"

        cursor.execute(query,(calories, nutritionfacts, size,foodtype, rid,))
        self.conn.commit()
        return rid

    def insertDryFood(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, calories, nutritionfacts, size, foodtype):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into dry_food(calories, nutrition_facts, dfsize, food_type, rid) values " \
              "(%s, %s, %s, %s, %s)"

        cursor.execute(query,(calories, nutritionfacts, size,foodtype, rid,))
        self.conn.commit()
        return rid

    def insertBabyFood(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, calories, nutritionfacts, size, foodtype):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into baby_food(calories, nutrition_facts, bfsize, food_type, rid) values " \
              "(%s, %s, %s, %s, %s)"

        cursor.execute(query,(calories, nutritionfacts, size,foodtype, rid,))
        self.conn.commit()
        return rid

    def insertMedication(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, type, servingspercontainer):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into medication(mtype, servings_per_container, rid) values " \
              "(%s, %s, %s)"

        cursor.execute(query,(type, servingspercontainer, rid,))
        self.conn.commit()
        return rid

    def insertIce(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, weight):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into ice(weight,rid) values (%s, %s)"
        cursor.execute(query,(weight, rid,))
        self.conn.commit()
        return rid

    def insertMedicalDevice(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, type):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into medical_device(mdtype,rid) values (%s, %s)"
        cursor.execute(query,(type, rid,))
        self.conn.commit()
        return rid

    def insertFuel(self,rname, description, brand, quantity, price, latitude, longitude, date, uid, initial_quantity, type,amount):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query = "insert into fuel(ftype,amount,rid) values (%s,%s, %s)"
        cursor.execute(query, (type,amount, rid,))
        self.conn.commit()
        return rid

    def insertHeavyEquipment(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, heavyEquipmentType):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query = "insert into heavy_equipment(hetype, rid) values (%s, %s)"
        cursor.execute(query, (heavyEquipmentType, rid,))
        self.conn.commit()
        return rid

    def insertBattery(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, disposability, householdType):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query="insert into battery(disposability, household_type, rid) values (%s, %s, %s)"
        cursor.execute(query, (disposability, householdType, rid,))
        self.conn.commit()
        return rid

    def insertPowerGenerator(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, gen_fuel_type, type, wattage, color):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query = "insert into power_generator(gen_fuel_type, pgtype, wattage, color, rid) values (%s, %s, %s, %s, %s)"
        cursor.execute(query, (gen_fuel_type, type, wattage, color, rid,))
        self.conn.commit()
        return rid

    def insertTool(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, material, field):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query = "insert into tool(material, field, rid) values (%s, %s, %s)"
        cursor.execute(query, (material, field, rid,))
        self.conn.commit()
        return rid

    def insertClothing(self, rname, description, brand, quantity, price, latitude, longitude, date,
                                  uid, initial_quantity, size, gender, color, material):
        cursor = self.conn.cursor()
        query = "insert into resource(rname, description, brand, quantity, price, latitude, longitude, rdate, " \
                "uid, initial_quantity) values (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s) returning rid;"
        cursor.execute(query, (rname, description, brand, quantity, price, latitude, longitude, date,
                               uid, initial_quantity,))
        rid = cursor.fetchone()[0]

        query = "insert into clothing(gender, color, material, rid, csize) values (%s, %s, %s, %s, %s)"
        cursor.execute(query, (gender, color, material, rid, size,))
        self.conn.commit()
        return rid

    def buyResources(self,uid,rids,quantities,date_milliseconds,method):
        cursor = self.conn.cursor()
        amount = 0
        for i in range(0,len(rids)):#FOR EACH RESOURCE THAT THE USER BUYS
            query= "select rid,quantity,cast(price as NUMERIC) from resource where rid=%s" #SELECT THE INFO OF THE RESOURCE
            cursor.execute(query, (rids[i],))
            rid,qty,price= cursor.fetchone()
            if(qty>=quantities[i]): #VALIDATION OF QUANTITY
                amount+=price*quantities[i] #CALCULATE THE PAYMENT AMOUNT QUANTITY*PRICE
        queryPayment = "insert into payment(method,amount,pdate,uid) values (%s,%s,%s,%s) returning pay_id;"
        cursor.execute(queryPayment, (method, amount, date_milliseconds, uid,))
        pay_id = cursor.fetchone()[0]  # GET THE ID OF THE CREATED PAYMENT

        for i in range(0,len(rids)):#FOR EACH RESOURCE THAT THE USER BUYS
            query= "select rid,quantity,cast(price as NUMERIC) from resource where rid=%s" #SELECT THE INFO OF THE RESOURCE
            cursor.execute(query, (rids[i],))
            rid,qty,price= cursor.fetchone()
            if(qty>=quantities[i]): #VALIDATION OF QUANTITY
                amount = price * quantities[i]  # CALCULATE THE PAYMENT AMOUNT QUANTITY*PRICE
                queryOrder="insert into orders(quantity, odate, pay_id,uid) values (%s,%s,%s,%s) returning ord_id;"
                cursor.execute(queryOrder,(quantities[i],date_milliseconds,pay_id,uid))
                ord_id=cursor.fetchone()[0]#GET THE ID OF THE ORDER CREATED
                newResourceQty=qty-quantities[i]
                queryUpdateResource="update resource SET quantity=%s where rid=%s;"
                cursor.execute(queryUpdateResource,(newResourceQty,rids[i])) #UPDATE THE QUANTITY OF THE RESOURCE AFTER BUY
                if(price==0): #IF THE PRICE IS 0, CREATE IT IN THE TABLE OF RESERVES
                    queryBuy = "insert into order_reserves_resource(ord_id,rid) values (%s,%s);"
                    cursor.execute(queryBuy, (ord_id, rids[i]))  # CREATE THE ORDER_RESERVES_RESOURCE
                else:
                    queryBuy="insert into order_buys_resource(ord_id,rid,price) values (%s,%s,%s);"
                    cursor.execute(queryBuy,(ord_id,rids[i],amount))#CREATE THE ORDER_BUY_RESOURCE
            else:
                return 2

        self.conn.commit()
        return 0

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
                queryOrder="insert into orders(quantity, odate,uid) values (%s,%s,%s) returning ord_id;"
                cursor.execute(queryOrder,(quantities[i],date_milliseconds,uid))
                ord_id=cursor.fetchone()[0]#GET THE ID OF THE ORDER CREATED
                newResourceQty=qty-quantities[i]
                queryUpdateResource="update resource SET quantity=%s where rid=%s;"
                cursor.execute(queryUpdateResource,(newResourceQty,rids[i])) #UPDATE THE QUANTITY OF THE RESOURCE AFTER RESERVE
                queryBuy="insert into order_reserves_resource(ord_id,rid) values (%s,%s);"
                cursor.execute(queryBuy,(ord_id,rids[i]))#CREATE THE ORDER_RESERVES RESOURCE
            else:
                return 2

        self.conn.commit()
        return 0


    def requestResources(self,uid,rids,quantities,date_milliseconds):
        cursor = self.conn.cursor()

        for i in range(0,len(rids)):#FOR EACH RESOURCE THAT THE USER RESERVES
            query= "select rid,quantity from resource where rid=%s" #SELECT THE INFO OF THE RESOURCE
            cursor.execute(query, (rids[i],))
            rid,qty= cursor.fetchone()

            if(qty==0): #VALIDATION OF QUANTITY
                queryOrder="insert into orders(quantity, odate,uid) values (%s,%s,%s) returning ord_id;"
                cursor.execute(queryOrder,(quantities[i],date_milliseconds,uid))
                ord_id=cursor.fetchone()[0]#GET THE ID OF THE ORDER CREATED
                queryBuy="insert into order_requests_resource(ord_id,rid,needed) values (%s,%s,%s);"
                cursor.execute(queryBuy,(ord_id,rids[i],1,))#CREATE THE ORDER_REQUESTS_RESOURCE
            else:
                return 2

        self.conn.commit()
        return 0


