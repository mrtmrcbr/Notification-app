from flask import Flask, jsonify, request
from flask_cors import CORS
from core.channels.telegram import send_telegram_notification
from core.channels.mail import send_mail_notification

app = Flask(__name__)
CORS(app)

def is_email_valid(mail):
    try:
        #https://github.com/JoshData/python-email-validator/blob/master/LICENSE
        from email_validator import validate_email, EmailNotValidError
        v = validate_email(mail) # validate and get info
        mail = v["email"] # replace with normalized form
        return mail
    except EmailNotValidError as e:
        return False

@app.route('/', methods=['POST'])
def read_data():
    if not request.json or not 'email' in request.json:
        return jsonify({'message': 'E-mail adres needed. Send it with "email" key.'}), 400

    email_adress = request.json['email']
    if not is_email_valid(email_adress):
         return jsonify({
            'message': "Email adres is not valid."
        }), 400

    try:
        # Notification methods
        send_telegram_notification(email_adress)
        send_mail_notification(email_adress)
        pass

    except RuntimeError as error:
        # raise runtime error on any error. give it the information as parameter:str
        return jsonify({
            'message': error.args[0]
        }), 400

    return jsonify({
        'message': 'Succes',
        'email': email_adress
    }), 200
