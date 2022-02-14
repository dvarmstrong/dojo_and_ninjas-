from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo


class Ninja:
    db_name = "dojos_and_ninjas"

    def __init__(self, data):
        self.id = data['id']
        self.first_name =data['first_name']
        self.last_name =data['last_name']
        self.created_at =data['created_at']
        self.updated_at =data['updated_at']
        

    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, created_at, updated_at, dojo_id) VALUES( %(first_name)s, %(last_name)s, NOW(), NOW(), %(dojo_id)s );"

        return connectToMySQL(cls.db_name).query_db(query,data)