import unittest
import json  # Add this import
from main import lambda_handler

class TestHelloWorldFunction(unittest.TestCase):

    def test_message_in_event(self):
        # Test case where the event contains the 'message' key
        event = {
            "queryStringParameters": {"message": "Test message"}
        }
        context = None  # Mock context if necessary
        result = lambda_handler(event, context)
        self.assertEqual(result['body'], "Test message")

    def test_no_message_in_event(self):
        # Test case where the event does not contain the 'message' key
        event = {}
        context = None  # Mock context if necessary
        result = lambda_handler(event, context)
        self.assertEqual(result['body'], "Hello World!")

    def test_message_in_body(self):
        # Test case where the event contains 'message' in the body
        event = {
            "body": json.dumps({"message": "Body message"})
        }
        context = None  # Mock context if necessary
        result = lambda_handler(event, context)
        self.assertEqual(result['body'], "Body message")

if __name__ == "__main__":
    unittest.main()
