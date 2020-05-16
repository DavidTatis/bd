from flask import Blueprint, request,jsonify
from handler.organizations import OrganizationsHandler
organizations = Blueprint('organizations', __name__)

@organizations.route('/', methods=['GET', 'POST'])
def getAllOrganizations():
    if request.method == 'POST':
        return OrganizationsHandler().createOrganization(request.get_json())
    else:
        if not request.args:
            return OrganizationsHandler().getAllOrganizations()
        else:
            return OrganizationsHandler().searchOrganizations(request.args)


@organizations.route('/<int:organization_id>', methods=['GET', 'PUT', 'DELETE'])
def getOrganizationById(organization_id):
    if request.method == 'GET':
        return OrganizationsHandler().getOrganizationById(organization_id)
    elif request.method == 'PUT':
        #OrganizationsHandler().updateOrganization(organization_id,request.form)
        return jsonify(Message="Organization update successful"), 200
    elif request.method == 'DELETE':
        #OrganizationsHandler().deleteOrganization(organization_id)
        return jsonify(Message="Organization delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405


