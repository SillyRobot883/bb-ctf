// Array of messages to rotate through
const messages = [
    "Hmm... nothing here.",
    "Are you sure you looked everywhere? Keep digging!",
    "Maybe it's hidden in plain sight... or somewhere else?"
];

// Function to rotate messages and update the text color
let index = 0;
function rotateMessages() {
    // Update message
    document.getElementById('message').textContent = messages[index];

    // Change color to a subtle greyish color
    document.getElementById('message').style.color = '#cc4444'; // Softer shade of red

    // Increment the index for the next message
    index = (index + 1) % messages.length; // Loop back to the first message after the last one
}

// Set an interval to rotate the messages every 10 seconds
rotateMessages(); // Show the first message immediately
setInterval(rotateMessages, 10000);


// Could the flag be hidden in here? Maybe not...