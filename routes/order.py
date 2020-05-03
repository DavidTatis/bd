from flask import Blueprint, request,jsonify
from handler.orders import OrdersHandler
orders = Blueprint('orders', __name__)

@orders.route('/', methods=['GET', 'POST'])
def getAllOrders():
    if request.method == 'POST':
      return jsonify(Message="Order created."), 200
    else:
        if not request.args:
            return OrdersHandler().getAllOrders()
        else:
            return OrdersHandler().searchOrders(request.args)


@orders.route('/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def getOrderById(order_id):
    if request.method == 'GET':
        return OrdersHandler().getOrderById(order_id)
    elif request.method == 'PUT':
        #OrdersHandler().updateOrder(order_id,request.form)
        return jsonify(Message="Order update successful"), 200
    elif request.method == 'DELETE':
        #OrdersHandler().deleteOrder(order_id)
        return jsonify(Message="Order delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405

