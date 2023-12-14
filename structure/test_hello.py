import unittest
import hello as hi


class TestHello(unittest.TestCase):

    def test_format_greeting(self):
        """
        Should format the specific greeting with some general text
        """
        self.assertEqual(hi.format_greeting("From Bob and Alice"),
                         "Hello From Bob and Alice")


if __name__ == '__main__':
    unittest.main()
