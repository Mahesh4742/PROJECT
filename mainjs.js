function sendMessage() {
    var userMessage = document.getElementById("user-input").value;
    if (userMessage.trim() === "") return; // Ignore empty messages
    displayUserMessage(userMessage);
    document.getElementById("user-input").value = "";
    fetch('/get?msg=' + encodeURIComponent(userMessage))
        .then(response => response.text())
        .then(data => displayBotMessage(data))
        .catch(error => console.error('Error:', error));
}

function sendPresetMessage(message) {
    displayUserMessage(message);
    fetch('/get?msg=' + encodeURIComponent(message))
        .then(response => response.text())
        .then(data => displayBotMessage(data))
        .catch(error => console.error('Error:', error));
}

function displayUserMessage(message) {
    var chatDisplay = document.getElementById("chat-display");
    chatDisplay.innerHTML += '<div class="user-message">' + "User: " + message + '</div>';
    chatDisplay.scrollTop = chatDisplay.scrollHeight; // Scroll to bottom
}

function displayBotMessage(message) {
    var chatDisplay = document.getElementById("chat-display");
    var lines = message.split('\n'); // Split response into separate lines
    lines.forEach(line => {
        chatDisplay.innerHTML += '<div class="bot-message">' + "Bot: " + line + '</div>';
    });
    chatDisplay.scrollTop = chatDisplay.scrollHeight; // Scroll to bottom
}

function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

