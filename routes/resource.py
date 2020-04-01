from flask import Blueprint, request,jsonify
from handler.resources import ResourcesHandler
resources = Blueprint('resources', __name__)
#====================== RESOURCE ==============================
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

#== ISA RESOURCE:
#====================== WATER ==============================

@resources.route('/water/', methods=['GET', 'POST'])
def getAllWaterResources():
    if request.method == 'POST':
      return jsonify(Message="Water Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllWaterResources()
        else:
            return ResourcesHandler().searchWaterResources(request.args)


@resources.route('/water/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getWaterResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getWaterResourceById(resource_id)
    elif request.method == 'PUT':
        #ResourcesHandler().updateWaterResource(resource_id,request.form)
        return jsonify(Message="Water Resource update successful"), 200
    elif request.method == 'DELETE':
        #ResourcesHandler().deleteWaterResource(resource_id)
        return jsonify(Message="Water Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405

#====================== WATER ==============================
#====================== BATTERIES ==============================

@resources.route('/battery/', methods=['GET', 'POST'])
def getAllBatteryResources():
    if request.method == 'POST':
      return jsonify(Message="Battery Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllBatteryResources()
        else:
            return ResourcesHandler().searchBatteryResources(request.args)


@resources.route('/battery/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getBatteryResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getBatteryResourceById(resource_id)
    elif request.method == 'PUT':
        #ResourcesHandler().updateBatteryResource(resource_id,request.form)
        return jsonify(Message="Battery Resource update successful"), 200
    elif request.method == 'DELETE':
        #ResourcesHandler().deleteBatteryResource(resource_id)
        return jsonify(Message="Battery Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405

#====================== BATTERIES ==============================
#====================== POWER GENERATORS ==============================

@resources.route('/PowerGenerator/', methods=['GET', 'POST'])
def getAllPowerGeneratorResources():
    if request.method == 'POST':
      return jsonify(Message="Power Generators Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllPowerGeneratorResources()
        else:
            return ResourcesHandler().searchPowerGeneratorResources(request.args)


@resources.route('/PowerGenerator/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getPowerGeneratorResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getPowerGeneratorResourceById(resource_id)
    elif request.method == 'PUT':
        #ResourcesHandler().updatePowerGeneratorResource(resource_id,request.form)
        return jsonify(Message="Power Generator Resource update successful"), 200
    elif request.method == 'DELETE':
        #ResourcesHandler().deletePowerGeneratorResource(resource_id)
        return jsonify(Message="Power Generator Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405
#====================== POWER GENERATORS ==============================
#====================== TOOLS ==============================

@resources.route('/tool/', methods=['GET', 'POST'])
def getAllToolResources():
    if request.method == 'POST':
      return jsonify(Message="Tool Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllToolResources()
        else:
            return ResourcesHandler().searchToolResources(request.args)


@resources.route('/PowerGenerator/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getToolResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getToolResourceById(resource_id)
    elif request.method == 'PUT':
        #ResourcesHandler().updateToolResource(resource_id,request.form)
        return jsonify(Message="Tool Resource update successful"), 200
    elif request.method == 'DELETE':
        #ResourcesHandler().deleteToolResource(resource_id)
        return jsonify(Message="Tool Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405
#====================== TOOLS ==============================
#====================== CLOTHING ==============================

@resources.route('/clothing/', methods=['GET', 'POST'])
def getAllClothingResources():
    if request.method == 'POST':
      return jsonify(Message="Clothing Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllClothingResources()
        else:
            return ResourcesHandler().searchClothingResources(request.args)


@resources.route('/clothing/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getClothingResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getClothingResourceById(resource_id)
    elif request.method == 'PUT':
        #ResourcesHandler().updateClothingResource(resource_id,request.form)
        return jsonify(Message="Clothing Resource update successful"), 200
    elif request.method == 'DELETE':
        #ResourcesHandler().deleteClothingResource(resource_id)
        return jsonify(Message="Clothing Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405
#====================== CLOTHING ==============================