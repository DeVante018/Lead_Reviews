import os

import bcrypt
import flask_login
from flask import Flask, redirect, render_template, request
from flask_login import LoginManager, login_required, logout_user, login_user
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename

from src.chat import insert_chat, load_chat
from src.custom_html_pages import set_offline, set_online, settings_page, \
    get_online_users, allowed_file, store_in_db, add_form
from src.make_api_call import Api
# from flask_socketio import SocketIO

app = Flask(__name__, template_folder="templates")
app.secret_key = os.urandom(16)
app.config['SECRET_KEY'] = app.secret_key

# CHANGE localhost TO database - DELETE
app.config['MONGO_URI'] = "mongodb://database/leadreviews" #change to localhost when runnig locally
app.config['UPLOAD_FOLDER'] = 'static/images'
mongo = PyMongo(app)
login_manager = LoginManager()
login_manager.init_app(app)

# socketio = SocketIO(app)


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


login = "login"
login_home = "main"
search = "search"
signup = "signup"
not_found = "notfound"
aco = Api()


@login_manager.user_loader
def load_user(username):
    u = mongo.db.users.find_one({"username": username})
    if not u:
        return None
    return User(username=u["username"])


@app.route("/")
@app.route("/login")
def signin():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/create-account", methods=['POST'])
def create_account():
    username = request.form['usr']

    if "<" in username or ">" in username or "&" in username:
        return render_template("invalidcharacters.html")

    email = request.form['eml']
    password = request.form['pswd']
    check = check_users(username, email)
    # We will do name validity so no duplicate user can exist
    if check == 'email':
        return render_template("signuperror.html")

    # Email will be added to the database later on
    if check == 'username':
        return render_template("signuperror.html")

    # Salt and hash password; store in database
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password.encode(), salt)
    User.data_base.online.insert_one({"username": username, "status": "offline"})
    User.data_base.users.insert_one({"username": username, "password": password, "email": email, "see-profiles-image": True})
    return redirect("/")


@app.route("/login", methods=['POST'])
def user_login():
    usr_login = False
    username = request.form['username']
    username = username.replace("&", "&amp;")
    username = username.replace("<", "&lt;")
    username = username.replace(">", "&gt;")
    password = request.form['password']
    data = User.data_base.users.find({"username": username})
    check = check_users(username, "")
    if check == " ":
        return render_template("loginerror.html")
    for ent in data:
        if bcrypt.checkpw(password.encode(), ent['password']):
            usr_login = True
    if usr_login:
        print("username :", username)
        print("password :", password)
        usr_obj = User(username=username)
        login_user(usr_obj)
        set_online(username, User.data_base)
        return redirect("/login/homepage")
    else:
        # flash("Invalid username or password")
        return redirect('/')
    # check if user is in the data base
    # if user exist check they have the correct password


@app.route('/login/log-out', methods=['POST'])
@login_required
def signout():
    cur_usr = flask_login.current_user
    set_offline(cur_usr.username, User.data_base) # set user to offline in database
    logout_user()
    return redirect("/")


@app.route('/login/settings')
@login_required
def usr_settings():
    return settings_page(User.data_base)


# @app.route("/movies/search")
# @login_required
# def search_page():
#     return render_template(search)


# @app.route("/movies/search/go", methods=['POST'])
# @login_required
# def search_movie():
#     name_of_movie = request.form['movie']
#     print(name_of_movie)
#     call = aco.make_call_to_server(name_of_movie)
#     parse_movie_response(call)
#     return "done"


@app.route("/login/homepage", methods=['GET'])
@app.route("/login/main")
@login_required
def user_home():
    # check database if user is logged in
    cur_usr = flask_login.current_user
    online_users = get_online_users(cur_usr.username, User.data_base)
    new_main = ""
    f = open("templates/main.html")

    for line in f:
        if '{{Username}}' in line:
            for names in online_users:
                #new_main += line.replace("{{Username}}", names)
                new_main += add_form(cur_usr.username, names, User.data_base)
        elif "{{Image_API}}" in line:
            new_main += line .replace("{{Image_API}}", "/static/images/default-movie.jpeg")
        elif "{{Movie_Name}}" in line:
            new_main += line.replace("{{Movie_Name}}", "N/A")
        else:
            if "{{start_movies_loop}}" not in line and "{{end_movies_loop}}" not in line:
                new_main += line

    return new_main


def error_response():
    return render_template(not_found)


# @app.route("/user/like/movie", methods=['POST'])
# @login_required
# def like_movie(movie_id, movie_name, user_name, user_hash):
#     value = 0
#     return "no implementation"


@app.route("/disturb", methods=['POST'])
@login_required
def see_other_profile_images():
    cur_usr = flask_login.current_user
    user = cur_usr.username
    print("Current user :", user)
    data = User.data_base.users.find({"username": user})
    cur_setting = True
    for fields in data:
        cur_setting = fields['see-profiles-image']

    User.data_base.users.update_one(
        {"username": user},
        {
            "$set": {
                "see-profiles-image": not cur_setting}
        }
    )

    return redirect('/login/settings')


@app.route("/enter-chat", methods=['GET', 'POST'])
@login_required
def dm():
    user = request.form["connected-username"]
    page = load_chat(flask_login.current_user.username, user, User.data_base)
    return page


@app.route("/uploadtext", methods=['POST'])
@login_required
def send_message():
    print(request.form)
    cur_usr = flask_login.current_user
    message = request.form['msg']
    message = message.replace("&", "&amp;")
    message = message.replace("<", "&lt;")
    message = message.replace(">", "&gt;")
    send = request.form['send-to']
    send = send.replace("&", "&amp;")
    send = send.replace("<", "&lt;")
    send = send.replace(">", "&gt;")
    insert_chat(cur_usr.username, send, message)
    new_page = load_chat(cur_usr.username, send, User.data_base)
    return new_page


@app.route("/profilepic-upload", methods=['GET', 'POST'])
@login_required
def upload_picture():
    print(request.files)
    if 'upload' not in request.files:
        print("file not found")
        return redirect('/login/settings')
    file = request.files['upload']
    if file.filename == '':
        # flash('No selected file')
        return redirect('login/settings')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        store_in_db(User.data_base, flask_login.current_user.username, filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect("login/settings")


# def parse_movie_response(movie_name):
#     s = json.loads(movie_name)
#     # print(s)
#     movie = s['d'][0]
#     movie_image_info = movie['i']
#     movie_id = movie['id']
#     movie_name = movie['l']
#     movie_rank = movie['rank']
#     movie_stars = movie['s']
#     movie_release_date = movie['y']

#     print("Movie image info: ", movie_image_info)
#     print("movie id: ", movie_id)
#     print("movie name: ", movie_name)
#     print("movie rank: ", movie_rank)
#     print("movie stars: ", movie_stars)
#     print("release date: ", movie_release_date)


def check_users(username, email):
    get_usr = User.data_base.users.find()

    for items in get_usr:
        if 'username' in items:
            if items['username'] == username:
                return "username"
        if 'email' in items:
            if items['email'] == email:
                return "email"
    return " "


if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0")
    # socketio.run(app, port=8000, host="0.0.0.0", debug=True)
