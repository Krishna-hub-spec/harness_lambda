
import unittest
from main import hello_world

class TestHelloWorldFunction(unittest.TestCase):

    def test_message_in_event(self):
        # Test case where the event contains the 'message' key
        event = {"message": "Test message"}
        context = None  # Mock context if necessary
        result = hello_world(event, context)
        self.assertEqual(result, "Test message")

    def test_no_message_in_event(self):
        # Test case where the event does not contain the 'message' key
        event = {}
        context = None  # Mock context if necessary
        result = hello_world(event, context)
        self.assertEqual(result, "Hello World!")

if __name__ == "__main__":
    unittest.main()
