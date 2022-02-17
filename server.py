
from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)


@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html")

@app.route("/add_user", methods=['POST'])
def addUser():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect("/users")

@app.route("/users")
def allUsers():
    users = User.get_all()

    return render_template("users.html" ,users = users)

if __name__ == "__main__":
    app.run(debug=True)

