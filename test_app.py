import unittest
from app import say_hello 


class TestApp(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello("AWS"), "Hello, AWS")
        
        
if __name__ == "__main__":
    unittest.main()        