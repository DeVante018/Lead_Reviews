FLASK + FLASK LOGIN REPORT
Flask (THE LIBRARY)

What does this technology (library/framework/service) accomplish for you?
Flask is a web framework that allows the user to create web applications with ease. Flask establishes a TCP connection, handles accepting requests and sending responses to and from the web application, user account management, authorized access to specific application functionality (such as preventing a logged out user from accessing the application home page), and sets secure cookies (see documentation https://flask.palletsprojects.com/en/1.1.x/ ).

How does this technology accomplish what it does?

We used the flask library for our web framework, and we can elaborate on how flask accomplishes what it does in the sections below:

How does flask handle tcp connection:
Flask uses its run function which which uses the werkzeug library’s run_simple function in serving.py which makes the server at this line (source code: https://github.com/pallets/werkzeug/blob/248a79cf9292a4a5e1deec4906a1f5296f151172/src/werkzeug/serving.py#L943) which uses the function from this line (source code: https://github.com/pallets/werkzeug/blob/248a79cf9292a4a5e1deec4906a1f5296f151172/src/werkzeug/serving.py#L758 ), which takes in a WSGIRequestHandler class (source code: https://github.com/pallets/werkzeug/blob/248a79cf9292a4a5e1deec4906a1f5296f151172/src/werkzeug/serving.py#L148 ) that takes in a BaseHTTPRequestHandler, and then return a multithreaded server, multiprocessor server, or a single thread server depending on the amount of threads and processors specified, and then letting it run forever at this line (source code:  https://github.com/pallets/werkzeug/blob/248a79cf9292a4a5e1deec4906a1f5296f151172/src/werkzeug/serving.py#L956 ).

How flask parses its headers:
Flask uses the werkzeug library which uses the BaseHTTPserver which is in the python standard library which uses the _parse_header function located in the feedparser.py file in the email folder, which finally parses the headers (Source code: https://github.com/python/cpython/blob/565a31804c1139fe7886f38af3b3923653b0c1b3/Lib/email/feedparser.py#L471 )

How flask parses form data:
Flask also uses the werkzeug library which uses its parse_multipart_headers function located in the formparser.py file to parse incoming multipart data request (Source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/formparser.py#L338 ), which subsequently uses the _line_parse function (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/formparser.py#L325  ) located in the same file to parse each line of the incoming multipart data request.

How flask route its requests and its paths:
Flask uses the route function located in scaffold.py, which uses the decoration function within it,  to route paths that are received from the http request or redirect(Source code:
https://github.com/pallets/flask/blob/47f0e799db8d8e379a1fd9bf48ce3a8b7d5bfe73/src/flask/scaffold.py#L407 ).
The decoration function will call the add_url_rule (source code: https://github.com/pallets/flask/blob/47f0e799db8d8e379a1fd9bf48ce3a8b7d5bfe73/src/flask/app.py#L1032 ) function, which has been elaborated in the app.py file after its Flask class took in the Scaffold Class where the route function and the original add_url_rule function (source code: https://github.com/pallets/flask/blob/47f0e799db8d8e379a1fd9bf48ce3a8b7d5bfe73/src/flask/scaffold.py#L439 )is located in the scaffold.py file, which will then assign the rule passed into the route function.
Then in the routing.py file of the werkzeug library, the matching function (Source code: https://github.com/pallets/werkzeug/blob/cb0fbec75f2e738c58e116a971656b00b9dec42c/src/werkzeug/routing.py#L883 ) will check if the path it received from the requests matches any of the assigned rules and redirects to the respective url if they match.

How flask sends an HTTP response:
Flask uses the werkzeug library which uses its response class in the response.py file located in the wrappers folder (Source code: https://github.com/pallets/werkzeug/blob/cb0fbec75f2e738c58e116a971656b00b9dec42c/src/werkzeug/wrappers/response.py#L66 ), which takes in the response class located in the response.py located in the sansio folder (source code:https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/sansio/response.py#L58 ), to formulate a HTTP response that is sent over the connection  Then in the serving.py file of the werkzeug library, the send_response function (Source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/serving.py#L376 ) under the WSGIRequestHandler class that takes in the BaseHTTPRequestHandler will send the response by calling the write function located in the same serving.py file (Source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/serving.py#L257 ) which will then send the response.


How flask accepts an HTTP request:
Flask use the werkzeug library which uses its request class in the request.py file  located in the wrappers folder to represent a HTTP request that is sent over the connection (Source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/wrappers/request.py#L28 ) that takes in the request class from the sansio folder’s request.py (Source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/sansio/request.py#L39) . Then, in the request class is the _load_form_data function (Source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/wrappers/request.py#L268 ) which will retrieve the incoming form data from the request (further explanation in the Request section below).
Then in the serving.py file of the werkzeug library, the handle_one_request function (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/serving.py#L368 ) under the WSGIRequestHandler class that takes in the BaseHTTPRequestHandler will read and accept the incoming request. 
    

The feature functions that we used from the library will be elaborated on in the pages below.

What license(s) or terms of service apply to this technology?
Flask uses a BSD 3-Clause license which allows redistribution and use of source code as long as the conditions, found in the flask repo are met: 
https://github.com/pallets/flask/blob/master/LICENSE.rst 
Copyright 2010 Pallets
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1.  Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
2.  Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
3.  Neither the name of the copyright holder nor the names of its
    contributors may be used to endorse or promote products derived from
    this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 
To summarize: it basically means that we can use the code as much as we want to and however we want to as long as we mention the copyright and the license and their conditions, and do not use the library and its source code to promote our project code.

Functionalities of Flask:
Secret Key
What does this technology (library/framework/service) accomplish for you?
The secret key variable stores the string value that is used to encrypt a user’s session cookie to keep their connection secure. (Documentation: https://flask.palletsprojects.com/en/1.1.x/config/ )
How does this technology accomplish what it does? 
    The secret key is a value stored in flask’s app.py  (Source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/app.py#L255 ) which calls the ConfigAttribute class to create the secret key for the session which is located in the config.py file (source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/config.py#L9). Then, the secret key is set via the Config class in the same config.py (source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/config.py#L28) .

Config
What does this technology (library/framework/service) accomplish for you?
    
    The config variable is a way of modifying the configuration for our app. Once the flask app constructor is given arguments, the config variable will be created which is essentially a dictionary. This is where we can set various environments by using key value searches and setting them equal to our desired field
https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/app.py#L422 
   
How does this technology accomplish what it does?  
    The config variable (source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/app.py#L422) is created using the make_config function located in the same app.py file (source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/app.py#L614 ). The make_config function will check if the app’s root path or relative path should be set as the default configuration and then it will take the default config values found in the same app.py file (source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/app.py#L320 ) and turn them into a mutable dict and set the “ENV” value and “DEBUG” value using the get_env function (source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/helpers.py#L27 ) and the get_debug_flag function (source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/helpers.py#L35 ) respectively, and they are both found in the helpers.py file. Then the updated default config dictionary and path will be passed into the Config class found in the config.py file (source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/config.py#L28 ) which will expand the ways the configuration for our app can be modified with the various functions under the Config class. Then the make_config function will return it, thus assigning configuration to the config variable which can then be used to modify the configurations for our app in the way we want. 

Redirect
What does this technology (library/framework/service) accomplish for you?
This Flask function redirects a user to another page from the page they are trying to access or the page they were originally on. Where they are redirected could be the updated version of a page or an error code page (such as Error 404: Page Not Found) (see documentation: https://flask.palletsprojects.com/en/1.1.x/api/#flask.redirect ).
How does this technology accomplish what it does?
    
Flask uses the werkzeug library’s redirect function found in its utils.py (Source code: https://github.com/pallets/werkzeug/blob/248a79cf9292a4a5e1deec4906a1f5296f151172/src/werkzeug/utils.py#L525 ) which ensures that the location string passed into it is safe and not broken using the iri_to_uri function found in the urls.py file (Source link: https://github.com/pallets/werkzeug/blob/248a79cf9292a4a5e1deec4906a1f5296f151172/src/werkzeug/urls.py#L753 ), and then it creates a HTTP response using the Response class found in the response.py file of the wrappers folder (source code: https://github.com/pallets/werkzeug/blob/248a79cf9292a4a5e1deec4906a1f5296f151172/src/werkzeug/wrappers/response.py#L66 ). That response would then be sent using the werkzeug library’s send_response function found in the serving.py file (source code: https://github.com/pallets/werkzeug/blob/cb0fbec75f2e738c58e116a971656b00b9dec42c/src/werkzeug/serving.py#L376) which will then call the write function found in the same file (https://github.com/pallets/werkzeug/blob/cb0fbec75f2e738c58e116a971656b00b9dec42c/src/werkzeug/serving.py#L257 ) that will finally send the response over the connection to redirect the user to the page specified.

Render_Template
What does this technology (library/framework/service) accomplish for you?
This Flask function renders the HTML templates that are stored in the template folder (see documentation https://flask.palletsprojects.com/en/1.1.x/api/#flask.render_template ) .
How does this technology accomplish what it does?

Flask’s render_template function located in the templating.py file  (source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/templating.py#L130 ) loads a template by using the create_jinja_environment function found in app.py (source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/app.py#L675) which in turn uses the Environment class which is located in the environment.py file of the jinja2 library(Source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/app.py#L675) which holds the get_or_select_template function (https://github.com/pallets/jinja/blob/f418f719c14e2509f8a35282334f1d17716c3c48/src/jinja2/environment.py#L931 ) that will proceed to use the _load_template function (source code: https://github.com/pallets/jinja/blob/f418f719c14e2509f8a35282334f1d17716c3c48/src/jinja2/environment.py#L829 ) found in the same file which  will finally load the template. Then the render_template function will pass the loaded template into the _render function located in the templating.py file of the same flask library (Source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/templating.py#L121) which will then use the render function located in the environment.py of the jinja2 library (Source code: https://github.com/pallets/jinja/blob/f418f719c14e2509f8a35282334f1d17716c3c48/src/jinja2/environment.py#L1106) that will finally render the template.


Request (specifically Request.form)
What does this technology (library/framework/service) accomplish for you?
This Flask function is used to access HTML id tags such as: the user entered username (id is “usr”), email (is “eml”), and password (id is “pswd) when creating an account through the signup.html template; the user entered username (id is “username”) and password (id is “password”) when logging into their account through the login.html template; the user uploaded profile image (id is “upload”) through the setting.html template (see documentation https://flask.palletsprojects.com/en/1.1.x/api/#flask.request ).

How does this technology accomplish what it does?
    
    Flask uses the werkzeug library which uses its Request class located in the request.py file in the wrappers folder (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/wrappers/request.py#L28 ) which takes in the request class located in the request.py file in the sansio folder (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/sansio/request.py#L39 ). Then, the form function (source code:https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/wrappers/request.py#L412 )  in the request class located in the request.py file of the wrapper folder calls the _load_form_data function located in the same request class located in the request.py file (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/wrappers/request.py#L268 ) will retrieve the data from the form contained in the incoming request by retrieving the content-type via the content_type function (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/datastructures.py#L2957 ), the content-length via the content_length function (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/datastructures.py#L2962 ), and the mime-type via the mimetype function (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/datastructures.py#L2967 ) which all exist in the datastructure.py file, and also retrieving the input stream via the via the get_input_stream function located in the wsgi.py file (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/wsgi.py#L141 ), and then passing all four of them them into the parse function located in the formparser.py file (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/formparser.py#L228) which will parse the data from the form in the incoming request and make them retrievable.
 

Flask_login (THE LIBRARY)
What does this technology (library/framework/service) accomplish for you?
Flask_login enables user session management such as logging in or logging out, maintaining users sessions, and prevents users’ sessions from being stolen (see documentation https://flask-login.readthedocs.io/en/latest/). 
How does this technology accomplish what it does?
    Flask_login library is essentially an extension of the flask library, so it works the same way the flask library does for parsing, routing, etc.
    
    The Flask_login features/functions are below:
    
What license(s) or terms of service apply to this technology?
Flask_login uses a MIT license which allows redistribution and use of source code as long as the conditions, found here in the repo of the library: 
https://github.com/maxcountryman/flask-login/blob/main/LICENSE 
Copyright (c) 2011 Matthew Frazier
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

    To summarize: we can use this library and its source code however we like in our project as long as we 
mention the copyright and its permission/condition somewhere in our project.


FUNCTIONS AND CLASSES OF FLASK LOGIN BELOW:
LoginManager
What does this technology (library/framework/service) accomplish for you?
LoginManager enables the server to track users and their accounts to allow or deny access to the web application (see documentation here).

How does this technology accomplish what it does?

The Flask-login’s LoginManager class is located in the login_manager.py file (Source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/login_manager.py#L30 ). By passing the app into the init_app function located under the LoginManager class (Source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/login_manager.py#L105 ), the function will update the session dictionary to store cookies via the _update_remember_cookies function located in the same file (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/login_manager.py#L409 ) if the session dictionary has not been already set to store cookies, and if the session dictionary has already been set to store cookies, then it would check if the operation inside the session is set to “set” with a “_user_id” existing in the session, or if the operation inside the session is set to “clear”. If the operation was set to “set” with a userid existing in the session,  then it would set a cookie using the _set_cookie function (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/login_manager.py#L425 )located in the same login_manager.py file that would use the werkzeug library’s set_cookie function located in the response.py file of the sansio folder (source code: https://github.com/pallets/werkzeug/blob/5dc62b8be10e5a52ee8da4f9f9c74658591b9e88/src/werkzeug/sansio/response.py#L191 ) to actually set the cookie in the session.  Otherwise if the operation was set to “clear”, the _update_remember_cookies function will remove a cookie using the _clear_cookie function located in the same file (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/login_manager.py#L464 )  that will use the werkzeug library’s delete_cookie function located in the response.py file of the sansio folder (source code: https://github.com/pallets/werkzeug/blob/5dc62b8be10e5a52ee8da4f9f9c74658591b9e88/src/werkzeug/sansio/response.py#L244 ) to actually remove the cookie from the session. 

Then, the LoginManager will take a user_loader function located in the same login_manager.py  file(source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/login_manager.py#L179 ) that will set the callback for the function we specify in our server.py that will find and retrieve the user whenever a login is attempted and a page is being accessed.

The LoginManager class also sets a session identifier value under its __init__ function (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/login_manager.py#L91 ) which uses the _create_identifier function function found in the utils.py file (source code:https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/utils.py#L369) to generate a session identifier value. The _create_identifier function is a way for the LoginManger to know who is currently logged in. It will retrieve the user-agent of the person who is logging in. It will then check the user agent and utf-8 encode it. At this point the user agent will be formatted and sha512() hashed. This will be returned using the hexdigest.() function and the new hash will  keep track of who is currently logged in. This is how the LoginManager stores who is currently logged in.

This way, the LoginManager enables the server to track users and their account and allow or deny access to the web application.




Login_required
What does this technology (library/framework/service) accomplish for you?
Prevents a user from accessing their settings page, the logout option, the search bar, the toggle profile picture settings option, and the homepage to vote on a movie unless the user is logged in to an account (see documentation: https://flask-login.readthedocs.io/en/latest/#flask_login.login_required ).

How does this technology accomplish what it does?
By adding @login_required right between an app.route() and a function, it will check to make sure if a user is logged in on the browser before it can run the function. If the user is not logged in, then internally it  will call the LoginManager.unauthorized callback and show the client a page stating that whatever they tried to do was unauthorized, preventing them from doing anything they shouldn’t be able to do without logging in.

The login_required function is located in the utils.py file (Source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/utils.py#L234 ) and inside the login_required function is the decorated_view function (Source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/utils.py#L268) which will check if the user is authenticated using the is_authenticated functions located in the mixins.py file which will return true if the user is logged in (Source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/mixins.py#L28 ) or false if the user is not logged in (https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/mixins.py#L64 ). And if it is not true, then the decorated_view function will call the unauthorized function (Source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/login_manager.py#L123 ) that will send them to a page with an unauthorized warning. Otherwise, it will allow the functions with login_required view to pass.


Logout_user
What does this technology (library/framework/service) accomplish for you? (what we used) 
This function will log out the user and erase their session cookies (see documentation: https://flask-login.readthedocs.io/en/latest/#flask_login.logout_user ).
How does this technology accomplish what it does?
The logout_user function located in the utils.py (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/utils.py#L195 )does not require any input parameters. Once it is called, it will pop the user_id, fresh, and id  associated with the user from the session dictionary. Additionally the cookie set to remember the user is logged in will be set to clear (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/utils.py#L214). The original remember cookie is found in flask’s global.py (source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/globals.py#L54) which uses werkzeug’s local.py (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/local.py#L515). Cookies are parsed in werkzeug library’s internal.py’s _cookie_unquote function (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/_internal.py#L415, https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/_internal.py#L457). Cookies are parsed on semicolons which is completed by regex (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/_internal.py#L35).
Next, the user_logged_out signal is sent through flask_login’s signals.py (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/signals.py#L22) which uses the flask library’s FakeSignal class ‘s send function (source code: https://github.com/pallets/flask/blob/master/src/flask/signals.py#L25 )  and the LoginManager is updated to reflect the user has logged out.
Login_user
What does this technology (library/framework/service) accomplish for you?
This function will log in the user and set a cookie to remember them (see documentation: https://flask-login.readthedocs.io/en/latest/#flask_login.login_user ).
How does this technology accomplish what it does?
The login_user function located in the utils.py (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/utils.py#L145 )is passed a user object and updates the session dictionary values user_id, fresh, remember, and duration of how long to remember the user that is logging in. The session dictionary is created in flask’s globals.py (source code: https://github.com/pallets/flask/blob/3c9b85469ef4abda1e996a5ec0e7bef0f1a0b394/src/flask/globals.py#L56) which uses the local value in werkzueg’s local.py (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/local.py#L515). Cookies are parsed in werkzueg’s internal.py in the _cookie_unquote function (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/_internal.py#L415, https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/_internal.py#L457). Cookies are parsed on semicolons which is completed by regex (source code: https://github.com/pallets/werkzeug/blob/4848b99a3863e84b4f1969abfa58864431bdf2d5/src/werkzeug/_internal.py#L35).
Next the LoginManager is updated to recognise the user (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/login_manager.py#L328) and the users cookies that were set (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/login_manager.py#L333), thus reflecting that the user has logged in. 
Source Code (link: https://flask-login.readthedocs.io/en/latest/_modules/flask_login/utils.html#login_user)

Current_user
What does this technology (library/framework/service) accomplish for you?
The current_user variable acts as a proxy for the current user (See documentation: https://flask-login.readthedocs.io/en/latest/#flask_login.current_user).
It is used by us as a way to check who the current user is specifically accessing our web application, so we can properly display the necessary information relevant to them such as their chat text, profile picture, settings toggles, other users online, etc. 
How does this technology accomplish what it does?
This variable (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/utils.py#L26 ) , uses the LocalProxy class in the werkzeug library’s local.py file (source code: https://github.com/pallets/werkzeug/blob/497055804c360ea7e97fc0b48e351f649cf1a794/src/werkzeug/local.py#L462) which is passed the value returned by _get_user function in flask_login’s utils.py file (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/utils.py#L26). The _get_user function loads the user using flask_login’s LoginManager class (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/utils.py#L349), which calls its own _load_user function that gets the user (source code: https://github.com/maxcountryman/flask-login/blob/c77ba6b12ef5e3045df054cf8bf2d61c4d83f54f/flask_login/login_manager.py#L328), thus finally retrieving the current user.