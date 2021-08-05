import pandas


def encode(data: pandas.Series) -> pandas.DataFrame:
    if not isinstance(data, pandas.Series):
        raise ValueError("Input must be a pandas Series")

    if data.empty:
        raise ValueError("Input data is empty")

    prev_val = data.iloc[0]
    prev_run = 0
    vals = []
    runs = []

    for _, curr_val in data.iteritems():
        if curr_val == prev_val:
            prev_run += 1
        else:
            vals.append(prev_val)
            runs.append(prev_run)
            prev_val = curr_val
            prev_run = 1

    vals.append(prev_val)
    runs.append(prev_run)

    return pandas.DataFrame({"vals": vals, "runs": runs})


def decode(vals: pandas.Series, runs: pandas.Series(dtype=int)) -> pandas.Series:
    data = vals.repeat(runs)
    data.reset_index(drop=True, inplace=True)
    return data


def id(data: pandas.Series) -> pandas.Series:
    rle = encode(data)
    return rle.index.repeat(rle.runs)

