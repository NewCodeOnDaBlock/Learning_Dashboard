from flask import Flask, render_template, redirect, request, session
from learning_dash.models.post import Post
from learning_dash.models.user import User
from learning_dash.models.request import Request
from learning_dash import app
from flask import flash


@app.route('/student/social/')
def renderStudentSocial():
    if 'logged_user' in session:
        data = {'id' : session ['logged_user']}
        this_student = User.getUserById(data)
        all_posts = Post.getAllPostsById()
        all_students = User.displayAllStudents()
        all_requests = Request.displayAllFriendRequestsById(data)
        all_friends = Request.getAllfriendsById(data)
        all_friend_ids = Request.getfriendIdById(data)
        return render_template ('social_feed.html', this_student = this_student, all_posts = all_posts, friend_ids = all_friend_ids, all_students = all_students, all_requests = all_requests, this_request = Request.getFriendRequestById(data), friends = all_friends)
    else:
        return redirect('/')



@app.route('/status-update/<id>', methods=['post'])
def submitStatusUpdate(id):
    if not Post.validatePost(request.form):
        return redirect ('/student/social')

    data = {

        'id' : id,
        'content' : request.form ['content'],
        'user_id' : session ['logged_user']

    }
    Post.submitPostToDb(data)
    return redirect ('/student/social')



