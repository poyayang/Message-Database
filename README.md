# save_and_read
This project is aim at letting users simply save message by sending text messages, and call the saved message whenever needed. 

## Steps
In this project, there are few steps with three files, 'app.py', 'message.py', and 'message_test.py'. 

### App.py
The initial file is 'app.py'. This is showing the overall structure of the project. 
1. Make sure that Flask is imported to the main file from flask import Flask, request app=Flask(__name__)
2. Mapping URL to the code
3. The functions to build up the message structure

### message.py
In message.py, it saves the class, which contains 'save_message' and 'read_message'. 
1. 'save_message' is to get the received message from the user and save it to the database
2. 'read_message' is to simply call the saved message from the database based on the corresponded user.

### message_test.py
Unit test for 'message.py'. 



https://github.com/poyayang/save_and_read/assets/136909810/ca58d5ab-cb34-43db-969f-bf722685be17

