from flask_app.config.mysqlconnection import connectToMySQL
# imported the connection to mysql database 

class Dojos:
    # class attribute for name of database dojos_and_ninjas
    db_name = "dojos_and_ninjas"
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make a connection to the database 
        results = connectToMySQL(cls.db_name).query_db(query)
        # create a list to hold the dojo objects, but why, we need to understand this 
        all_dojos = []
        for row in results:
            # make dojo object using the info from the row in the data table 
            dojo_object =cls(row)
            #append the object to the list all_dojos
            print(all_dojos)
            all_dojos.append(dojo_object)
        return all_dojos

