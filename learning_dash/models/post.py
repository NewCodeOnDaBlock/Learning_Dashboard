from learning_dash.config.mysqlconnection import connectToMySQL
from learning_dash.models.user import User
from flask import flash

class Post:
    def __init__ (self,data):
        self.id = data ['id']
        self.content = data ['content']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.user_id = data ['user_id']
        self.user = None

    @classmethod
    def submitPostToDb(cls, data): #SUBMITS CONTENT TO DB
        query = " INSERT INTO posts (content, user_id) VALUES (%(content)s, %(user_id)s); "
        results = connectToMySQL('learning_dashboard').query_db(query,data)
        return results


    @classmethod
    def getAllPostsById(cls):
        query = "SELECT * FROM posts JOIN users ON user_id WHERE user_id = users.id "
        results = connectToMySQL('learning_dashboard').query_db(query)

        all_posts = []

        for post in results:
            this_post = cls(post)
            data = {

                'id' : post ['users.id'],
                'first_name' : post['first_name'],
                'last_name' : post ['last_name'],
                'email' : post ['email'],
                'password' : post['password'],
                'created_at' : post['users.created_at'],
                'updated_at' : post ['users.updated_at']
            }
            this_post.user = User (data)
            all_posts.append(this_post)


            query = "SELECT * FROM posts; "
            results = connectToMySQL('learning_dashboard').query_db(query)


        return all_posts

    @staticmethod
    def validatePost(data):
        is_valid = True
        if len(data['content']) < 1:
            flash('Invalid amount of characters, must be 1 or more to post!', 'content')
            is_valid = False
        return is_valid