message_database={}

def save_message(number: str, output: str):
    # The outcome of "output" will then be saved in the "message_stored"
    message_database[number] = output

def read_message(number:str) -> str:    
    return message_database[number]