# all methods for creating html pages for the specific user

def settings_page() -> str:
    f = open("../templates/settings.html", 'r')
    defalt_img = "../static/images/default_pic.png"
    custom = ""
    #
    # TODO: check database if a profile picture for this user has been uploaded, else set default picture
    #
    for line in f:
        if '{Profile_Image}' in line:
            custom += line.replace('{Profile_Image}', defalt_img)
        else:
            custom += line

    return custom
