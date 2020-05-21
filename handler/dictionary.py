from flask import jsonify

class Dictionary:

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        result['username'] = row[3]
        result['password'] = row[4]
        result['email'] = row[5]
        result['phone'] = row[6]
        result['dateofbirth'] = row[7]
        result['address'] = row[8]
        result['zipcode'] = row[9]
        return result

    def build_admin_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        result['username'] = row[3]
        result['password'] = row[4]
        result['email'] = row[5]
        result['phone'] = row[6]
        result['dateofbirth'] = row[7]
        result['address'] = row[8]
        result['zipcode'] = row[9]
        result['salary'] = row[10]

        return result

    def build_consumer_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        result['username'] = row[3]
        result['password'] = row[4]
        result['email'] = row[5]
        result['phone'] = row[6]
        result['dateofbirth'] = row[7]
        result['address'] = row[8]
        result['zipcode'] = row[9]
        result['priority'] = row[10]

        return result

    def build_supplier_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        result['username'] = row[3]
        result['password'] = row[4]
        result['email'] = row[5]
        result['phone'] = row[6]
        result['dateofbirth'] = row[7]
        result['address'] = row[8]
        result['zipcode'] = row[9]
        result['country'] = row[10]
        result['occupation'] = row[11]
        result['org_id'] = row[13]

        return result

    def build_request_dict(self, row):
        result = {}
        result['ord_id'] = row[0]
        result['quantity'] = row[1]
        result['date'] = row[2]
        result['pay_id'] = row[3]
        result['uid'] = row[4]
        result['rid'] = row[6]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['description'] = row[2]
        result['brand'] = row[3]
        result['quantity'] = row[4]
        result['price'] = row[5]
        result['latitude'] = row[6]
        result['longitude'] = row[7]
        result['date'] = row[8]
        result['uid'] = row[9]
        result['initial_quantity'] = row[10]
        return result

    def build_complete_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['description'] = row[2]
        result['brand'] = row[3]
        result['quantity'] = row[4]
        result['price'] = row[5]
        result['latitude'] = row[6]
        result['longitude'] = row[7]
        result['date'] = row[8]
        result['uid'] = row[9]
        result['initial_quantity'] = row[10]
        result['categoryId'] = row[11]

        if result['categoryId'] == 1: # Water
            result['calories'] = row[12]
            result['speciality'] = row[13]
            result['ounces'] = row[14]
        elif result['categoryId'] == 2: # Clothing
            result['gender'] = row[12]
            result['color'] = row[13]
            result['material'] = row[14]
            result['size'] = row[15]
        elif result['categoryId'] == 3: # Canned food
            result['calories'] = row[12]
            result['nutritionfacts'] = row[13]
            result['size'] = row[14]
            result['foodtype'] = row[15]
        elif result['categoryId'] == 4: # Baby food
            result['calories'] = row[12]
            result['nutritionfacts'] = row[13]
            result['size'] = row[14]
            result['foodtype'] = row[15]
        elif result['categoryId'] == 5: # Battery
            result['disposability'] = row[12]
            result['householdtype'] = row[13]
        elif result['categoryId'] == 6: # Dry food
            result['calories'] = row[12]
            result['nutritionfacts'] = row[13]
            result['size'] = row[14]
            result['foodtype'] = row[15]
        elif result['categoryId'] == 7: # Fuel
            result['type'] = row[12]
            result['amount'] = row[13]
        elif result['categoryId'] == 8: # Heavy equipment
            result['type'] = row[12]
        elif result['categoryId'] == 9: # Ice
            result['weight'] = row[12]
        elif result['categoryId'] == 10: # Medical device
            result['type'] = row[12]
        elif result['categoryId'] == 11: # Medication
            result['type'] = row[12]
            result['servingspercontainer'] = row[13]
        elif result['categoryId'] == 12: # Power generator
            result['genFuelType'] = row[12]
            result['type'] = row[13]
            result['wattage'] = row[14]
            result['color'] = row[15]
        elif result['categoryId'] == 13: # Tool
            result['material'] = row[12]
            result['field'] = row[13]

        return result

    def build_resource_attributes(self, rid, rname, description, brand, quantity, price, latitude,
                                  longitude, date, uid, initial_quantity):
        result = {}
        result['rid'] = rid
        result['rname'] = rname
        result['description'] = description
        result['brand'] = brand
        result['quantity'] = quantity
        result['price'] = price
        result['latitude'] = latitude
        result['longitude'] = longitude
        result['date'] = date
        result['uid'] = uid
        result['initial_quantity'] = initial_quantity

        return result


    def build_organization_dict(self, row):
        result = {}
        result['org_id'] = row[0]
        result['name'] = row[1]
        result['email'] = row[2]
        result['phone'] = row[3]
        result['zipcode'] = row[4]
        result['address'] = row[5]

        return result

    def build_purchases_dict(self,row):
        result = {}
        result['firstname'] = row[0]
        result['lastname'] = row[1]
        result['rid'] = row[2]
        result['rname'] = row[3]
        result['price'] = row[4]
        result['ord_id'] = row[5]
        result['quantity'] = row[6]
        result['date'] = row[7]
        result['uid'] = row[8]
        return result

    def build_requests_dict(self,row):
        result = {}
        result['firstname'] = row[0]
        result['lastname'] = row[1]
        result['rid'] = row[2]
        result['rname'] = row[3]
        result['ord_id'] = row[4]
        result['quantity'] = row[5]
        result['date'] = row[6]
        result['uid'] = row[7]
        return result

    def build_reserves_dict(self, row):
        result = {}
        result['firstname'] = row[0]
        result['lastname'] = row[1]
        result['rid'] = row[2]
        result['rname'] = row[3]
        result['ord_id'] = row[4]
        result['quantity'] = row[5]
        result['date'] = row[6]
        result['uid'] = row[7]
        return result