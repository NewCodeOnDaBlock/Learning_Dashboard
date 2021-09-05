from flask import Flask, render_template, session, redirect,request

app = Flask (__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/login', methods=['Post'])
def login():
    session['email'] = request.form['email']    
    session['password'] = request.form['password']
    return redirect('/user')

@app.route('/submit', methods=['Post'])
def createAccount():
    session['full_name'] = request.form['full_name']
    session['email'] = request.form['email']    
    session['confirm_email'] = request.form['confirm_email']
    session['password'] = request.form['password']
    return redirect ('/welcome')


@app.route('/welcome')
def welcome():
    return render_template('/new_user.html', full_name = session['full_name'], email = session['email'], confirm_email = session['confirm_email'], password = session['password'])

@app.route('/user')
def userDash():
    return render_template('/user.html', full_name = session['full_name'], email = session['email'], confirm_email = session['confirm_email'], password = session['password'])


if __name__ == "__main__":
    app.run(debug=True)