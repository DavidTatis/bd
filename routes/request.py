from flask import Blueprint, request,jsonify
from handler.requests import RequestsHandler
requests = Blueprint('requests', __name__)

@requests.route('/', methods=['GET', 'POST'])
def getAllRequests():
    if request.method == 'POST':
      #insert a request
      return jsonify(Message="Request created."), 200
    else:
        if not request.args:
            return RequestsHandler().getAllRequests()
        else:
            return RequestsHandler().searchRequests(request.args)


@requests.route('/<int:req_id>', methods=['GET', 'PUT', 'DELETE'])
def getRequestById(req_id):
    if request.method == 'GET':
        return RequestsHandler().getRequestById(req_id)
    elif request.method == 'PUT':
        return jsonify(Message="Request update successful"), 200
    elif request.method == 'DELETE':
        return jsonify(Message="Request delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405