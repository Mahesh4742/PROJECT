function sendMessage() {
    var userMessage = document.getElementById('user-input').value;
    document.getElementById('user-input').value = '';

    var chatDisplay = document.getElementById('chat-display');
    chatDisplay.innerHTML += '<div><strong>You:</strong> ' + userMessage + '</div>';

    // Send the user message to the server
    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'user_message=' + userMessage,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.text();
    })
    .then(data => {
        chatDisplay.innerHTML += '<div><strong>Bot:</strong> ' + data + '</div>';
        chatDisplay.lastElementChild.scrollIntoView({ behavior: 'smooth' });
    })
    .catch(error => {
        console.error('Error:', error);
        chatDisplay.innerHTML += '<div><strong>Bot:</strong> An error occurred. Please try again.</div>';
        chatDisplay.lastElementChild.scrollIntoView({ behavior: 'smooth' });
    });
}