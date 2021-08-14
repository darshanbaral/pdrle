import pandas


def encode(data: pandas.Series) -> pandas.DataFrame:
    """
    Computes the lengths and values of runs of equal values in a vector.
    :param data: pandas Series
    :return: pandas Dataframe with columns 'runs' (length of each run) and 'vals' (corresponding values)
    """
    if not isinstance(data, pandas.Series):
        raise ValueError("Input must be a pandas Series")

    if data.empty:
        raise ValueError("Input data is empty")

    prev_val = data.iloc[0]
    prev_run = 0
    vals = []
    runs = []

    for curr_val in data.to_list():
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
    """
    Reverses encode operation. Returns pandas Series from lengths of run and corresponding values.
    :param vals: values of different runs
    :param runs: lengths of runs corresponding to vals
    :return: pandas Series
    """
    data = vals.repeat(runs)
    data.reset_index(drop=True, inplace=True)
    data.rename(inplace=True)
    return data


def id(data: pandas.Series) -> pandas.Series:
    """
    Generates unique integer id for different runs in a pandas Series
    :param data: input value, a pandas Series
    :return: pandas Series
    """
    rle = encode(data)
    rle_id = rle.index.repeat(rle.runs)
    rle_id = rle_id.to_series().reset_index(drop=True)
    return rle_id

