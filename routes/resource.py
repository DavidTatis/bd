from flask import Blueprint, request,jsonify
from handler.resources import ResourcesHandler
resources = Blueprint('resources', __name__)

@resources.route('/', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
      return jsonify(Message="Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllResources()
        else:
            return ResourcesHandler().searchResources(request.args)


@resources.route('/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getResourceById(resource_id)
    elif request.method == 'PUT':
        #ResourcesHandler().updateResource(resource_id,request.form)
        return jsonify(Message="Resource update successful"), 200
    elif request.method == 'DELETE':
        #ResourcesHandler().deleteResource(resource_id)
        return jsonify(Message="Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405


