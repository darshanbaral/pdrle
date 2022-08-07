import unittest
from parameterized import parameterized
import pandas
import numpy
from pdrle import Rle


class TestGetSn(unittest.TestCase):
    @parameterized.expand([
        [pandas.Series(["a", "a", "b", "b", "b", "a", "a", "c"]),
         pandas.Series([0, 1, 0, 1, 2, 0, 1, 0])],
        [pandas.Series([1, 1, 1, 1, 1, 1, 1]),
         pandas.Series([0, 1, 2, 3, 4, 5, 6])],
        [pandas.Series(["home", "home", numpy.nan, numpy.nan, numpy.nan, "home", "home"]),
         pandas.Series([0, 1, 0, 1, 2, 0, 1])],
        [pandas.Series([2]),
         pandas.Series([0])],
        [pandas.Series({"a": 1, "b": 2, "c": 3, "d": 3, "e": 3, "f": 1}),
         pandas.Series({"a": 0, "b": 0, "c": 0, "d": 1, "e": 2, "f": 0})],
        [pandas.Series({"a": 1, "b": 1, "c": numpy.nan, "d": 1, "e": 2, "f": 2}),
         pandas.Series({"a": 0, "b": 1, "c": 0, "d": 0, "e": 0, "f": 1})],
        [pandas.Series({"a": 1, "b": 1, "c": numpy.nan, "d": numpy.nan, "e": numpy.nan, "f": 2}),
         pandas.Series({"a": 0, "b": 1, "c": 0, "d": 1, "e": 2, "f": 0})]
    ])
    def test_get_sn(self, input_data, expected_output):
        expected_output.name = "rle_sn"
        rle = Rle(input_data)
        actual_output = rle.sn
        pandas.testing.assert_series_equal(actual_output, expected_output)
