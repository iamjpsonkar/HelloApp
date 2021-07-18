from HelloApp import app, db

from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from .models import User
from .forms import UserForm


@app.route("/")
def hello():
    return render_template("index.html",title="Title page of Hello App",user=None)


def hello1():
    return '''
    <html>
    <head>
    <title>Title page of Hello App</title>
    </head>
    <body>
    <h1>Hello World!!!</h1>
    </body>
    </html>'''

@app.route("/user/<username>/")
def user_msq(username,age=18):
    return '''
    <html>
    <head>
    <title>Title page of Hello App</title>
    </head>
    <body>
    <h1>Hello {} !!!</h1>
    </body>
    </html>'''.format(username) 
 

@app.route("/user/<username>/<int:age>")
def user_msq_age(username,age=18):
    return "<h1>You are Welcome {}, you are {} years old</h1>".format(username,age)



@app.route("/home/")
def demo_redirect():
    return redirect("http://localhost:5000/")

@app.route("/greet/user/<uname>/")
def greet_user(uname):
   #return redirect(url_for('hello', username=uname))
   return render_template("index.html",title="User Page",user=uname)

@app.route("/users/")
def display_users():
    users = User.query.all()
    fullnames = [ user.fname + ' ' + user.lname for user in users ]
    return render_template('users.html', users=fullnames)
@app.route("/users_default/")
def display_users1():
    users=["Jay", "Faizan", "Praveen"]
    return render_template("users.html",title="Users Page",users=users)

@app.route("/adduser/", methods=['GET', 'POST'])
def useradd():
    form=UserForm()
    if request.method=='POST':
        if not form.validate_on_submit():
            return render_template("adduser.html", title="User Input Form", form=form)
        user=User(fname=form.fname.data, lname=form.lname.data, email=form.email.data)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception:
            db.session.rollback()
        return render_template("adduser_confirmation.html",title="Add User Confirmation", username=form.fname.data)
    return render_template("adduser.html", title="User Input Form", form=form)

