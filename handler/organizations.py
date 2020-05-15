from flask import jsonify
from dao.organizations import OrganizationsDAO
from handler.dictionary import Dictionary

class OrganizationsHandler:
    def getAllOrganizations(self):
        dao = OrganizationsDAO()
        dic = Dictionary()
        organizations_list = dao.getAllOrganizations()
        organizations = []
        for row in organizations_list:
            result = dic.build_organization_dict(row)
            organizations.append(result)
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

    def createOrganization(self,form):
        if form:
            name=form['name']
            email = form['email']
            phone = form['phone']
            zipcode = form['zipcode']
            address = form['address']
            dao=OrganizationsDAO()
            organization_id=dao.insert(name,email,phone,address,zipcode)
            result = {}
            result["organization_id"] = organization_id
            return jsonify(Organization=result), 201

