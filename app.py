from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

app = Flask(__name__)


@app.route("/sms", methods=["Post"])
def sms():
    receive_body = request.form["Body"].upper()
    message = receive_body.split()
    if message[0] == "SAVE":
        print("OK")
    elif message[0] == "READ":
        print(receive_body[5:])
    else:
        print("Something might be wrong, please try again!")
