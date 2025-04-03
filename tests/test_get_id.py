import unittest

import numpy
import pandas
from parameterized import parameterized

from pdrle import Rle


class TestGetId(unittest.TestCase):
    @parameterized.expand(
        [
            [
                pandas.Series(["a", "a", "b", "b", "b", "a", "a", "c"]),
                pandas.Series([0, 0, 1, 1, 1, 2, 2, 3]),
            ],
            [
                pandas.Series([(1, 2), (1, 2), (1, 3), (4, 5)]),
                pandas.Series([0, 0, 1, 2]),
            ],
            [
                pandas.Series(
                    [(1, 2), (1, 2), (numpy.nan, numpy.nan), (numpy.nan, numpy.nan)]
                ),
                pandas.Series([0, 0, 1, 1]),
            ],
            [
                pandas.Series([1, 1, 1, 1, 1, 1, 1]),
                pandas.Series([0, 0, 0, 0, 0, 0, 0]),
            ],
            [
                pandas.Series(
                    ["home", "home", numpy.nan, numpy.nan, numpy.nan, "home", "home"]
                ),
                pandas.Series([0, 0, 1, 1, 1, 2, 2]),
            ],
            [pandas.Series([2]), pandas.Series([0])],
            [
                pandas.Series({"a": 1, "b": 2, "c": 3, "d": 3, "e": 3, "f": 1}),
                pandas.Series({"a": 0, "b": 1, "c": 2, "d": 2, "e": 2, "f": 3}),
            ],
            [
                pandas.Series({"a": 1, "b": 1, "c": numpy.nan, "d": 1, "e": 2, "f": 2}),
                pandas.Series({"a": 0, "b": 0, "c": 1, "d": 2, "e": 3, "f": 3}),
            ],
            [
                pandas.Series(
                    {
                        "a": 1,
                        "b": 1,
                        "c": numpy.nan,
                        "d": numpy.nan,
                        "e": numpy.nan,
                        "f": 2,
                    }
                ),
                pandas.Series({"a": 0, "b": 0, "c": 1, "d": 1, "e": 1, "f": 2}),
            ],
        ]
    )
    def test_get_id(self, input_data, expected_output):
        expected_output.name = "rle_id"
        rle = Rle(input_data)
        actual_output = rle.id
        pandas.testing.assert_series_equal(actual_output, expected_output)
