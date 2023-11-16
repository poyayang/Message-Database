from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from flask_cors import CORS
from message import save_message, read_message

app = Flask(__name__)
CORS(app)


@app.route("/sms", methods=["Get", "Post"])
def sms():
    phone_number = request.form.get('From', tryp=str)
    # Getting received message content
    receive_body = request.form.get("Body", type=str)
    # Split the body for further use
    message = receive_body.upper().split()

    # To send send the message back to Twilio
    resp = MessagingResponse()
    # If the first word is "SAVE",
    if message[0] == "SAVE":
        # The message will be save from the 6 digits
        save_message(number=phone_number, output=receive_body[5:])
        return resp == 'Message saved'
    # If the first word is "READ",
    elif message[0] == "READ":
        # The message will be read from the storage
        response = read_message(number=phone_number)
        return resp == response
    else:
        print("Something might be wrong, please try again!")


if __name__ == '__main__':
    app.run()
    app.app_context().push()
