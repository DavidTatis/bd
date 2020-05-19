from flask import Flask, jsonify, request, Blueprint
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin
from routes.order import orders
from routes.organization import organizations
from routes.resource import resources
from routes.payment import payments
from routes.request import requests
from routes.user import users

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

app.register_blueprint(users, url_prefix='/aid/users')
app.register_blueprint(orders, url_prefix='/aid/orders')
app.register_blueprint(organizations, url_prefix='/aid/organizations')
app.register_blueprint(resources, url_prefix='/aid/resources')
app.register_blueprint(payments, url_prefix='/aid/payments')
app.register_blueprint(requests, url_prefix='/aid/requests')


@app.route('/')
def greeting():
    return 'Hello, this is the Disaster Aid DB App!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


