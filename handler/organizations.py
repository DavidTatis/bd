from flask import jsonify


class OrganizationsHandler:
    def getAllOrganizations(self):
        organizations = [
            {"organization_id":1, "name": "Google"},
            {"organization_id": 2, "name": "Facebook"},
            {"organization_id": 3, "name": "AWS"},
        ]
        return jsonify(Organizations=organizations), 200

    def getOrganizationById(self, organization_id):
        organizations = [
            {"organization_id": 1, "name": "Google"}
        ]
        return jsonify(Organizations=organizations), 200

    def searchOrganizations(self, args):
        organizations = [
            {"organization_id": 1, "name": "Google"}
        ]
        return jsonify(Organizations=organizations,Args=args), 200
