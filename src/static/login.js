function tryLogin() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://127.0.0.1:8080/login/try", true);
    xhttp.setRequestHeader("Content-Type", "text");
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            // Response
            var response = this.responseText;
        }
    };

    var userName = document.getElementById('usr').value;
    var passWord = document.getElementById('pswd').value;
    var data = {username: userName, password: passWord};
    xhttp.send()
}