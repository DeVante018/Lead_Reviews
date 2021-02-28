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
        return redirect("/login/"+username)
    else:
        return error_response()
    #check if user is in the data base
    #if user exist check they have the correct password


def error_response():
        response = ""
        return response


if __name__ == '__main__':
    app.run(port=8080, debug=True)