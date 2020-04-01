from flask import jsonify


class OrganizationsHandler:
    def getAllOrganizations(self):
        organizations = [
            {"organization_id":1, "name": "Google", "email": 'google@gmail.com', "phone": 7877871234, "zipcode": 12458, "address": 'California'},
            {"organization_id": 2, "name": "Facebook", "email": 'facebook@facebook.com', "phone": 8024551234, "zipcode": 18568, "address": 'California'},
            {"organization_id": 3, "name": "Amazon Web Services", "email": 'amz@amazon.com', "phone": 9965401234, "zipcode": 98552, "address": 'California'},
        ]
        return jsonify(Organizations=organizations), 200

    def getOrganizationById(self, organization_id):
        organizations = [
            {"organization_id": 1, "name": "Google", "email": 'google@gmail.com', "phone": 7877871234, "zipcode": 12458, "address": 'California'}
        ]
        return jsonify(Organizations=organizations), 200

    def searchOrganizations(self, args):
        organizations = [
            {"organization_id": 1, "name": "Google", "email": 'google@gmail.com', "phone": 7877871234, "zipcode": 12458, "address": 'California'}
        ]
        return jsonify(Organizations=organizations,Args=args), 200
