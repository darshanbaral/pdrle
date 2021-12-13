import unittest
from parameterized import parameterized
import pandas
import numpy
from pdrle import encode


class TestEncode(unittest.TestCase):
    @parameterized.expand([
        [{"data": pandas.Series(["a", "a", "b", "b", "b", "a", "a", "c"])},
         pandas.DataFrame({"vals": ["a", "b", "a", "c"],
                           "runs": [2, 3, 2, 1]})],
        [{"data": pandas.Series(["a", "a", "b", "b", "b", "a", "a", "c"]),
          "vals_name": "letters",
          "runs_name": "lengths"},
         pandas.DataFrame({"letters": ["a", "b", "a", "c"],
                           "lengths": [2, 3, 2, 1]})],
        [{"data": pandas.Series(["home", "home", "home", "home"])},
         pandas.DataFrame({"vals": ["home"],
                           "runs": [4]})],
        [{"data": pandas.Series(["home", "home", numpy.nan, numpy.nan, numpy.nan, "home", "home"])},
         pandas.DataFrame({"vals": ["home", numpy.nan, "home"],
                           "runs": [2, 3, 2]})],
        [{"data": pandas.Series([1, 1, 1, 1, 1, 1, 1])},
         pandas.DataFrame({"vals": [1],
                           "runs": [7]})],
        [{"data": pandas.Series([2])},
         pandas.DataFrame({"vals": [2],
                           "runs": [1]})],
        [{"data": pandas.Series({"a": 1, "b": 1, "c": numpy.nan, "d": numpy.nan, "e": numpy.nan, "f": 2})},
         pandas.DataFrame({"vals": [1, numpy.nan, 2],
                           "runs": [2, 3, 1]})]
    ])
    def test_encode(self, input_data, expected_output):
        actual_output = encode(**input_data)
        pandas.testing.assert_frame_equal(actual_output, expected_output)
