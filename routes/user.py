from flask import Blueprint, request,jsonify
from handler.users import UserHandler
users = Blueprint('users', __name__)

@users.route('/', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
      #insert a user
      return jsonify(Message="User created."), 200
    else:
        if not request.args:
            return UserHandler().getAllUsers()
        else:
            return UserHandler().searchUsers(request.args)


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


