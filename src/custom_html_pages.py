# all methods for creating html pages for the specific user
import flask_login

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def settings_page(database) -> str:
    do_not_disturb = ""
    cur_usr = flask_login.current_user
    user = cur_usr.username
    data = database.users.find({"username": user})
    for info in data:
        do_not_disturb = info['do_not_disturb']

    f = open("templates/settings.html", 'r')
    img = "/static/images/default_pic.png"
    custom = ""
    check_profile_image = database.pictures.find({"username": user})
    for x in check_profile_image:
        img = "/static/images/" + x['picture']

    for line in f:
        if '{Profile_Image}' in line:
            custom += line.replace('{Profile_Image}', img)
        elif '{{On_Off_Indicator}}' in line:
            if do_not_disturb:
                custom += line.replace('{{On_Off_Indicator}}', "off")
            else:
                custom += line.replace('{{On_Off_Indicator}}', "on")
        else:
            custom += line

    return custom


def get_online_users(cur_user, database):
    online = database.online.find()
    is_online = []
    for status in online:
        if cur_user != status['username'] and status['status'] == 'online':
            is_online.append(status['username'])
    return is_online


def set_online(username, database):
    database.online.update_one(
        {"username": username},
        {
            "$set": {
                "status": "online"}
        }
    )


def set_offline(username, database):
    database.online.update_one(
        {"username": username},
        {
            "$set": {
                "status": "offline"}
        }
    )


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def store_in_db(db, usr, filename):
    profile = db.pictures.find({"username": usr})
    has_user = False
    for _ in profile:
        has_user = True
    if not has_user:
        db.pictures.insert_one({"username": usr, "picture": filename})
    else:
        print("updating")
    db.pictures.update_one(
        {"username": usr},
        {
            "$set": {
                "picture": filename}
        }
    )
    return
