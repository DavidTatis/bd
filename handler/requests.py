from flask import jsonify


class RequestsHandler:
    def getAllRequests(self):
        requests = [
            {"req_id": 1, "ord_id": 1, "res_id": 1},
            {"req_id": 2, "ord_id": 2, "res_id": 2},
            {"req_id": 3, "ord_id": 3, "res_id": 3},
        ]
        return jsonify(Requests=requests), 200

    def getRequestById(self, req_id):
        requests = [
            {"req_id": 3, "ord_id": 3, "res_id": 3},
        ]
        return jsonify(Requests=requests), 200

    def searchRequests(self, args):
        requests = [
            {"req_id": 2, "ord_id": 2, "res_id": 2},
        ]
        return jsonify(Requests=requests,Args=args), 200
