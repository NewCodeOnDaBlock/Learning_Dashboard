from learning_dash.controller import users, posts, requests
from learning_dash import app, socketio



if __name__ == "__main__":
    socketio.run(app,debug=True)