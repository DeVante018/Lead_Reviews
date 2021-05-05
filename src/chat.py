# use the users_chat like a static variable
import flask_login


class Chat:
    users_chat = {}  # map of users -> map of created conversations -> array of messages sent
    # EX: {"DeVante":{"Li":["hi Li", "im good and you?"], "Emily":["Hey!", "im fine"]} "Li"...}


def insert_chat(sender, to, message):
    if sender in Chat.users_chat:
        if to in Chat.users_chat[sender]:
            Chat.users_chat[sender][to].append(sender + ": " + message)
        else:
            Chat.users_chat[sender][to] = [sender + ": " + message]
    elif to in Chat.users_chat:
        if sender in Chat.users_chat[to]:
            Chat.users_chat[to][sender].append(sender + ": " + message)
        else:
            Chat.users_chat[to][sender] = [sender + ": " + message]
    else:
        Chat.users_chat[sender] = {to: [sender + ": " + message]}

    print(Chat.users_chat)


def load_chat(cur_user, user, db):
    page = ""
    f = open('templates/chatbox.html')
    get_user = db.pictures.find({"username": user})
    settings = db.users.find({"username": cur_user})

    profile_img = "/static/images/default_pic.png"
    for s in settings:
        check = s["see-profiles-image"]
        print("YGCKJYFGCKYFCJYFC: ", check)
        if check:
            for info in get_user:
                profile_img = "/static/images/" + info['picture']

    for line in f:
        if '{Person_Profile_Image}' in line:
            page += line.replace('{Person_Profile_Image}', profile_img)
        elif '{{person_name}}' in line:
            page += line.replace('{{person_name}}', user)
        elif '{{comment}}' in line:
            messages = get_messages(flask_login.current_user.username, user)
            for all_messages in messages:
                page += line.replace('{{comment}}', all_messages)
        else:
            if '{{start_loop}}' not in line and '{{end_loop}}' not in line:
                page += line
    return page


def get_messages(sender, reciever):
    print(sender)
    print(reciever)
    messages = []
    if sender in Chat.users_chat:
        if reciever in Chat.users_chat[sender]:
            messages = Chat.users_chat[sender][reciever]
    if reciever in Chat.users_chat:
        if sender in Chat.users_chat[reciever]:
            messages = Chat.users_chat[reciever][sender]
    return messages
