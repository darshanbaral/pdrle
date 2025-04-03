import unittest

import numpy
import pandas

from pdrle import Rle


class TestEncode(unittest.TestCase):
    def test_encode(
        self,
    ):
        test_data = [
            [
                pandas.Series(["a", "a", "b", "b", "b", "a", "a", "c"]),
                pandas.DataFrame({"vals": ["a", "b", "a", "c"], "runs": [2, 3, 2, 1]}),
            ],
            [
                pandas.Series(["a", "a", "b", "b", "b", "a", "a", "c"]),
                pandas.DataFrame({"vals": ["a", "b", "a", "c"], "runs": [2, 3, 2, 1]}),
            ],
            [
                pandas.Series(["home", "home", "home", "home"]),
                pandas.DataFrame({"vals": ["home"], "runs": [4]}),
            ],
            [
                pandas.Series(
                    ["home", "home", None, None, None, "home", "home"]
                ),
                pandas.DataFrame(
                    {"vals": ["home", None, "home"], "runs": [2, 3, 2]}
                ),
            ],
            [
                pandas.Series([1, 1, 1, 1, 1, 1, 1]),
                pandas.DataFrame({"vals": [1], "runs": [7]}),
            ],
            [pandas.Series([2]), pandas.DataFrame({"vals": [2], "runs": [1]})],
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
                pandas.DataFrame({"vals": [1, numpy.nan, 2], "runs": [2, 3, 1]}),
            ],
        ]
        for input_data, expected_output in test_data:
            with self.subTest(input_data=input_data):
                rle = Rle(input_data)
                actual_output = rle.data
                pandas.testing.assert_frame_equal(actual_output, expected_output)
