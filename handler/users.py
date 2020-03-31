from flask import jsonify
#from dao.users import UsersDAO


class UserHandler:
    def getAllUsers(self):
        users = [
            {"user_id":1, "name":'Ariel'},
            {"user_id": 2, "name": 'David'},
            {"user_id": 3, "name": 'Javier'},
        ]
        return jsonify(Users=users), 200

    def getAllAdminUsers(self):
        users = [
            {"user_id":1, "name":'Ariel'},
            {"user_id": 2, "name": 'David'},
            {"user_id": 3, "name": 'Javier'},
        ]
        return jsonify(Users=users), 200

    def getUserById(self, user_id):
        users = [
            {"user_id": 1, "name": 'Ariel'}
        ]
        return jsonify(Users=users), 200

    def searchUsers(self, args):
        users = [
            {"user_id": 1, "name": 'Ariel'}
        ]
        return jsonify(Users=users,Args=args), 200
