from flask import Blueprint, request,jsonify
from handler.users import UserHandler
users = Blueprint('users', __name__)

@users.route('/', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
      #insert a user
      return jsonify(Message="User user created."), 201
    else:
        if not request.args:
            return UserHandler().getAllUsers()
        else:
            return UserHandler().searchUsers(request.args)

@users.route('/needed/', methods=['GET', 'POST'])
def getAllUsersInneed():
    if request.method=='GET':
        return UserHandler().getAllUsersInneed()

@users.route('/admin/', methods=['GET', 'POST'])
def getAllAdminUsers():
    if request.method == 'POST':
      return UserHandler().createUserAdmin(request.get_json())
    else:
        if not request.args:
            return UserHandler().getAllAdminUsers()
        else:
            return UserHandler().searchAdminUsers(request.args)

@users.route('/supplier/', methods=['GET', 'POST'])
def getAllSupplierUsers():
    if request.method == 'POST':
      #insert a user
      return UserHandler().createUserSupplier(request.get_json())
    else:
        if not request.args:
            return UserHandler().getAllSupplierUsers()
        else:
            return UserHandler().searchSupplierUsers(request.args)

@users.route('/consumer/', methods=['GET', 'POST'])
def getAllConsumerUsers():
    if request.method == 'POST':
      #insert a user
      return UserHandler().createUserConsumer(request.get_json())
    else:
        if not request.args:
            return UserHandler().getAllConsumerUsers()
        else:
            return UserHandler().searchConsumerUsers(request.args)

@users.route('/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def getUserById(user_id):
    if request.method == 'GET':
        return UserHandler().getUserById(user_id)
    elif request.method == 'PUT':
        #UserHandler().updateUser(user_id,request.form)
        return jsonify(Message="User update successful"), 200
    elif request.method == 'DELETE':
        #UserHandler().deleteUser(user_id)
        return jsonify(Message="User delete successful"), 200
    else:
        return jsonify(Error="Method not allowed."), 405

@users.route('/login/', methods=['POST'])
def loginUsers():
    if request.method == 'POST':
      return UserHandler().loginUser(request.get_json())

