# pdrle

## Installation

```console
pip install pdrle
```

## Usage

```python
import pdrle
import pandas
import numpy


x = pandas.Series([1, 2, 2, 2, 1, 1, numpy.nan, numpy.nan, 3])
x.index = ["a", "a", "b", "c", "d", "d", "e", "f", "g"]
x.name = "data"

rle = pdrle.Rle(x)
pandas.concat([x, rle.count, rle.sn, rle.id], axis=1)
#    data  rle_count  rle_sn  rle_id
# 0   1.0          1       0       0
# 1   2.0          3       0       1
# 2   2.0          3       1       1
# 3   2.0          3       2       1
# 4   1.0          2       0       2
# 5   1.0          2       1       2
# 6   NaN          2       0       3
# 7   NaN          2       1       3
# 8   3.0          1       0       4
```