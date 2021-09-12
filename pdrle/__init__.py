import pandas
import numpy


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

    rle_id = get_id(data)
    return pandas.DataFrame({"vals": data.groupby(rle_id).first(), "runs": data.groupby(rle_id).size()})


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


def get_id(data: pandas.Series) -> pandas.Series:
    """
    Generates unique integer id for different runs in a pandas Series
    :param data: input value, a pandas Series
    :return: pandas Series
    """
    check = data != data.shift(1)
    if data.isna().any():
        check = check.cumsum()
        check[data.isna()] = -1
        check = check != check.shift(1)

    rle_id = check.cumsum().astype(numpy.int64)
    return rle_id - 1


def get_sn(data: pandas.Series) -> pandas.Series:
    """
    Generates serial number for different elements of each consecutive runs of values in a pandas Series
    :param data: input value, a pandas Series
    :return: pandas Series
    """
    grp = get_id(data)
    rle_sn = data.groupby(grp).cumcount()
    return rle_sn
