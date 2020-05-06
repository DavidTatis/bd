from flask import jsonify
from dao.users import UsersDAO
from handler.dictionary import Dictionary

class UserHandler:

    def getAllUsers(self):
        dao = UsersDAO()
        dic = Dictionary()
        users_list = dao.getAllUsers()
        users = []
        for row in users_list:
            result = dic.build_user_dict(row)
            users.append(result)

        return jsonify(Users=users), 200

    def getAllAdminUsers(self):
        users = [
            {"user_id": 1, "firstName": 'Manuel', "lastName": 'Rodríguez',
             "username": 'ManuelRodriguez', "password": 'pass',
             "email": 'manuel.rodriguez@upr.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Mayagüez', "Zipcode": 10966},
            {"user_id": 2, "firstName": 'Pedro', "lastName": 'Rivera',
             "username": 'PedroRivera', "password": 'pass',
             "email": 'pedro.rivera@upr.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Mayagüez', "Zipcode": 10966},
            {"user_id": 3, "firstName": 'Emmanuel', "lastName": 'Arzuaga',
             "username": 'EmaArzuaga', "password": 'pass',
             "email": 'emmanuel.arzuaga@ece.uprm.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Mayagüez', "Zipcode": 10966},
        ]
        return jsonify(Users=users), 200

    def getAllSupplierUsers(self):
        users = [
            {"user_id": 4, "firstName": 'Ariel', "lastName": 'Silva',
             "username": 'ArielSilva', "password": 'pass',
             "email": 'ariel.silva@upr.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Mayagüez', "Zipcode": 10966},
            {"user_id": 5, "firstName": 'David', "lastName": 'Tatis',
             "username": 'DavidTatis', "password": 'pass',
             "email": 'david.tatis@upr.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Mayagüez', "Zipcode": 10966},
            {"user_id": 6, "firstName": 'Javier', "lastName": 'Hernández',
             "username": 'JavierHernandez', "password": 'baticueva',
             "email": 'javier.hernandez7@upr.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Mayagüez', "Zipcode": 10966},

        ]
        return jsonify(Users=users), 200

    def getAllConsumerUsers(self):
        users = [
            {"user_id": 7, "firstName": 'Pablo', "lastName": 'Escobar',
             "username": 'PabloEscobar', "password": 'baticueva',
             "email": 'pablo.escobar@cali.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Mayagüez', "Zipcode": 10966},
            {"user_id": 8, "firstName": 'Jhon', "lastName": 'Velásquez',
             "username": 'Popeye', "password": 'pablito',
             "email": 'jhon.jairo@cali.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Medellín', "Zipcode": 10966},
            {"user_id": 9, "firstName": 'John', "lastName": 'Arias',
             "username": 'Pinina', "password": 'popeye',
             "email": 'john.jairo@cali.edu', "phone": 7871234567, "dateOfBirth": 843192000000,
             "Address": 'Medellín', "Zipcode": 10966},
        ]
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