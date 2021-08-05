# pyrle

## Installation

```console
pip install git+https://github.com/darshanbaral/pyrle.git
```

## Usage

```python
>>> x = pandas.Series([2, 2, 2, 2, 1, 3, 3])
>>> pyrle.encode(x)
#    vals  runs
# 0     2     4
# 1     1     1
# 2     3     2
```
