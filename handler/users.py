from flask import jsonify
#from dao.users import UsersDAO


class UserHandler:
    def getAllUsers(self):
        users = [
            {"user_id": 1, "firstname":'Ariel', "lastname": 'Silva', "username": 'ArielSilva', "password": 'pass',"email": 'ariel.silva@upr.edu',
             "phone": 7871234567, "dateOfBirth": 12211996, "Address": 'Mayaguez', "Zipcode": 10966},
            {"user_id": 2, "firstname":'David', "lastname": 'Tatis', "username": 'DavidTatis', "password": 'password',"email": 'david.tatis@upr.edu',
             "phone": 7871178921, "dateOfBirth": 1015996, "Address": 'Mayaguez', "Zipcode": 10845},
            {"user_id": 3, "firstname":'Javier', "lastname": 'Hernandez', "username": 'JavierHernandez', "password": 'baticueva',"email": 'javier.hernandez@upr.edu',
             "phone": 7874551223, "dateOfBirth": 12281996, "Address": 'Ponce', "Zipcode": 206800},
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
            {"user_id": 1, "firstname": 'Ariel', "lastname": 'Silva', "username": 'ArielSilva', "password": 'pass',"email": 'ariel.silva@upr.edu',
             "phone": 7871234567, "dateOfBirth": 12211996, "Address": 'Mayaguez', "Zipcode": 10966}
        ]
        return jsonify(Users=users), 200

    def searchUsers(self, args):
        users = [
            {"user_id": 1, "firstname": 'Ariel', "lastname": 'Silva', "username": 'ArielSilva', "password": 'pass',"email": 'ariel.silva@upr.edu',
             "phone": 7871234567, "dateOfBirth": 12211996, "Address": 'Mayaguez', "Zipcode": 10966}
        ]
        return jsonify(Users=users,Args=args), 200
