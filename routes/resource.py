from flask import Blueprint, request,jsonify
from handler.resources import ResourcesHandler
resources = Blueprint('resources', __name__)
#====================== RESOURCE ==============================
@resources.route('/', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        #return ResourcesHandler().insertResourceJson(request.json)
        return jsonify(Message="Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllResources()
        else:
            return ResourcesHandler().searchResources(request.args)

@resources.route('/available/', methods=['GET', 'POST'])
def getAllResourcesAvailable():
    if request.method == 'GET':
        return ResourcesHandler().getAllResourcesAvailable()



@resources.route('/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getResourceById(resource_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@resources.route('/requested/name/<string:rname>', methods=['GET', 'PUT', 'DELETE'])
def getResourceRequestedByName(rname):
    if request.method == 'GET':
        return ResourcesHandler().getResourceRequestedByName(rname)
    else:
        return jsonify(Error="Method not allowed."), 405

@resources.route('/available/name/<string:rname>', methods=['GET', 'PUT', 'DELETE'])
def getResourceAvailableByName(rname):
    if request.method == 'GET':
        return ResourcesHandler().getResourceAvailableByName(rname)
    else:
        return jsonify(Error="Method not allowed."), 405


@resources.route('/<int:rid>/order/<int:ord_id>', methods=['GET', 'PUT', 'DELETE'])
def getResourceRequestedByRequestID(rid,ord_id):
    if request.method == 'GET':
        return ResourcesHandler().getResourceRequestedByRequestID(rid,ord_id)
    else:
        return jsonify(Error="Method not allowed."), 405

#== ISA RESOURCE:
#====================== WATER ==============================

@resources.route('/water/', methods=['GET', 'POST'])
def getAllWaterResources():
    if request.method == 'POST':
        return ResourcesHandler().insertWater(request.get_json())
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
        return ResourcesHandler().insertBattery(request.get_json())
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
      return ResourcesHandler().insertPowerGenerator(request.get_json())
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
        return ResourcesHandler().insertTool(request.get_json())
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
      return ResourcesHandler().insertClothing(request.get_json())
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

# ====================== HEAVY EQUIPMENT ==============================

@resources.route('/heavyEquipment/', methods=['GET', 'POST'])
def getAllHeavyEquipmentResources():
    if request.method == 'POST':
        return ResourcesHandler().insertHeavyEquipment(request.get_json())
    else:
        if not request.args:
            return ResourcesHandler().getAllHeavyEquipmentResources()
        else:
            return ResourcesHandler().searchHeavyEquipmentResources(request.args)

@resources.route('/heavyEquipment/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getHeavyEquipmentResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getHeavyEquipmentResourceById(resource_id)
    elif request.method == 'PUT':
        # ResourcesHandler().updateHeavyEquipmentResource(resource_id,request.form)
        return jsonify(Message="Heavy Equipment Resource update successful"), 200
    elif request.method == 'DELETE':
        # ResourcesHandler().deleteHeavyEquipmentResource(resource_id)
        return jsonify(Message="Heavy Equipment Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405

# ====================== ICE ==============================

@resources.route('/ice/', methods=['GET', 'POST'])
def getAllIceResources():
    if request.method == 'POST':
        return jsonify(Message="Ice Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllIceResources()
        else:
            return ResourcesHandler().searchIceResources(request.args)

@resources.route('/ice/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getIceResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getIceResourceById(resource_id)
    elif request.method == 'PUT':
        # ResourcesHandler().updateIceResource(resource_id,request.form)
        return jsonify(Message="Ice Resource update successful"), 200
    elif request.method == 'DELETE':
        # ResourcesHandler().deleteIceResource(resource_id)
        return jsonify(Message="Ice Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405

# ====================== MEDICAL DEVICE ==============================

@resources.route('/medicalDevice/', methods=['GET', 'POST'])
def getAllMedicalDeviceResources():
    if request.method == 'POST':
        return jsonify(Message="Medical Device Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllMedicalDeviceResources()
        else:
            return ResourcesHandler().searchMedicalDeviceResources(request.args)

@resources.route('/medicalDevice/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getMedicalDeviceResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getMedicalDeviceResourceById(resource_id)
    elif request.method == 'PUT':
        # ResourcesHandler().updateMedicalDeviceResource(resource_id,request.form)
        return jsonify(Message="Medical Device update successful"), 200
    elif request.method == 'DELETE':
        # ResourcesHandler().deleteMedicalDeviceResource(resource_id)
        return jsonify(Message="Medical Device Resource delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405

# ====================== FUEL ==============================

@resources.route('/fuel/', methods=['GET', 'POST'])
def getAllFuelResources():
    if request.method == 'POST':
        return jsonify(Message="Fuel Resource created."), 200
    else:
        if not request.args:
            return ResourcesHandler().getAllFuelResources()
        else:
            return ResourcesHandler().searchFuelResources(request.args)

@resources.route('/fuel/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def getFuelResourceById(resource_id):
    if request.method == 'GET':
        return ResourcesHandler().getFuelResourceById(resource_id)
    elif request.method == 'PUT':
        # ResourcesHandler().updateFuelResource(resource_id,request.form)
        return jsonify(Message="Fuel Resource update successful"), 200
    elif request.method == 'DELETE':
        # ResourcesHandler().deleteFuelResource(resource_id)
        return jsonify(Message="Fuel Resource delete successful"), 200
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