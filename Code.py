import nltk
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Download the Punkt tokenizer for tokenization
nltk.download('punkt')

# Chatbot class to handle responses from an Excel file
class CollegeChatBot:
    def __init__(self, excel_file):
        # Read responses from Excel file
        self.responses_df = pd.read_excel(excel_file)
        print(self.responses_df)

    def get_response(self, user_message):
        user_message_tokens = nltk.word_tokenize(user_message.lower())

        for _, row in self.responses_df.iterrows():
            for keyword in row['Keywords'].split(','):
                if keyword.strip() in user_message_tokens:
                    return self.format_response(row['Response'])

        return "I am sorry, but I do not have information on that. Please check our website or contact the college directly."

    def format_response(self, response_text):
        # Add any formatting or structuring logic here
        return response_text

# Provide the path to your Excel file with responses
excel_file_path = "C:\\Users\\Mahesh\\Desktop\\PROJECT ONE\\clg_data.xlsx"

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
