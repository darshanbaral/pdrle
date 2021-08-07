import pandas


arr = pandas.Series([1, 1, 1, 2, 2, 2, 3, 3])

# 1
for el in arr:
    print(el)

# 2
for _, el in arr.iteritems():
    print(el)

# 3
for el in arr.array:
    print(el)

# 4
for el in arr.values:
    print(el)

# 5
for i in range(len(arr)):
    print(arr.iloc[i])
