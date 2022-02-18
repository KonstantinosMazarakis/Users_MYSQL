
from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

# nothing on the page
@app.route("/")
def index():
    return redirect ("/users")

#--------------------------------------------------------

# all users
@app.route("/users")
def users():
    users = User.get_all()
    return render_template("users.html", users = users)

#POST from who deletes users from user page ^
@app.route("/users/delete_post", methods=["POST"])
def delete_user():
    User.delete_user(request.form)
    return redirect("/users")

#--------------------------------------------------------
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
#--------------------------------------------------------

# info for one user specific targeted by id
@app.route("/users/<int:id>")
def user_info(id):
    user = User.one_user({'id': id})
    return render_template("user_info.html", user = user)

#--------------------------------------------------------

# edit a spesific user targeted by id
@app.route("/users/<int:id>/edit")
def edit_user(id):
    user = User.one_user({'id': id})

    return render_template("edit_user.html", user = user)

# POST from edit users ^
@app.route("/users/edit/post", methods=["POST"])
def edit_users_post():
    edit_user = request.form
    User.edit_user(edit_user)
    return redirect ("/users")

#--------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)

