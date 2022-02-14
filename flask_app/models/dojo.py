from flask_app.config.mysqlconnection import connectToMySQL
# imported the connection to mysql database 
from flask_app.models import ninja


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
            print(results)
            all_dojos.append(dojo_object)
        return all_dojos


    @classmethod
    def get_dojo_and_ninjas(cls, data):
        # left join ninjas on dojo_id to parse the data of what ninjas belong to what dojo
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON  dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print(f"RESULTS:{results}")

        dojo = cls(results[0])  # results will be a list of ninjas ???
        
        # parse the ninja data to make instances of ninjas
        
        for row in results:
            ninja_data = {
                "id" : row["ninjas.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["ninjas.updated_at"]
            }

            # this_ninja = ninja.Ninja(ninja_data)

            dojo.ninjas.append(ninja.Ninja(ninja_data))

        return dojo
            
            




