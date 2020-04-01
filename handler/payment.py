from flask import jsonify


class PaymentsHandler:
    def getAllPayments(self):
        payments = [
            {"payment_id": 1, "method": 'visa', "amount": 100, "date": 1585683736555},
            {"payment_id": 2, "method": 'visa', "amount": 50, "date": 1158746985455},
            {"payment_id": 3, "method": 'visa', "amount": 80, "date": 1632568956205},
        ]
        return jsonify(Payments=payments), 200

    def getPaymentById(self, payment_id):
        payments = [
            {"payment_id": 3, "method": 'visa', "amount": 80, "date": 1632568956205}
        ]
        return jsonify(Payments=payments), 200

    def searchPayments(self, args):
        payments = [
            {"payment_id": 1, "method": 'visa', "amount": 100, "date": 1585683736555}
        ]
        return jsonify(Payments=payments,Args=args), 200
