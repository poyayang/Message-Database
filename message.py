message_database={}

def save_message(number: str, output: str):
    message_database[number] = output
    # The outcome of "output" will then be saved in the "message_stored"

def read_message(number:str) -> str:
    message_database[number]