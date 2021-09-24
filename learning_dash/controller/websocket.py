from learning_dash import app, socketio
from flask_socketio import emit, join_room
from learning_dash.models.request import Request


clients = {}

@socketio.on('connected')
def connection(connection_data):
    clients[ connection_data ['user_id'] ] = request.sid 
    join_room(request.sid)


@socketio.on('sending-request') # Making a custom Event listener 
def sendingFriendRequest(request_data):
    Request.submitFriendRequestToDb({ 'user_id' : session['logged_user'], 'friend_id': request_data['receiver_id']})
    emit ('request-sent', request_data, room = clients[request_data['receiver_id']]) #how it sends the response back to the client


@socketio.on('accepting-request')
def acceptFriendRequestListener(accept_data):
    Request.submitAcceptToDb({ 'user_id' : session['logged_user'], 'friend_id': accept_data['sender_id']})
    emit ('request-accept', accept_data, room = clients[accept_data['sender_id']])



@socketio.on('denying-request')
def denyFriendRequestListener(deny_data):
    Request.destroyRequest({ 'user_id' : session['logged_user'], 'friend_id': deny_data['sender_id']})
    emit ('request-accept', deny_data, room = clients[deny_data['sender_id']])