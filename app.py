from flask import Flask, render_template, redirect
from flask_mail import Mail, Message
from dotenv import load_dotenv

import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = 'code'

mail_sttings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv("EMAIL"),
    "MAIL_PASSWORD": os.getenv("EMAIL_PASSWORD"),
}


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=9090, debug=True)

