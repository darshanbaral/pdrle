import numpy
import pandas

import pdrle

if __name__ == "__main__":
    x = pandas.Series([1, 2, 2, 2, 1, 1, numpy.nan, numpy.nan, 3])
    x.index = ["a", "a", "b", "c", "d", "d", "e", "f", "g"]
    x.name = "data"

    rle = pdrle.Rle(x)
    print(pandas.concat([x, rle.count, rle.sn, rle.id], axis=1))
