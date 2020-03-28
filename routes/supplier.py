from flask import Flask, jsonify, request, Blueprint
from handler.supplier import SupplierHandler

supplier=Blueprint("supplier",__name__)

@supplier.route('/', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else :
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)



@supplier.route('/<int:sid>',
           methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error = "Method not allowed"), 405


@supplier.route('/<int:sid>/parts')
def getPartsBySuplierId(sid):
    return SupplierHandler().getPartsBySupplierId(sid)

