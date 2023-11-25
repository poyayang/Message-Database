
class message_database:
    def __init__(self) -> None:
        self.message_dict={}
          
    def save_message(self, number: str, input: str):
        # The outcome of "output" will then be saved in the "message_stored"
        self.message_dict[str(number)] = input

    def read_message(self, number:str) -> str:    
        if number in self.message_dict: 
            return self.message_dict[str(number)]
        else: 
            return "No message available"