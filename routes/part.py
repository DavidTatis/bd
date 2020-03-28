from handler.parts import PartHandler
from flask import Flask, jsonify, request, Blueprint

parts=Blueprint("parts",__name__)


@parts.route('/', methods=['GET', 'POST'])
def getAllParts():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return PartHandler().insertPartJson(request.json)
    else:
        if not request.args:
            return PartHandler().getAllParts()
        else:
            return PartHandler().searchParts(request.args)

@parts.route('/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
def getPartById(pid):
    if request.method == 'GET':
        return PartHandler().getPartById(pid)
    elif request.method == 'PUT':
        return PartHandler().updatePart(pid, request.form)
    elif request.method == 'DELETE':
        return PartHandler().deletePart(pid)
    else:
        return jsonify(Error="Method not allowed."), 405



@parts.route('/<int:pid>/suppliers')
def getSuppliersByPartId(pid):
    return PartHandler().getSuppliersByPartId(pid)


@parts.route('/PartApp/parts/countbypartid')
def getCountByPartId():
    return PartHandler().getCountByPartId()
