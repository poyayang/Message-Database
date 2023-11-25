import unittest
from message import message_database


class TestApp(unittest.TestCase):

    def test_message_database(self):

        # As message_database is a template, should create an instance to run the functions
        database = message_database()
        database.save_message(number="07900000000", input="Good night")
        message = database.read_message(number="07900000000")

        # "self" are the functions included in unittest.TestCase
        # assertEqual is only included in the unittest

        self.assertEqual(message, "Good night")

    def test_message_database_read_before_save(self): 
        database=message_database()
        database.read_message(number="07900000000")



if __name__ == "__main__":
    unittest.main()
