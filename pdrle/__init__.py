import pandas
import numpy


def get_id(data: pandas.Series) -> pandas.Series:
    """
    Generates unique integer id for different runs in a pandas Series
    :param data: input value, a pandas Series
    :return: pandas Series
    """
    assert isinstance(data, pandas.Series), "Input must be a pandas Series"
    assert (not data.empty), "Input is empty"

    arr = data.to_numpy()
    check = numpy.append([False], arr[1:] != arr[:-1])
    if data.isna().any():
        check = check.cumsum()
        check[numpy.where(data.isna())] = -1
        check = numpy.append([False], check[1:] != check[:-1])

    rle_id = pandas.Series(check.cumsum().astype(numpy.int64))
    rle_id.index = data.index
    return rle_id


def encode(data: pandas.Series) -> pandas.DataFrame:
    """
    Computes the lengths and values of runs of equal values in a vector.
    :param data: pandas Series
    :return: pandas Dataframe with columns 'runs' (length of each run) and 'vals' (corresponding values)
    """
    return data.groupby(get_id(data), sort=False).agg(vals="first", runs="size").reset_index(drop=True)


def decode(vals: pandas.Series,
           runs: pandas.Series(dtype=int)) -> pandas.Series:
    """
    Reverses encode operation. Returns pandas Series from lengths of run and corresponding values.
    :param vals: values of different runs
    :param runs: lengths of runs corresponding to vals
    :return: pandas Series
    """
    return vals.repeat(runs).reset_index(drop=True).rename()


def get_sn(data: pandas.Series) -> pandas.Series:
    """
    Generates serial number for different elements of each consecutive runs of values in a pandas Series
    :param data: input value, a pandas Series
    :return: pandas Series
    """
    return data.groupby(get_id(data)).cumcount()
