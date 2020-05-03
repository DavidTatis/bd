from flask import jsonify
from dao.users import UsersDAO

class OrganizationsHandler:
    def getAllOrganizations(self):
        dao = UsersDAO()
        organizations=dao.getAllUsers()
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
