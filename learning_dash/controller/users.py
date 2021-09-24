from flask import Flask, render_template, redirect, request, session
from learning_dash.models.user import User
from learning_dash import app
from flask import flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def loginRegistrationPage():
    return render_template ('login_registration.html')
    


@app.route('/register', methods=['post'])
def registerUser():

    if not User.validateRegistration(request.form):
        return redirect ('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    pw_hash2 = bcrypt.generate_password_hash(request.form['confirm_password'])  

    data = {

        'first_name' : request.form ['first_name'],
        'last_name' : request.form ['last_name'],
        'email' : request.form ['email'],
        'password' : pw_hash,
        'confirm_password' : pw_hash2
    
    }
    results = User.submitUserToDb(data)
    session['logged_user'] = results
    return redirect('/student/dashboard')



@app.route('/student/login')
def renderLogin():
    return render_template ('login.html')



@app.route('/login', methods = ['post'])
def loginStudent():
    email = request.form['email']
    data = {

        'email' : email
    }
    user = User.getUserByEmail(data)
    if not user:
        flash('Invalid entry Email/Password is incorrect', 'email')
        return redirect ('/student/login')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid entry Email/Password is incorrect', 'password')
        return redirect ('/student/login')

    session['logged_user'] = user.id
    return redirect ('/student/dashboard')



@app.route('/student/dashboard')
def renderStudentDashboard():
    if 'logged_user' in session:
        this_student = User.getUserById({'id' : session ['logged_user']})
        return render_template ('user.html', this_student = this_student)
    else:
        return redirect('/')


@app.route('/student/learn')
def renderLearnSection():
    if 'logged_user' in session:
        data = {'id' : session ['logged_user']}
        this_student = User.getUserById(data)
        return render_template ('learn.html', this_student = this_student)
    else: 
        return redirect ('/')



@app.route('/settings')
def renderSettings():
    if 'logged_user' in session:
        this_student = User.getUserById({'id' : session ['logged_user']})
        return render_template ('settings.html', this_student = this_student)
    else:
        return redirect('/')



@app.route('/update/email/<id>')
def renderEmailUpdate(id):
    if 'logged_user' in session:
        data = {

            'id' :id
        }
        this_student = User.getUserById({'id' : session ['logged_user']})
        return render_template ('update_email.html', this_student = this_student, this_id = User.getUserById(data))
    else:
        return redirect ('/')



@app.route('/update-submit/email/<id>', methods = ['post'])
def updateStudentsEmail(id):
    if not User.validateEmailUpdate(request.form):
        return redirect (f'/update/email/{id}') 

    data = {

        'id' : id,
        'email' : request.form['email']
    }
    User.updateStudentEmail(data)
    return redirect ('/student/email-updated')



@app.route('/update/password/<id>')
def renderPasswordUpdate(id):
    if 'logged_user' in session:
        data = {

            'id' :id
        }
        this_student = User.getUserById({'id' : session ['logged_user']})
        return render_template ('update_password.html', this_student = this_student, this_id = User.getUserById(data))
    else:
        return redirect ('/')



@app.route('/update-submit/password/<id>', methods=['post'])
def updateStudentPassword(id):
    if not User.validatePasswordUpdate(request.form):
        return redirect (f'/update/password/{id}')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    pw_hash2 = bcrypt.generate_password_hash(request.form['password'])

    data = {

        'id' :id,
        'password' : pw_hash,
        'confirm_password': pw_hash2
    }
    User.updateStudentPassword(data)
    return redirect ('/student/password-updated')



@app.route('/student/email-updated')
def thanksForTheEmailUpdate():
    if 'logged_user' in session:
        this_student = User.getUserById({'id' : session ['logged_user']})
        return render_template ('emailupdate_thankyou.html', this_student = this_student)
    else:
        return render_template('/')
        


@app.route('/student/password-updated')
def thanksForThePasswordUpdate():
    if 'logged_user' in session:
        this_student = User.getUserById({'id' : session ['logged_user']})
        return render_template ('passwordupdate_thankyou.html', this_student = this_student)
    else:
        return render_template('/')



@app.route('/logout')
def logOutUser():
    session.clear()
    return redirect('/')