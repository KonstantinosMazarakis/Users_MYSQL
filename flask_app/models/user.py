from flask_app.config.mysqlconnection import connectToMySQL



class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    


# pull the users table from data base
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

# function for adding a new user to the database
    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s ,NOW() , NOW() );"
        return connectToMySQL('users_schema').query_db( query, data )

#function brings 1 specific user from the data base targeted by ID
    @classmethod
    def one_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query,data)
        return User(results[0])

#function edits ALL THE COLUMS from a specific user from the database targeted by ID
    @classmethod
    def edit_user(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query,data)
        return

#function delete a user from users table targeted by ID
    @classmethod
    def delete_user(cls,data):
        query = "DELETE from users where id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query,data)
        return
