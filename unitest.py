import unittest
from app import save_message, read_message


class TestApp(unittest.TestCase):
    def test_save_message(self):
        save_message(number='+447935462009', output='Good morning!')

    def test_read_message(self):
        save_message(number='+447935462009', output='Good morning!')
        x=read_message(number='+447935462009')
        
        self.assertEquals(x, 'Good morning!')

if __name__ == "__main__":
    unittest.main()

