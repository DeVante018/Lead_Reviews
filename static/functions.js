
function noDisturb(){
    alert("You turned on [Do Not Disturb]")
}

function saveEdits(){
    if (confirm("Do you want to save the changes you made?")){
        location.replace("settings.html")
    }
}
function deleteAccountAlert(){
    if (confirm("You just pressed [Delete Account], are you sure you want to delete this account?")){
        alert("Account has been deleted")
    }

}