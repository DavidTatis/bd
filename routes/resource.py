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





#====================== POWER GENERATORS ==============================

@resources.route('/powerGenerator/', methods=['GET', 'POST'])
def getAllPowerGeneratorResources():
    if request.method == 'POST':
      return jsonify(Message="Power Generators Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllPowerGeneratorResources()
        else:
            return ResourcesHandler().searchPowerGeneratorResources(request.args)


@resources.route('/powerGenerator/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
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


@resources.route('/tool/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
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

# ====================== CANNED FOOD ==============================

@resources.route('/cannedFood/', methods=['GET', 'POST'])
def getAllCannedFoodResources():
    if request.method == 'POST':
        return jsonify(Message="Canned Food Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllCannedFoodResources()
        else:
            return ResourcesHandler().searchCannedFoodResources(request.args)

@resources.route('/cannedFood/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getCannedFoodResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getCannedFoodResourceById(resource_id)
    elif request.method == 'PUT':
        # ResourcesHandler().updateClothingResource(resource_id,request.form)
        return jsonify(Message="Canned Food Resource update successful"), 200
    elif request.method == 'DELETE':
        # ResourcesHandler().deleteClothingResource(resource_id)
        return jsonify(Message="Canned Food Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405

# ====================== DRY FOOD ==============================

@resources.route('/dryFood/', methods=['GET', 'POST'])
def getAllDryFoodResources():
    if request.method == 'POST':
        return jsonify(Message="Dry Food Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllDryFoodResources()
        else:
            return ResourcesHandler().searchDryFoodResources(request.args)

@resources.route('/dryFood/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getDryFoodResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getDryFoodResourceById(resource_id)
    elif request.method == 'PUT':
        # ResourcesHandler().updateClothingResource(resource_id,request.form)
        return jsonify(Message="Dry Food Resource update successful"), 200
    elif request.method == 'DELETE':
        # ResourcesHandler().deleteClothingResource(resource_id)
        return jsonify(Message="Dry Food Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405

# ====================== BABY FOOD ==============================

@resources.route('/babyFood/', methods=['GET', 'POST'])
def getAllBabyFoodResources():
    if request.method == 'POST':
        return jsonify(Message="Baby Food Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllBabyFoodResources()
        else:
            return ResourcesHandler().searchBabyFoodResources(request.args)

@resources.route('/babyFood/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getBabyFoodResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getBabyFoodResourceById(resource_id)
    elif request.method == 'PUT':
        # ResourcesHandler().updateClothingResource(resource_id,request.form)
        return jsonify(Message="Baby Food Resource update successful"), 200
    elif request.method == 'DELETE':
        # ResourcesHandler().deleteClothingResource(resource_id)
        return jsonify(Message="Baby Food Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405

# ====================== MEDICATION ==============================

@resources.route('/medication/', methods=['GET', 'POST'])
def getAllMedicationResources():
    if request.method == 'POST':
        return jsonify(Message="Medication Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllMedicationResources()
        else:
            return ResourcesHandler().searchMedicationResources(request.args)

@resources.route('/medication/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getMedicationResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getMedicationResourceById(resource_id)
    elif request.method == 'PUT':
        # ResourcesHandler().updateClothingResource(resource_id,request.form)
        return jsonify(Message="Medication Resource update successful"), 200
    elif request.method == 'DELETE':
        # ResourcesHandler().deleteClothingResource(resource_id)
        return jsonify(Message="Medication Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405