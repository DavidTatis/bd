from flask import jsonify



class PaymentHandler:
    def getAllPayments(self):
        payments = [
            {"payment_id":1, "method":'Paypal',"amount":22000},
            {"payment_id":2, "method":'Paypal',"amount":33000},
            {"payment_id":3, "method":'Paypal',"amount":100},
        ]
        return jsonify(Payments=payments), 200

    def getPaymentById(self, payment_id):
        payments = [
            {"payment_id": 1, "name": 'Ariel'}
        ]
        return jsonify(Payments=payments), 200

    def searchPayments(self, args):
        payments = [
            {"payment_id": 1, "name": 'Ariel'}
        ]
        return jsonify(Payments=payments,Args=args), 200
