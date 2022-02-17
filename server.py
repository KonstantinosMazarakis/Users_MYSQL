from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

# nothing on the page
@app.route("/")
def index():
    return redirect ("/users")


# all users
@app.route("/users")
def users():
    users = User.get_all()
    return render_template("users.html", users = users)

# create a new user
@app.route("/new_user")
def new_user():
    pass
    return render_template ("new_user.html")

#POST form from new user ^
@app.route("/new_user/post", methods=["POST"])
def new_user_post():
    new_user = request.form
    User.add_user(new_user)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)

