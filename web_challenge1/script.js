
const messages = [
    "Hmm... nothing here.",
    "Are you sure you looked everywhere? Keep digging!",
    "Maybe it's hidden in plain sight... or somewhere else?"
];

let index = 0;
function rotateMessages() {
    document.getElementById('message').textContent = messages[index];
    document.getElementById('message').style.color = '#cc4444';
    index = (index + 1) % messages.length;
}

rotateMessages();
setInterval(rotateMessages, 10000);


// Could the flag be hidden in here? Maybe not...