from flask import jsonify
from dao.resources import ResourcesDAO
from handler.dictionary import Dictionary

class ResourcesHandler:
    def getAllResources(self):
        resources = [
            {"resource_id": 1, "quantity": 2, "description": 'Botellas de agua 13oz Dasani', "brand": 'Dasani', "price": 1.00, "lat": 18.0111, "long": 66.6141},
            {"resource_id": 2, "quantity": 23, "description": 'Bolsa de hielo 5 libras', "brand": 'La Hielera Inc', "price": 5.00, "lat": 18.0121, "long": 65.6181},
            {"resource_id": 3, "quantity": 5, "description": 'Salchichas Carmela', "brand": 'Carmela',  "price": 0.59, "lat": 18.0111, "long": 64.9876},
        ]
        return jsonify(resources=resources), 200

    def getAllResourcesAvailable(self):
        dao = ResourcesDAO()
        requests = dao.getAllResourcesAvailable()
        dic = Dictionary()
        result_list = []
        for row in requests:
            result = dic.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list), 200

    def getResourceById(self, resource_id):
        dao = ResourcesDAO()
        requests = dao.getResourceByID(resource_id)
        dic = Dictionary()
        result = dic.build_resource_dict(requests)
        return jsonify(Requests=result), 200

    def getResourceRequestedByName(self,rname):
        dao = ResourcesDAO()
        requests = dao.getResourceRequestedByName(rname)
        dic = Dictionary()
        result_list = []
        for row in requests:
            result = dic.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list), 200

    def getResourceAvailableByName(self,rname):
        dao = ResourcesDAO()
        requests = dao.getResourceAvailableByName(rname)
        dic = Dictionary()
        result_list = []
        for row in requests:
            result = dic.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list), 200

    def searchResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 2, "description": 'Botellas de agua 13oz Dasani', "brand": 'Dasani', "price": 1.00, "lat": 18.0111, "long": 66.6141}
        ]
        return jsonify(Resources=resources,Args=args), 200

    def getResourceRequestedByRequestID(self,rid,ord_id):
        dao = ResourcesDAO()
        requests = dao.getResourceRequestedByRequestID(rid,ord_id)
        dic = Dictionary()
        result_list = []
        for row in requests:
            result = dic.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list), 200















    #=============== WATER ===========================
    def getAllWaterResources(self):
        resources = [
            {"resource_id":1, "quantity": 2, "description": 'Botellas de agua 13oz Dasani', "brand": 'Dasani',  "price": 1.00, "lat": 18.0111, "long": 66.6141, "calories":0, "speciality":"mineral","container":"six pack","ounces_per_bottle":24},
            {"resource_id": 2, "quantity": 23, "description": 'Bolsa de hielo 5 libras', "brand": 'La Hielera Inc',  "price": 5.00, "lat": 18.0121, "long": 65.6181, "calories":0,"speciality":"mineral","container":"six pack","ounces_per_bottle":24},
            {"resource_id": 3, "quantity": 5, "description": 'Salchichas Carmela', "brand": 'Carmela',  "price": 0.59, "lat": 18.0111, "long": 64.9876,"calories":0,"speciality":"mineral","container":"six pack","ounces_per_bottle":24},
        ]
        return jsonify(resources=resources), 200

    def getWaterResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 2, "description": 'Botellas de agua 13oz Dasani', "brand": 'Dasani',  "price": 1.00, "lat": 18.0111, "long": 66.6141, "calories":0, "speciality":"mineral","container":"six pack","ounces_per_bottle":24}
        ]
        return jsonify(Resources=resources), 200

    def searchWaterResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 2, "description": 'Botellas de agua 13oz Dasani', "brand": 'Dasani',  "price": 1.00, "lat": 18.0111, "long": 66.6141, "calories":0, "speciality":"mineral","container":"six pack","ounces_per_bottle":24}
        ]
        return jsonify(Resources=resources,Args=args), 200



    # =============== BATTERIES ===========================
    def getAllBatteryResources(self):
        resources = [
            {"resource_id":1, "quantity": 20, "description": 'Baterias AAA', "brand": 'Duracell',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "disposability":'true' , "household_type":'Lithium'},
            {"resource_id": 2, "quantity": 123, "description": 'Baterias AA', "brand": 'Duracell',  "price": 6.00, "lat": 18.0121, "long": 65.6181, "disposability": 'true' ,"household_type":'Alkaline'},
            {"resource_id": 3, "quantity": 500, "description": 'Baterias DD', "brand": 'Duracell',  "price": 9.59, "lat": 18.0111, "long": 64.9876,"disposability": 'false' ,"household_type":'Lithium'},
        ]
        return jsonify(resources=resources), 200

    def getBatteryResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 20, "description": 'Baterias AAA', "brand": 'Duracell',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "disposability":'true' , "household_type":'Lithium'},
        ]
        return jsonify(Resources=resources), 200

    def searchBatteryResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 20, "description": 'Baterias AAA', "brand": 'Duracell',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "disposability":'true' , "household_type":'Lithium'},
        ]
        return jsonify(Resources=resources,Args=args), 200



    # =============== POWER GENERATOR ===========================
    def getAllPowerGeneratorResources(self):
        resources = [
            {"resource_id":1, "quantity": 24, "description": 'Inverter Generator', "brand": 'Honda',  "price": 2250.00, "lat": 18.0111, "long": 66.6141, "generator_fuel_type": 'Diesel' , "type": 'Inverter', "wattage": '8000w', "color": 'Red'},
            {"resource_id": 2, "quantity": 23, "description": 'Portable Generator', "brand": 'Duromax',  "price": 300.00, "lat": 18.0121, "long": 65.6181, "generator_fuel_type": 'Gasoline' ,"type": 'Portable', "wattage": '4000w', "color": 'Blue'},
            {"resource_id": 3, "quantity": 50, "description": 'Portable Generator', "brand": 'Sportsman',  "price": 900.99, "lat": 18.0111, "long": 64.9876,"generator_fuel_type": 'Gasoline' ,"type": 'Portable', "wattage": '3000w', "color": 'Yellow'},
        ]
        return jsonify(resources=resources), 200

    def getPowerGeneratorResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 24, "description": 'Inverter Generator', "brand": 'Honda',  "price": 2250.00, "lat": 18.0111, "long": 66.6141, "generator_fuel_type": 'Diesel' , "type": 'Inverter', "wattage": '8000w', "color": 'Red'},
        ]
        return jsonify(Resources=resources), 200

    def searchPowerGeneratorResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 24, "description": 'Inverter Generator', "brand": 'Honda',  "price": 2250.00, "lat": 18.0111, "long": 66.6141, "generator_fuel_type": 'Diesel' , "type": 'Inverter', "wattage": '8000w', "color": 'Red'},
        ]
        return jsonify(Resources=resources,Args=args), 200




    # =============== TOOLS ===========================
    def getAllToolResources(self):
        resources = [
            {"resource_id":1, "quantity": 2000, "description": 'Hammer 24', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "material":'Aluminum' , "field":'General'},
            {"resource_id": 2, "quantity": 123, "description": 'Saw 3 Feetlong', "brand": 'Home Depot',  "price": 16.00, "lat": 18.0121, "long": 65.6181, "material": 'Steel' ,"field":'Carpenter'},
            {"resource_id": 3, "quantity": 50000, "description": 'Wood Plank 4 feet long', "brand": 'Home Depot',  "price": 4.00, "lat": 18.0111, "long": 64.9876, "material": 'Wood' , "field": 'Carpenter'},
        ]
        return jsonify(resources=resources), 200

    def getToolResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 2000, "description": 'Hammer 24', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "material":'Aluminum' , "field":'General'},
        ]
        return jsonify(Resources=resources), 200

    def searchToolResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 2000, "description": 'Hammer 24', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "material":'Aluminum' , "field":'General'},
        ]
        return jsonify(Resources=resources,Args=args), 200




    # =============== CLOTHING ===========================
    def getAllClothingResources(self):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Hammer 24', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 2, "quantity": 123, "description": 'Saw 3 Feetlong', "brand": 'Home Depot',  "price": 16.00, "lat": 18.0121, "long": 65.6181, "Size":'Small' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 3, "quantity": 50000, "description": 'Wood Plank 4 feet long', "brand": 'Home Depot',  "price": 4.00, "lat": 18.0111, "long": 64.9876, "Size":'Large' , "Gender":'Male', "color": 'Blue', "material": 'Cotton'},
        ]
        return jsonify(resources=resources), 200

    def getClothingResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Hammer 24', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources), 200

    def searchClothingResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Hammer 24', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources,Args=args), 200

    # =============== HEAVY EQUIPMENT ===========================
    def getAllHeavyEquipmentResources(self):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Heavy Equipment 1', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 2, "quantity": 123, "description": 'Heavy Equipment 2', "brand": 'Home Depot',  "price": 16.00, "lat": 18.0121, "long": 65.6181, "Size":'Small' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 3, "quantity": 50000, "description": 'Heavy Equipment 3', "brand": 'Home Depot',  "price": 4.00, "lat": 18.0111, "long": 64.9876, "Size":'Large' , "Gender":'Male', "color": 'Blue', "material": 'Cotton'},
        ]
        return jsonify(resources=resources), 200

    def getHeavyEquipmentResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Heavy Equipment ID', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources), 200

    def searchHeavyEquipmentResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Heavy Equipment Search', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources,Args=args), 200

    # =============== ICE ===========================
    def getAllIceResources(self):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'ICE 1', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 2, "quantity": 123, "description": 'ICE 2', "brand": 'Home Depot',  "price": 16.00, "lat": 18.0121, "long": 65.6181, "Size":'Small' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 3, "quantity": 50000, "description": 'ICE 3', "brand": 'Home Depot',  "price": 4.00, "lat": 18.0111, "long": 64.9876, "Size":'Large' , "Gender":'Male', "color": 'Blue', "material": 'Cotton'},
        ]
        return jsonify(resources=resources), 200

    def getIceResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'ICE ID', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources), 200

    def searchIceResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'ICE Search', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources,Args=args), 200

    # =============== MEDICAL DEVICE ===========================
    def getAllMedicalDeviceResources(self):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Medical Device 1', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 2, "quantity": 123, "description": 'Medical Device 2', "brand": 'Home Depot',  "price": 16.00, "lat": 18.0121, "long": 65.6181, "Size":'Small' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 3, "quantity": 50000, "description": 'Medical Device 3', "brand": 'Home Depot',  "price": 4.00, "lat": 18.0111, "long": 64.9876, "Size":'Large' , "Gender":'Male', "color": 'Blue', "material": 'Cotton'},
        ]
        return jsonify(resources=resources), 200

    def getMedicalDeviceResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Medical Device ID', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources), 200

    def searchMedicalDeviceResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Medical Device Search', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources,Args=args), 200

    # =============== FUEL ===========================
    def getAllFuelResources(self):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Fuel 1', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 2, "quantity": 123, "description": 'Fuel 2', "brand": 'Home Depot',  "price": 16.00, "lat": 18.0121, "long": 65.6181, "Size":'Small' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 3, "quantity": 50000, "description": 'Fuel 3', "brand": 'Home Depot',  "price": 4.00, "lat": 18.0111, "long": 64.9876, "Size":'Large' , "Gender":'Male', "color": 'Blue', "material": 'Cotton'},
        ]
        return jsonify(resources=resources), 200

    def getFuelResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Fuel ID', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources), 200

    def searchFuelResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Fuel Search', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources,Args=args), 200



    # =============== CANNED FOOD ===========================
    def getAllCannedFoodResources(self):
        resources = [
            {"resource_id": 1, "quantity": 500, "description": 'Salchicha carmela', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 2, "quantity": 123, "description": 'Saw 3 Feetlong', "brand": 'Home Depot',  "price": 16.00, "lat": 18.0121, "long": 65.6181, "Size":'Small' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 3, "quantity": 50000, "description": 'Wood Plank 4 feet long', "brand": 'Home Depot',  "price": 4.00, "lat": 18.0111, "long": 64.9876, "Size":'Large' , "Gender":'Male', "color": 'Blue', "material": 'Cotton'},
        ]
        return jsonify(resources=resources), 200

    def getCannedFoodResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Salchicha carmela', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources), 200

    def searchCannedFoodResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Salchicha carmela', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources,Args=args), 200



    # =============== DRY FOOD ===========================
    def getAllDryFoodResources(self):
        resources = [
            {"resource_id": 1, "quantity": 500, "description": 'Mezcla de Pancake', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 2, "quantity": 123, "description": 'Saw 3 Feetlong', "brand": 'Home Depot',  "price": 16.00, "lat": 18.0121, "long": 65.6181, "Size":'Small' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 3, "quantity": 50000, "description": 'Wood Plank 4 feet long', "brand": 'Home Depot',  "price": 4.00, "lat": 18.0111, "long": 64.9876, "Size":'Large' , "Gender":'Male', "color": 'Blue', "material": 'Cotton'},
        ]
        return jsonify(resources=resources), 200

    def getDryFoodResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Mezcla de Pancake', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources), 200

    def searchDryFoodResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Mezcla de Pancake', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources,Args=args), 200



    # =============== BABY FOOD ===========================
    def getAllBabyFoodResources(self):
        resources = [
            {"resource_id": 1, "quantity": 500, "description": 'Baby Food Guineo', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 2, "quantity": 123, "description": 'Saw 3 Feetlong', "brand": 'Home Depot',  "price": 16.00, "lat": 18.0121, "long": 65.6181, "Size":'Small' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 3, "quantity": 50000, "description": 'Wood Plank 4 feet long', "brand": 'Home Depot',  "price": 4.00, "lat": 18.0111, "long": 64.9876, "Size":'Large' , "Gender":'Male', "color": 'Blue', "material": 'Cotton'},
        ]
        return jsonify(resources=resources), 200

    def getBabyFoodResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Baby Food Guineo', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources), 200

    def searchBabyFoodResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Baby Food Guineo', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources,Args=args), 200



    # =============== MEDICATION ===========================
    def getAllMedicationResources(self):
        resources = [
            {"resource_id": 1, "quantity": 500, "description": 'Tylenol', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 2, "quantity": 123, "description": 'Saw 3 Feetlong', "brand": 'Home Depot',  "price": 16.00, "lat": 18.0121, "long": 65.6181, "Size":'Small' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
            {"resource_id": 3, "quantity": 50000, "description": 'Wood Plank 4 feet long', "brand": 'Home Depot',  "price": 4.00, "lat": 18.0111, "long": 64.9876, "Size":'Large' , "Gender":'Male', "color": 'Blue', "material": 'Cotton'},
        ]
        return jsonify(resources=resources), 200

    def getMedicationResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Tylenol', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources), 200

    def searchMedicationResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 500, "description": 'Tylenols', "brand": 'Home Depot',  "price": 2.00, "lat": 18.0111, "long": 66.6141, "Size":'Medium' , "Gender":'Male', "color": 'Red', "material": 'Cotton'},
        ]
        return jsonify(Resources=resources,Args=args), 200
