
from learning_dash.config.mysqlconnection import connectToMySQL
from learning_dash.models.user import User


class Request:
    def __init__ (self, data): 
        self.id = data ['id']
        self.user_id = data ['user_id']
        self.friend_id = data ['friend_id']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.user = None

    @classmethod 
    def submitFriendRequestToDb(cls, data): 
        query = """
        INSERT INTO requests (user_id, friend_id) VALUES (%(user_id)s, %(friend_id)s);
        """
        results = connectToMySQL('learning_dashboard').query_db(query,data)
        return results

    @classmethod
    def submitAcceptToDb(cls,data):
        query = " INSERT INTO friends (user_id, friend_id) VALUES (%(user_id)s, %(friend_id)s);"
        results = connectToMySQL('learning_dashboard').query_db(query,data)
        return results

    @classmethod
    def destroyRequest(cls, data):
        query = "DELETE FROM requests WHERE user_id = %(user_id)s AND friend_id = %(friend_id)s;"
    
        results = connectToMySQL('learning_dashboard').query_db(query,data)
        return results

    @classmethod
    def getAllfriendsById(cls, data):  
        #First Query Displays all the requests that was received and accepted by the 'logged_user'..
        #Second Query Displays all the requests that were sent from the 'logged_user' and accepted by the receiver..

        query = """ SELECT * FROM users JOIN friends ON user_id = users.id JOIN 
        users AS other_user ON friend_id = other_user.id WHERE users.id = %(id)s;        
        """
        results = connectToMySQL('learning_dashboard').query_db(query, data)

        friend_list = []

        for friend in results: 

            friend_data = {

                'id' : friend ['other_user.id'],
                'first_name' : friend ['other_user.first_name'],
                'last_name' : friend ['other_user.last_name'],
                'email' : friend ['other_user.email'],
                'password' : friend ['other_user.password'],
                'created_at' : friend ['other_user.created_at'],
                'updated_at' : friend ['other_user.updated_at']
            }
            friend_list.append (User(friend_data)) 

        query = """ SELECT * FROM users JOIN friends ON friend_id = users.id JOIN 
        users AS other_user ON user_id = other_user.id WHERE users.id = %(id)s;        
        """
        results = connectToMySQL('learning_dashboard').query_db(query, data)

        for friend in results: 

            friend_data = {

                'id' : friend ['other_user.id'],
                'first_name' : friend ['other_user.first_name'],
                'last_name' : friend ['other_user.last_name'],
                'email' : friend ['other_user.email'],
                'password' : friend ['other_user.password'],
                'created_at' : friend ['other_user.created_at'],
                'updated_at' : friend ['other_user.updated_at']
            }
            friend_list.append (User(friend_data))

        return friend_list


    @classmethod  #WHERE = filter for the current 'logged_user' 
    def getfriendIdById(cls, data): #Displays all the received friend requests that were accepted by the current 'logged_user'
        query = """ SELECT friend_id FROM friends WHERE user_id = %(id)s;
        """
        results = connectToMySQL('learning_dashboard').query_db(query, data)

        friend_list = []

        for friend in results: 

            friend_list.append (friend ['friend_id']) 

                                    #Displays all the friend requests that were sent by the current 'logged_user' that was accepted 
        query = """ SELECT user_id FROM friends WHERE friend_id = %(id)s; 
        """
        results = connectToMySQL('learning_dashboard').query_db(query, data)

        for friend in results: 
            
            friend_list.append (friend['user_id'])

        return friend_list



    @classmethod
    def displayAllFriendRequestsById(cls, data): #Displays a list of users that have all requested the current logged in user
        query = "SELECT * FROM users JOIN requests ON user_id = users.id JOIN users AS request_user ON friend_id = request_user.id WHERE users.id = %(id)s;"
        results = connectToMySQL('learning_dashboard').query_db(query, data)
        
        all_requests = []

        for request in results:
    
            data = {

                'id' : request ['request_user.id'],
                'first_name' : request ['request_user.first_name'],
                'last_name' : request ['request_user.last_name'],
                'email' : request ['request_user.email'],
                'password' :request ['request_user.password'],
                'created_at' : request ['request_user.created_at'],
                'updated_at' : request ['request_user.updated_at']
            }

            all_requests.append(User(data))
        return all_requests        


    @classmethod 
    def displayFriendRequest(cls): #Displays every single request / not needed .... for this situation
        query = " SELECT * FROM requests";
        results = connectToMySQL('learning_dashboard').query_db(query)
            
        requests = []

        for friend_request in results:
            requests.append ( cls (friend_request) )
        return requests
        

    @classmethod
    def getFriendRequestById(cls,data): #Displays All every single request by user id and friend id/ not needed .... for this situation
        query = "SELECT * FROM requests WHERE id = %(id)s"
        results = connectToMySQL('learning_dashboard').query_db(query, data)
        return results

