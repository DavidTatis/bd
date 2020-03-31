from flask import jsonify


class OrdersHandler:
    def getAllOrders(self):
        orders = [
            {"order_id":1, "quantity": 2},
            {"order_id": 2, "quantity": 23},
            {"order_id": 3, "quantity": 5},
        ]
        return jsonify(Orders=orders), 200

    def getOrderById(self, order_id):
        orders = [
            {"order_id": 1, "quantity": 5}
        ]
        return jsonify(Orders=orders), 200

    def searchOrders(self, args):
        orders = [
            {"order_id": 1, "quantity": 2}
        ]
        return jsonify(Orders=orders,Args=args), 200
