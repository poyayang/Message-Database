import unittest
from app import save_message, read_message


class TestApp(unittest.TestCase):
    def test_save_message(self):
        save_message(number='+447935462009', output='Good morning!')

    def test_read_message(self):
        save_message(number='+447935462009', output='Good morning!')
        read_message(number='+447935462009')


if __name__ == "__main__":
    unittest.main()
