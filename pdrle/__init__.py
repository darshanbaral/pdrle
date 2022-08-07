"""
Run length encoding for pandas Series

## Installation

```console
pip install pdrle
```

## Usage

```python
import pdrle
import pandas
import numpy


x = pandas.Series(data=[1, 2, 2, 2, 1, 1, numpy.nan, numpy.nan, 3],
                  index=["a", "a", "b", "c", "d", "d", "e", "f", "g"],
                  name="data")
rle = pdrle.Rle(x)
print(rle.rle)
#    vals  runs
# 0   1.0     1
# 1   2.0     3
# 2   1.0     2
# 3   NaN     2
# 4   3.0     1

df = pandas.concat([x, rle.count, rle.sn, rle.id], axis=1)
print(df)
#    data  rle_count  rle_sn  rle_id
# a   1.0          1       0       0
# a   2.0          3       0       1
# b   2.0          3       1       1
# c   2.0          3       2       1
# d   1.0          2       0       2
# d   1.0          2       1       2
# e   NaN          2       0       3
# f   NaN          2       1       3
# g   3.0          1       0       4
```
"""

from .rle import Rle
