from flask import Flask, redirect, render_template, request

app = Flask(__name__)
std_home_page = "standard_home_page.html"
login = "login.html"
login_home = "login_home _page.html"


@app.route("/")
def not_signed_in_home_page():
    return render_template(std_home_page)


@app.route("/login")
def user_login():
    return render_template(login)


@app.route("/login/{user}")
def user_home(user):
    return render_template(login_home)


@app.route("/login/try", methods=['POST'])
def parse_request():
    username = request.form['username']
    password = request.form['password']

    usr_exist = False
    valid_password = False

    print(username, password)

    if usr_exist and valid_password:
        return redirect("/login/" + username)
    else:
        return error_response()
    # check if user is in the data base
    # if user exist check they have the correct password


def error_response():
    response = ""
    return response


@app.route("/user/like/movie", methods=['POST'])
def like_movie(movie_id, movie_name, user_name, user_hash):
    value = 0
    check_hash = check_user_hash(user_name, user_hash)
    # make sql request to database
    if check_hash == 1:
        kjbi = 0
        # do more stuff
    else:
        iguv = 0
        # return current number in database


def check_user_hash(username, hash):
    # make call to database
    # username would be used to search name in database
    database_result = "find_user_hash(username)" # this would be the function call
    if hash == database_result:
        return 1
    else:
        return 0


if __name__ == '__main__':
    app.run(port=8080, debug=True)
