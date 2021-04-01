from flask import Flask, redirect, render_template, request, url_for
from make_api_call import Api
import json


app = Flask(__name__)
login = "login.html"
login_home = "login_home_page.html"
search = "search.html"
aco = Api()


@app.route("/")
def not_signed_in_home_page():
    return render_template(login)


@app.route("/movies/search")
def search_page():
    return render_template(search)


@app.route("/movies/search/go", methods=['POST'])
def search_movie():
    name_of_movie = request.form['movie']
    print(name_of_movie)
    call = aco.make_call_to_server(name_of_movie)
    parse_movie_response(call)
    return "done"


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
    response = "Username or password not found"
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
    app.run(port=8081, debug=True)