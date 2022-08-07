import unittest
from parameterized import parameterized
import pandas
import numpy
from pdrle import Rle


class TestGetId(unittest.TestCase):
    @parameterized.expand([
        [pandas.Series(["a", "a", "b", "b", "b", "a", "a", "c"]),
         pandas.Series([2, 2, 3, 3, 3, 2, 2, 1])],
        [pandas.Series([(1, 2), (1, 2), (1, 3), (4, 5)]),
         pandas.Series([2, 2, 1, 1])],
        [pandas.Series([(1, 2), (1, 2), (numpy.nan, numpy.nan), (numpy.nan, numpy.nan)]),
         pandas.Series([2, 2, 2, 2])],
        [pandas.Series([1, 1, 1, 1, 1, 1, 1]),
         pandas.Series([7, 7, 7, 7, 7, 7, 7])],
        [pandas.Series(["home", "home", numpy.nan, numpy.nan, numpy.nan, "home", "home"]),
         pandas.Series([2, 2, 3, 3, 3, 2, 2])],
        [pandas.Series([2]),
         pandas.Series([1])],
        [pandas.Series({"a": 1, "b": 2, "c": 3, "d": 3, "e": 3, "f": 1}),
         pandas.Series({"a": 1, "b": 1, "c": 3, "d": 3, "e": 3, "f": 1})],
        [pandas.Series({"a": 1, "b": 1, "c": numpy.nan, "d": 1, "e": 2, "f": 2}),
         pandas.Series({"a": 2, "b": 2, "c": 1, "d": 1, "e": 2, "f": 2})],
        [pandas.Series({"a": 1, "b": 1, "c": numpy.nan, "d": numpy.nan, "e": numpy.nan, "f": 2}),
         pandas.Series({"a": 2, "b": 2, "c": 3, "d": 3, "e": 3, "f": 1})]
    ])
    def test_get_id(self, input_data, expected_output):
        expected_output.name = "rle_count"
        rle = Rle(input_data)
        actual_output = rle.count
        pandas.testing.assert_series_equal(actual_output, expected_output)
