from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from message import save_message, read_message

app = Flask(__name__)


@app.route("/sms", methods=["Post"])
def sms():
    phone_number = request.form.get('From', tryp=str)
    receive_body = request.form.get("Body", type=str)
    # Getting received message content
    message = receive_body.upper().split()
    # Split the body for further use

    resp = MessagingResponse()
    # To send send the message back to Twilio
    if message[0] == "SAVE":
        # If the first word is "SAVE",
        save_message(number=phone_number, output=receive_body[5:])
        # The message will be save from the 6 digits
        return resp == 'Message saved'
    elif message[0] == "READ":
        # If the first word is "READ",
        response = read_message(number=phone_number)
        # The message will be read from the storage
        return resp == response
    else:
        print("Something might be wrong, please try again!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    app.app_context().push()
