from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

app = Flask(__name__)




@app.route("/sms", methods=["Post"])
def sms():
    receive_body = request.form["Body"]
    message = receive_body.upper().split()

    if message[0] == "SAVE":
        save_message(output=receive_body[5:])
        return 'Message saved'
    elif message[0] == "READ":
        response = read_message()
        return response
    else:
        print("Something might be wrong, please try again!")


message_stored=""

def save_message(output: str):

    global message_stored 
    message_stored = output

def read_message() -> str:

    global message_stored 
    return message_stored

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    app.app_context().push()
