from flask import Flask, jsonify, request, Blueprint

# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin
from routes.user import users
from routes.order import orders
from routes.resource import resources


# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

app.register_blueprint(users, url_prefix='/Supply/users')
app.register_blueprint(orders, url_prefix='/Supply/orders')
app.register_blueprint(resources, url_prefix='/Supply/resources')


@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'


if __name__ == '__main__':
    app.run()