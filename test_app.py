import unittest
from app import hello_world, welcome_message

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_message(self):
        """Test if the message returned is exactly 'Hello, Git!'"""
        self.assertEqual(hello_world(), "Hello, Git!")
        
    def test_hello_world_type(self):
        """Test if the return type of the hello_world function is a string"""
        self.assertIsInstance(hello_world(), str)

    def test_welcome_message(self):
        """Test the welcome_message function with different names"""
        self.assertEqual(welcome_message("Aarav"), "Welcome to DevOps, Aarav!")
        self.assertEqual(welcome_message("Maya"), "Welcome to DevOps, Maya!")

if __name__ == "__main__":
    unittest.main()
