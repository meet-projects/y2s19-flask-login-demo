from database import *
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
current_user = None

@app.route('/')
def home():
    global current_user
    if current_user != None:
        return render_template('logged.html',name = current_user.username)
    return render_template('home.html')
    

@app.route('/login', methods=['POST'])
def login():
    global current_user
    user = get_user(request.form['username'])
    if user != None and user.password == request.form["password"]:
        current_user = user
        return render_template('logged.html',name = current_user.username)
    else:
        return home()


@app.route('/signup', methods=['POST'])
def signup():
    #check that username isn't taken
    user = get_user(request.form['username'])
    if user == None:
        create_user(request.form['username'],request.form['password'])
    return home()


@app.route('/logout')
def logout():
    global current_user
    curent_user = None
    return home()


if __name__ == '__main__':
    app.run(debug=True)
