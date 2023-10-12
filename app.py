from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flask-db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)  # Initialize Flask-RESTful

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

# Create a resource for fetching all users
class UsersResource(Resource):
    def get(self):
        users = User.query.all()
        user_list = []
        for user in users:
            user_list.append({
                'id': user.id,
                'username': user.username,
                'email': user.email
            })
        return {'users': user_list}


api.add_resource(UsersResource, '/users')

if __name__ == '__main__':
    app.run(debug=True)
