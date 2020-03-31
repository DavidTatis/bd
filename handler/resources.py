from flask import jsonify


class ResourcesHandler:
    def getAllResources(self):
        resources = [
            {"resource_id":1, "quantity": 2},
            {"resource_id": 2, "quantity": 23},
            {"resource_id": 3, "quantity": 5},
        ]
        return jsonify(resources=resources), 200

    def getResourceById(self, resource_id):
        resources = [
            {"resource_id": 1, "quantity": 5}
        ]
        return jsonify(Resources=resources), 200

    def searchResources(self, args):
        resources = [
            {"resource_id": 1, "quantity": 2}
        ]
        return jsonify(Resources=resources,Args=args), 200
