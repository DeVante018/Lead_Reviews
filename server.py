import json
import os
import bcrypt
import flask_login
import src.chat

from flask import Flask, redirect, render_template, request, flash
from flask_login import LoginManager, login_required, logout_user, login_user
from flask_pymongo import PyMongo
from src.make_api_call import Api

app = Flask(__name__, template_folder="templates")
app.secret_key = os.urandom(16)
app.config['SECRET_KEY'] = app.secret_key

# CHANGE localhost TO database - DELETE
app.config['MONGO_URI'] = "mongodb://localhost:27017/leadreviews"

mongo = PyMongo(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User:
    data_base = mongo.db
    username = ""

    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username


login = "login.html"
login_home = "main.html"
search = "search.html"
signup = "signup.html"
not_found = "notfound.html"
aco = Api()


@login_manager.user_loader
def load_user(username):
    u = mongo.db.users.find_one({"username": username})
    if not u:
        return None
    return User(username=u["username"])


@app.route("/")
@app.route("/login.html")
@app.route("/templates/login.html")
def signin():
    return render_template("login.html")


@app.route("/signup.html")
@app.route("/templates/signup.html")
def signup():
    return render_template("signup.html")


@app.route("/create-account", methods=['POST'])
def create_account():
    username = request.form['usr']
    email = request.form['eml']
    password = request.form['pswd']

    # We will do name validity so no duplicate user can exist
    if User.data_base.users.find({"username": username}).count() > 0:
        pass  # display username already exists

    # Email will be added to the database later on
    if User.data_base.users.find({"email": username}).count() > 0:
        # change user name to email ^^^         ^^^
        pass  # display email already has an account associated with it

    # Salt and hash password; store in database
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password.encode(), salt)
    User.data_base.users.insert_one({"username": username, "password": password, "email": email, "do_not_disturb": False})
    return redirect("/")


@app.route("/login", methods=['POST'])
def user_login():
    usr_login = False
    username = request.form['username']
    password = request.form['password']
    data = User.data_base.users.find({"username": username})
    for ent in data:
        if bcrypt.checkpw(password.encode(), ent['password']):
            usr_login = True
    if usr_login:
        print("username :", username)
        print("password :", password)
        usr_obj = User(username=username)
        login_user(usr_obj)
        return redirect("/login/homepage")
    else:
        flash("Invalid username or password")
        return error_response()
    # check if user is in the data base
    # if user exist check they have the correct password


@app.route('/login/log-out', methods=['POST'])
@login_required
def signout():
    logout_user()
    return redirect("/")


@app.route('/login/settings.html')
@login_required
def usr_settings():
    return render_template("settings.html")


@app.route("/movies/search")
@login_required
def search_page():
    return render_template(search)


@app.route("/movies/search/go", methods=['POST'])
@login_required
def search_movie():
    name_of_movie = request.form['movie']
    print(name_of_movie)
    call = aco.make_call_to_server(name_of_movie)
    parse_movie_response(call)
    return "done"


@app.route("/login/homepage", methods=['GET'])
@app.route("/login/main.html")
@login_required
def user_home():
    # check database if user is logged in
    print("just logged in")
    return render_template(login_home)


def error_response():
    return render_template(not_found)


@app.route("/user/like/movie", methods=['POST'])
@login_required
def like_movie(movie_id, movie_name, user_name, user_hash):
    value = 0
    return "no implementation"


@app.route("/disturb", methods=['POST'])
@login_required
def do_not_disturb():
    cur_usr = flask_login.current_user
    user = cur_usr.username
    print("Current user :", user)
    data = User.data_base.users.find({"username": user})
    cur_setting = True
    for fields in data:
        cur_setting = fields['do_not_disturb']

    if cur_setting:
        User.data_base.users.update_one(
            {"username": user},
            {
                "$set": {
                    "do_not_disturb": False}
            }
        )

    else:
        print("Setting was false")
        User.data_base.users.update_one(
            {"username": user},
            {
                "$set": {
                    "do_not_disturb": True}
            }
        )

    return redirect('/login/homepage')


@app.route("/chat", methods=['GET'])
def dm():
    return render_template('chatbox.html')


@app.route("/uploadtext", methods=['POST'])
def send_message():
    print("TEMP")


def parse_movie_response(movie_name):
    s = json.loads(movie_name)
    # print(s)
    movie = s['d'][0]
    movie_image_info = movie['i']
    movie_id = movie['id']
    movie_name = movie['l']
    movie_rank = movie['rank']
    movie_stars = movie['s']
    movie_release_date = movie['y']

    print("Movie image info: ", movie_image_info)
    print("movie id: ", movie_id)
    print("movie name: ", movie_name)
    print("movie rank: ", movie_rank)
    print("movie stars: ", movie_stars)
    print("release date: ", movie_release_date)


if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0", debug=True)
