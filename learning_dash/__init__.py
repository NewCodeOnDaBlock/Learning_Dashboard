from flask import Flask
from flask_socketio import SocketIO

app = Flask (__name__)
app.secret_key ='learningdash123'
socketio = SocketIO (app,cors_allowed_origins = "*")