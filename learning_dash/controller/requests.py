from flask import Flask, render_template, redirect, request, session
from learning_dash.models.request import Request
from learning_dash.models.post import Post
from learning_dash.models.user import User
from learning_dash import app, socketio
from flask_socketio import emit, join_room
from flask import flash




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