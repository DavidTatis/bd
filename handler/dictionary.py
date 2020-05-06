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
        result['name'] = row[1]
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

    def build_organization_dict(self, row):
        result = {}
        result['org_id'] = row[0]
        result['name'] = row[1]
        result['email'] = row[2]
        result['phone'] = row[3]
        result['zipcode'] = row[4]
        result['address'] = row[5]

        return result