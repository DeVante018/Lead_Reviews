# all methods for creating html pages for the specific user
import flask_login


def settings_page(database) -> str:
    do_not_disturb = ""
    cur_usr = flask_login.current_user
    user = cur_usr.username
    data = database.users.find({"username": user})
    for info in data:
        do_not_disturb = info['do_not_disturb']

    f = open("templates/settings.html", 'r')
    defalt_img = "static/images/default_pic.png"
    custom = ""
    #
    # TODO: check database if a profile picture for this user has been uploaded, else set default picture
    #
    for line in f:
        if '{Profile_Image}' in line:
            custom += line.replace('{Profile_Image}', defalt_img)
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

