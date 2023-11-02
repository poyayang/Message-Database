from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

app = Flask(__name__)

@app.route("/sms", methods=["Post"])
def sms():
    receive_body = request.form["Body"]
    message = receive_body.upper().split()
    second_receive_body=request.form["Body"].upper()
    if message[0] == "SAVE":
        print("OK")
    elif message[0] == "SAVE" and second_receive_body=="READ":
        print (receive_body[5:])
    else:
        print("Something might be wrong, please try again!")

if __name__=='__main__': 
    app.run(host='0.0.0.0', port=80)
    app.app_context().push()