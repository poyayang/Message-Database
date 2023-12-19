from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from message import message_database

app = Flask(__name__)


@app.route("/", methods=["Get"])
def health_check():
    return "OK"

database=message_database()

@app.route("/sms", methods=["Post"])
def sms():
    phone_number = request.form.get('From')
    # Getting received message content
    receive_body = request.form.get("Body")
    # Split the body for further use
    message = receive_body.upper().split()

    # To send the message back to Twilio
    resp = MessagingResponse()
    # If the first word is "SAVE",
    if message[0] == "SAVE":
        # The message will be save from the 6 digits
        database.save_message(number=phone_number, input=receive_body[5:])
        resp.message('Message saved')

    # If the first word is "READ",
    elif message[0] == "READ":
        # The message will be read from the storage
        response=database.read_message(number=phone_number)
        resp.message(response)

    else:
        resp.message("Something might be wrong, please try again!")

    return str(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    app.app_context().push()
