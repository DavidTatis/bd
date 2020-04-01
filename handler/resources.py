from flask import jsonify


class ResourcesHandler:
    def getAllResources(self):
        resources = [
            {"resource_id":1, "quantity": 2, "description": 'Botellas de agua 13oz Dasani', "brand": 'Dasani', "quantity": 100, "price": 1.00, "lat": 18.0111, "long": 66.6141},
            {"resource_id": 2, "quantity": 23, "description": 'Bolsa de hielo 5 libras', "brand": 'La Hielera Inc', "quantity": 10, "price": 5.00, "lat": 18.0121, "long": 65.6181},
            {"resource_id": 3, "quantity": 5, "description": 'Salchichas Carmela', "brand": 'Carmela', "quantity": 500, "price": 0.59, "lat": 18.0111, "long": 64.9876},
        ]
        return jsonify(resources=resources), 200

    def getResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 2, "description": 'Botellas de agua 13oz Dasani', "brand": 'Dasani', "quantity": 100, "price": 1.00, "lat": 18.0111, "long": 66.6141}
        ]
        return jsonify(Resources=resources), 200

    def searchResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 2, "description": 'Botellas de agua 13oz Dasani', "brand": 'Dasani', "quantity": 100, "price": 1.00, "lat": 18.0111, "long": 66.6141}
        ]
        return jsonify(Resources=resources,Args=args), 200

    #=============== WATER ===========================
    def getAllWaterResources(self):
        resources = [
            {"resource_id":1, "quantity": 2, "description": 'Botellas de agua 13oz Dasani', "brand": 'Dasani', "quantity": 100, "price": 1.00, "lat": 18.0111, "long": 66.6141, "calories":0, "speciality":"mineral","container":"six pack","ounces_per_bottle":24},
            {"resource_id": 2, "quantity": 23, "description": 'Bolsa de hielo 5 libras', "brand": 'La Hielera Inc', "quantity": 10, "price": 5.00, "lat": 18.0121, "long": 65.6181, "calories":0,"speciality":"mineral","container":"six pack","ounces_per_bottle":24},
            {"resource_id": 3, "quantity": 5, "description": 'Salchichas Carmela', "brand": 'Carmela', "quantity": 500, "price": 0.59, "lat": 18.0111, "long": 64.9876,"calories":0,"speciality":"mineral","container":"six pack","ounces_per_bottle":24},
        ]
        return jsonify(resources=resources), 200

    def getWaterResourceById(self, resource_id):
        resources = [
            {"resource_id":1, "quantity": 2, "description": 'Botellas de agua 13oz Dasani', "brand": 'Dasani', "quantity": 100, "price": 1.00, "lat": 18.0111, "long": 66.6141, "calories":0, "speciality":"mineral","container":"six pack","ounces_per_bottle":24}
        ]
        return jsonify(Resources=resources), 200

    def searchWaterResources(self, args):
        resources = [
            {"resource_id":1, "quantity": 2, "description": 'Botellas de agua 13oz Dasani', "brand": 'Dasani', "quantity": 100, "price": 1.00, "lat": 18.0111, "long": 66.6141, "calories":0, "speciality":"mineral","container":"six pack","ounces_per_bottle":24}
        ]
        return jsonify(Resources=resources,Args=args), 200