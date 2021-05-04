
function noDisturb(){
    alert("You turned on [Do Not Disturb]")
}
// do nothing because using flask socketio
// // taken from hw 4
// // Establish a WebSocket connection with the server
// const socket = new WebSocket('ws://' + window.location.host + '/websocket');

// // Call the addMessage function whenever data is received from the server over the WebSocket
// socket.onmessage = addVote;

// // Allow users to upvote or downvote by pressing like or dislite instead of clicking the Send button
// document.addEventListener("keypress", function (event) {
//    if (event.code === "Like") {
//     //    sendMessage();
//         sendLike();
//    }
//    if (event.code === "Dislike"){
//         sendDislike();
//    }
// });

// // Read the name/comment the user is sending to chat and send it to the server over the WebSocket as a JSON string
// // Called whenever the user clicks the Send button or pressed enter
// // function sendMessage() {
// //    const chatName = document.getElementById("chat-name").value;
// //    const chatBox = document.getElementById("chat-comment");
// //    const comment = chatBox.value;
// //    chatBox.value = "";
// //    chatBox.focus();
// //    if(comment !== "") {
// //        socket.send(JSON.stringify({'username': chatName, 'comment': comment}));
// //    }
// // }

// function sendLike(){
//     socket.send(JSON.stringify({'username': nameofsession, 'voted': liked}))
// }

// function sendDislike(){
//     socket.send(JSON.stringify({'username': nameofsession, 'voted': disliked}))
// }

// // Called when the server sends a new message over the WebSocket and renders that message so the user can read it
// // function addMessage(message) {
// //    const chatMessage = JSON.parse(message.data);
// //    let chat = document.getElementById('chat');
// //    chat.innerHTML += "<b>" + chatMessage['username'] + "</b>: " + chatMessage["comment"] + "<br/>";
// // }

// function addVote(message) {
//     const votesMessage = JSON.parse(message.data);
//     let votes = document.getElementById('votes');
//     votes.innerHTML += "<b>" + chatMessage['username'] + "</b>: " + chatMessage["voted"] + "<br/>";
// }

// // function saveEdits(){
// //     if (confirm("Do you want to save the changes you made?")){
// //         location.replace("settings.html")
// //     }
// // }
// // function deleteAccountAlert(){
// //     if (confirm("You just pressed [Delete Account], are you sure you want to delete this account?")){
// //         alert("Account has been deleted")
// //     }

// // }