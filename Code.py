import nltk
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Download the Punkt tokenizer for tokenization
nltk.download('punkt')

# Chatbot class to handle responses from an Excel file
class CollegeChatBot:
    def __init__(self, excel_file):
        # Read responses from Excel file, explicitly specifying data types
        self.responses_df = pd.read_excel(excel_file, engine='openpyxl', dtype={'Keywords': str})

    def get_response(self, user_message):
        user_message_tokens = nltk.word_tokenize(user_message.lower())
        for _, row in self.responses_df.iterrows():
            try:
                keywords = str(row['Keywords'])  # Convert to string to handle potential float values
                for keyword in keywords.split(','):
                    if keyword.strip() in user_message_tokens:
                        return self.format_response(row['Description'],row.get('Link'))
            except AttributeError:  # Handle cases where 'Keywords' is not a string
                pass
        return "I'm sorry, I do not have information on that. Please check our website or contact the college directly."

    def format_response(self, response_text, link=None):
        if link:
             return f"{response_text}\nLink: <a href='{link}' target='_blank'>{link}</a>"
        else:
            # Check if the response_text contains bullet points
            if '\n•' in response_text:
                return response_text
            else:
                # Add bullet points
                bullet_points = response_text.split('\n')
                formatted_response = '\n• '.join(bullet_points)
                return f"• {formatted_response}"

# Provide the path to your Excel file with responses
excel_file_path = "clg_data.xlsx"  

# Create a chatbot instance with the Excel file
chatbot = CollegeChatBot(excel_file_path)

@app.route('/')
def home():
    return render_template('MainPG.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    response = chatbot.get_response(user_message)
    return response

if __name__ == '__main__':
    app.run(debug=True)
