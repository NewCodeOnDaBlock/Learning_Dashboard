from flask import Flask, render_template, redirect, request, session
from learning_dash.models.request import Request
from learning_dash.models.post import Post
from learning_dash.models.user import User
from learning_dash.models.request import Request
from learning_dash import app, socketio
from flask_socketio import emit, join_room
from flask import flash

from learning_dash import app, socketio
from flask_socketio import emit, join_room, send
from learning_dash.models.request import Request


clients = {}


@socketio.on('connected')
def connection(connection_data):
    clients[ connection_data ['user_id'] ] = request.sid 
    print(f"HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEYYY {clients}")
    join_room(request.sid)



@socketio.on('sending-request') # Making a custom Event listener 
def sendingFriendRequest(request_data):
    Request.submitFriendRequestToDb({ 'user_id' : request_data['receiver_id'], 'friend_id': session['logged_user']})
    print('submitted to db')
    emit ('request-sent', request_data, room = clients[request_data['receiver_id']]) #how it sends the response back to the client
    print('emit occured')



@socketio.on('accepting-request')
def acceptFriendRequestListener(accept_data):
    Request.submitAcceptToDb({ 'user_id' : accept_data['sender_id'], 'friend_id': session['logged_user']})
    emit ('request-accept', accept_data, room = clients[accept_data['sender_id']])



@socketio.on('denying-request')
def denyFriendRequestListener(deny_data):
    Request.destroyRequest({ 'user_id' : deny_data['sender_id'], 'friend_id': session['logged_user']})
    emit ('request-deny', deny_data, room = clients[deny_data['sender_id']])



# ----------------------------------------------------------------------------------------------------#


@app.route('/send-request/<int:id>')
def sendFriendRequest(id):
    data = {

        'friend_id' : session ['logged_user'],
        'user_id' : id

    }
    Request.submitFriendRequestToDb(data)
    return redirect ('/student/social')



@app.route('/accept-request', methods=['post'])
def acceptDeny():
    data = {

        'friend_id' : request.form ['friend_id'],
        'user_id' : session ['logged_user']

    }
    if 'accept' in request.form:
        Request.submitAcceptToDb(data)
    Request.destroyRequest(data)

    print(request.form)
    return redirect('/student/social')