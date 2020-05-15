from flask import jsonify
from dao.users import UsersDAO
from handler.dictionary import Dictionary
#from flask.ext.bcrypt import generate_password_hash

class UserHandler:
    def getAllUsers(self):
        dao = UsersDAO()
        users = dao.getAllUsers()
        dic=Dictionary()
        result_list=[]
        for row in users:
            result=dic.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list), 200

    def getAllUsersInneed(self):
        dao = UsersDAO()
        users = dao.getAllUsersInneed()
        dic=Dictionary()
        result_list=[]
        for row in users:
            result=dic.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list), 200



    def getAllAdminUsers(self):
        dao = UsersDAO()
        users = dao.getAllAdminUsers()
        dic = Dictionary()
        result_list = []
        for row in users:
            result = dic.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list), 200

    def getAllSupplierUsers(self):
        dao = UsersDAO()
        users = dao.getAllSupplierUsers()
        dic = Dictionary()
        result_list = []
        for row in users:
            result = dic.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list), 200

    def getAllConsumerUsers(self):
        dao = UsersDAO()
        users = dao.getAllConsumerUsers()
        dic = Dictionary()
        result_list = []
        for row in users:
            result = dic.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list), 200

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

    def createUserAdmin(self, form):
        if form :
            firstname = form['firstname']
            lastname = form['lastname']
            username = form['username']
            password = form['password']
            email = form['email']
            phone = form['phone']
            dateofbirth = form['dateofbirth']
            address = form['address']
            zipcode = form['zipcode']
            salary = form['salary']
            dao = UsersDAO()
            uid = dao.insertAdmin(firstname, lastname, username,password,email,phone,dateofbirth,address,zipcode,salary)
            result = {}
            result["uid"] = uid
            return jsonify(User=result), 201
        else:
            return jsonify(Message="Error"), 500
