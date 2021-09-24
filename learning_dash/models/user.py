from learning_dash.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__ (self,data):
        self.id = data ['id']
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
        self.email = data ['email']
        self.password = data ['password']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod
    def submitUserToDb(cls, data): #SUBMITS USER TO DB
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """
        results = connectToMySQL('learning_dashboard').query_db(query,data)
        return results

    @staticmethod 
    def validateRegistration(data): #VALIDATION CHECK
        is_valid = True
        if len(data ['first_name']) < 2:
            flash('Invalid amount of characters, must be at least 2 or more characters', 'first_name')
            is_valid = False
        if len(data ['last_name']) < 2:
            flash('Invalid amount of characters, must be at least 2 or more characters', 'last_name')
            is_valid = False    
        if not EMAIL_REGEX.match(data['email']):
            flash('Invalid email/ password entry, please try again', 'email')
            is_valid = False
        if len(data ['password']) < 8:
            flash('Invalid email/ password entry, must be at least 8 a more characters', 'password')
            is_valid = False
        if data['confirm_password'] != data['password']:
            flash('Email/ Password does not match, please try again', 'confirm_password')
            is_valid = False

        return is_valid

    @staticmethod
    def validateEmailUpdate(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash('Invalid email entry, please try again', 'email')
            is_valid = False
        return is_valid

    staticmethod
    def validatePasswordUpdate(data):
        is_valid = True
        if len(data ['password']) < 8:
            flash('Invalid email/ password entry, must be at least 8 a more characters', 'password')
            is_valid = False
        return is_valid


    @classmethod
    def getUserByEmail(cls, data): #VALIDATE USERS EXISTENCE IN DB FOR LOGIN
        query = " SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('learning_dashboard').query_db(query, data)

        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def getUserById(cls,data):
        query = " SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('learning_dashboard').query_db(query, data)

        user = cls(results[0])

        return user

    @classmethod
    def updateStudentEmail(cls, data):
        query = "UPDATE users SET email = %(email)s WHERE id = %(id)s;"
        results = connectToMySQL('learning_dashboard').query_db(query, data)
        return "email updated!"

    @classmethod
    def updateStudentPassword(cls, data):
        query = "UPDATE users SET password = %(password)s WHERE id = %(id)s;"
        results = connectToMySQL('learning_dashboard').query_db(query, data)
        return "password updated!"

    @classmethod 
    def displayAllStudents(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('learning_dashboard').query_db(query)

        all_students = []

        for student in results:
            all_students.append( cls(student) )
        return all_students