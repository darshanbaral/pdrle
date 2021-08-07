# pyrle

## Installation

```console
pip install git+https://github.com/darshanbaral/pyrle.git
```

## Usage

```python
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
# Name: vals, dtype: object

id = pyrle.id(x)
id
# 0    0
# 0    0
# 1    1
# 1    1
# 2    2
# 2    2
# 2    2
# 3    3
# dtype: int64
```
