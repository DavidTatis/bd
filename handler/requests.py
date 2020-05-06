from flask import jsonify
from dao.requests import RequestsDAO
from handler.dictionary import Dictionary

class RequestsHandler:
    def getAllRequests(self):
        dao = RequestsDAO()
        requests = dao.getAllRequests()
        dic=Dictionary()
        result_list = []
        for row in requests:
            result = dic.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list), 200

    def getPurchasesById(self, req_id):
        dao = RequestsDAO()
        requests = dao.getPurchasesByID(req_id)
        dic = Dictionary()
        result_list = []
        for row in requests:
            result = dic.build_purchases_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list), 200

    def getRequestsByID(self, req_id):
        dao = RequestsDAO()
        requests = dao.getRequestsByID(req_id)
        dic = Dictionary()
        result_list = []
        for row in requests:
            result = dic.build_requests_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list), 200

    def getReservesByID(self, req_id):
        dao = RequestsDAO()
        requests = dao.getReservesByID(req_id)
        dic = Dictionary()
        result_list = []
        for row in requests:
            result = dic.build_reserves_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list), 200

    def searchRequests(self, args):
        requests = [
            {"req_id": 2, "ord_id": 2, "res_id": 2},
        ]
        return jsonify(Requests=requests,Args=args), 200
