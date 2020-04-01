from flask import Blueprint, request,jsonify
from handler.payments import PaymentHandler
payments = Blueprint('payments', __name__)

@payments.route('/', methods=['GET', 'POST'])
def getAllPayments():
    if request.method == 'POST':
      #insert a payment
      return jsonify(Message="Payment created."), 200
    else:
        if not request.args:
            return PaymentHandler().getAllPayments()
        else:
            return PaymentHandler().searchPayments(request.args)


@payments.route('/<int:payment_id>', methods=['GET', 'PUT', 'DELETE'])
def getPaymentById(payment_id):
    if request.method == 'GET':
        return PaymentHandler().getPaymentById(payment_id)
    elif request.method == 'PUT':
        #PaymentHandler().updatePayment(payment_id,request.form)
        return jsonify(Message="Payment update successful"), 200
    elif request.method == 'DELETE':
        #PaymentHandler().deletePayment(payment_id)
        return jsonify(Message="Payment delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405


