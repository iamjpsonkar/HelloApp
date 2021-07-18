from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template

app=Flask(__name__)

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

@app.route("/greet/user/<uname>")
def greet_user(uname):
   #return redirect(url_for('hello', username=uname))
   return render_template("index.html",title="User Page",user="Jay")


@app.route("/users/")
def display_users():
    users=["Jay", "Faizan", "Praveen"]
    return render_template("users.html",title="Users Page",users=users)

if __name__=='__main__':
    app.run(debug=True)

