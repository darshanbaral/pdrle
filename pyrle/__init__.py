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

    for curr_val in data:
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
