import unittest
from app import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_message(self):
        """Test if the message returned is exactly 'Hello, Git!'"""
        self.assertEqual(hello_world(), "Hello, Git!")
        
    def test_hello_world_type(self):
        """Test if the return type of the hello_world function is a string"""
        self.assertIsInstance(hello_world(), str)

if __name__ == "__main__":
    unittest.main()
