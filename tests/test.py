import unittest
from parameterized import parameterized
import pandas
import numpy
import pyrle


class TestPyrle(unittest.TestCase):
    # test encode
    @parameterized.expand([
        [pandas.Series(["a", "a", "b", "b", "b", "a", "a", "c"]),
         pandas.DataFrame({"vals": ["a", "b", "a", "c"],
                           "runs": [2, 3, 2, 1]})],
        [pandas.Series(["home", "home", "home", "home"]),
         pandas.DataFrame({"vals": ["home"],
                           "runs": [4]})],
        [pandas.Series([1, 1, 1, 1, 1, 1, 1]),
         pandas.DataFrame({"vals": [1],
                           "runs": [7]})],
        [pandas.Series([2]),
         pandas.DataFrame({"vals": [2],
                           "runs": [1]})],
        [pandas.Series({"a": 1, "b": 1, "c": numpy.nan, "d": numpy.nan, "e": numpy.nan, "f": 2}),
         pandas.DataFrame({"vals": [1, numpy.nan, 2],
                           "runs": [2, 3, 1]})]
    ])
    def test_encode(self, input_data, expected_output):
        actual_output = pyrle.encode(input_data)
        pandas.testing.assert_frame_equal(actual_output, expected_output)

    # test decode
    @parameterized.expand([
        [pandas.Series(["a", "a", "b", "b", "b", "a", "a", "c"]),
         pandas.DataFrame({"vals": ["a", "b", "a", "c"],
                           "runs": [2, 3, 2, 1]})],
        [pandas.Series([1, 1, 1, 1, 1, 1, 1]),
         pandas.DataFrame({"vals": [1],
                           "runs": [7]})],
        [pandas.Series([2]),
         pandas.DataFrame({"vals": [2],
                           "runs": [1]})]
    ])
    def test_decode(self, expected_output, input_data):
        actual_output = pyrle.decode(input_data.vals, input_data.runs)
        pandas.testing.assert_series_equal(actual_output, expected_output)

    # test get_id
    @parameterized.expand([
        [pandas.Series(["a", "a", "b", "b", "b", "a", "a", "c"]),
         pandas.Series([0, 0, 1, 1, 1, 2, 2, 3])],
        [pandas.Series([1, 1, 1, 1, 1, 1, 1]),
         pandas.Series([0, 0, 0, 0, 0, 0, 0])],
        [pandas.Series([2]),
         pandas.Series([0])],
        [pandas.Series({"a": 1, "b": 2, "c": 3, "d": 3, "e": 3, "f": 1}),
         pandas.Series({"a": 0, "b": 1, "c": 2, "d": 2, "e": 2, "f": 3})],
        [pandas.Series({"a": 1, "b": 1, "c": numpy.nan, "d": 1, "e": 2, "f": 2}),
         pandas.Series({"a": 0, "b": 0, "c": 1, "d": 2, "e": 3, "f": 3})],
        [pandas.Series({"a": 1, "b": 1, "c": numpy.nan, "d": numpy.nan, "e": numpy.nan, "f": 2}),
         pandas.Series({"a": 0, "b": 0, "c": 1, "d": 1, "e": 1, "f": 2})]
    ])
    def test_get_id(self, input_data, expected_output):
        actual_output = pyrle.get_id(input_data)
        pandas.testing.assert_series_equal(actual_output, expected_output)
