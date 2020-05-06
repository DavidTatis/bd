from flask import jsonify
from dao.users import UsersDAO


class UserHandler:
    def getAllUsers(self):
        dao = UsersDAO()
        users = dao.getAllUsers()
        result_list=[]
        for row in users:
            result=self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list), 200

    def getAllAdminUsers(self):
        dao = UsersDAO()
        users = dao.getAllAdminUsers()
        return jsonify(Users=users), 200

    def getAllSupplierUsers(self):
        dao = UsersDAO()
        users = dao.getAllSupplierUsers()
        return jsonify(Users=users), 200

    def getAllConsumerUsers(self):
        dao = UsersDAO()
        users = dao.getAllConsumerUsers()
        return jsonify(Users=users), 200

    def getUserById(self, user_id):
        users = [
            {"user_id": 4, "firstName": 'Ariel', "lastName": 'Silva',
             "username": 'ArielSilva', "password": 'pass',
             "email": 'ariel.silva@upr.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Mayagüez', "Zipcode": 10966}
        ]
        return jsonify(Users=users), 200

    def searchUsers(self, args):
        users = [
            {"user_id": 5, "firstName": 'David', "lastName": 'Tatis',
             "username": 'DavidTatis', "password": 'pass',
             "email": 'david.tatis@upr.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Mayagüez', "Zipcode": 10966}
        ]
        return jsonify(Users=users,Args=args), 200

    def searchAdminUsers(self, args):
        users = [
            {"user_id": 1, "firstName": 'Manuel', "lastName": 'Rodríguez',
             "username": 'ManuelRodriguez', "password": 'pass',
             "email": 'manuel.rodriguez@upr.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Mayagüez', "Zipcode": 10966}
        ]
        return jsonify(Users=users,Args=args), 200

    def searchSupplierUsers(self, args):
        users = [
            {"user_id": 4, "firstName": 'Ariel', "lastName": 'Silva',
             "username": 'ArielSilva', "password": 'pass',
             "email": 'ariel.silva@upr.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Mayagüez', "Zipcode": 10966}
        ]
        return jsonify(Users=users,Args=args), 200

    def searchConsumerUsers(self, args):
        users = [
            {"user_id": 7, "firstName": 'Pablo', "lastName": 'Escobar',
             "username": 'PabloEscobar', "password": 'baticueva',
             "email": 'pablo.escobar@cali.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Mayagüez', "Zipcode": 10966}
        ]
        return jsonify(Users=users,Args=args), 200