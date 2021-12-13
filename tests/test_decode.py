import unittest
from parameterized import parameterized
import pandas
import numpy
from pdrle import decode


class TestDecode(unittest.TestCase):
    @parameterized.expand([
        [pandas.Series(["a", "a", "b", "b", "b", "a", "a", "c"]),
         pandas.DataFrame({"vals": ["a", "b", "a", "c"],
                           "runs": [2, 3, 2, 1]})],
        [pandas.Series([1, 1, 1, 1, 1, 1, 1]),
         pandas.DataFrame({"vals": [1],
                           "runs": [7]})],
        [pandas.Series([2]),
         pandas.DataFrame({"vals": [2],
                           "runs": [1]})],
        [pandas.Series([2, 3, 3, 3, numpy.nan, numpy.nan, 5, 5]),
         pandas.DataFrame({"vals": [2, 3, numpy.nan, 5],
                           "runs": [1, 3, 2, 2]})],
        [pandas.Series(["a", numpy.nan, numpy.nan, "b"]),
         pandas.DataFrame({"vals": ["a", numpy.nan, "b"],
                           "runs": [1, 2, 1]})]
    ])
    def test_decode(self, expected_output, input_data):
        actual_output = decode(input_data.vals, input_data.runs)
        pandas.testing.assert_series_equal(actual_output, expected_output)
