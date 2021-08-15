# pyrle

## Installation

```console
pip install git+https://github.com/darshanbaral/pyrle.git
```

## Usage

```python
import pyrle
import pandas


x = pandas.Series(["a", "a", "b", "b", "a", "a", "a", "c"])

rle = pyrle.encode(x)
rle
#   vals  runs
# 0    a     2
# 1    b     2
# 2    a     3
# 3    c     1

y = pyrle.decode(rle.vals, rle.runs)
y
# 0    a
# 1    a
# 2    b
# 3    b
# 4    a
# 5    a
# 6    a
# 7    c
# dtype: object

pandas.concat({"x": x, "id": pyrle.get_id(x)}, axis=1)
#    x  id
# 0  a   0
# 1  a   0
# 2  b   1
# 3  b   1
# 4  a   2
# 5  a   2
# 6  a   2
# 7  c   3
```
