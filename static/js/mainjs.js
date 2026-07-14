document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('chat-toggle-btn');
    const chatContainer = document.getElementById('chatbot-container');
    const userInput = document.getElementById('user-input');

    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            chatContainer.classList.toggle('active');
            if(chatContainer.classList.contains('active')) {
                userInput.focus();
            }
        });
    }

    if (userInput) {
        userInput.addEventListener('keypress', (event) => {
            if (event.key === "Enter") {
                sendMessage();
            }
        });
    }
});

function sendMessage() {
    var userMessage = document.getElementById("user-input").value;
    if (userMessage.trim() === "") return;
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
    chatDisplay.innerHTML += '<div class="user-message">' + message + '</div>';
    chatDisplay.scrollTop = chatDisplay.scrollHeight;
}

function displayBotMessage(message) {
    var chatDisplay = document.getElementById("chat-display");
    var lines = message.split('\n');
    lines.forEach(line => {
        if(line.trim() !== "") {
            chatDisplay.innerHTML += '<div class="bot-message">' + line + '</div>';
        }
    });
    chatDisplay.scrollTop = chatDisplay.scrollHeight;
}
