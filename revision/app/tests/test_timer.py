import unittest
import time
from unittest.mock import patch
from revision.app.timer import timer


class TestTimerDecorator(unittest.TestCase):

    def test_return_value(self):
        @timer
        def add(a, b):
            return a + b

        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_function_name_preserved(self):
        @timer
        def sample():
            pass

        self.assertEqual(sample.__name__, "sample")

    def test_output_format(self):
        @timer
        def sleep_func():
            time.sleep(0.1)

        with patch("builtins.print") as mocked_print:
            sleep_func()

            mocked_print.assert_called_once()
            printed_text = mocked_print.call_args[0][0]

            self.assertIn("sleep_func took", printed_text)
            self.assertIn("seconds", printed_text)


if __name__ == "__main__":
    unittest.main()