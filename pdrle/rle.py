import pandas
import numpy


class Rle:
    def __init__(self, x: pandas.Series):
        assert isinstance(x, pandas.Series), "Input must be a pandas Series"
        assert (not x.empty), "Input is empty"
        self.input = x
        self.__index = x.index
        self.__id = None
        self.__sn = None
        self.__count = None
        self.__rle = None

    @property
    def id(self) -> pandas.Series:
        """
        Series named `rle_id` with unique integer id for different runs
        """
        if self.__id is None:
            arr = self.input.to_numpy()
            check = numpy.append([False], arr[1:] != arr[:-1])
            if self.input.isna().any():
                check = check.cumsum()
                check[numpy.where(self.input.isna())] = -1
                check = numpy.append([False], check[1:] != check[:-1])

            rle_id = pandas.Series(check.cumsum().astype(numpy.int64))
            rle_id.index = self.__index
            rle_id.name = "rle_id"
            self.__id = rle_id

        return self.__id

    @property
    def data(self) -> pandas.DataFrame:
        """
        Dataframe with columns `runs` (length of each run) and `vals` (corresponding values)
        """
        if self.__rle is None:
            self.__rle = self.input.groupby(self.id, sort=False).agg(vals="first", runs="size").reset_index(drop=True)

        return self.__rle

    @property
    def sn(self) -> pandas.Series:
        """
        Series named `rle_sn` with serial number for different elements of each consecutive run
        """
        if self.__sn is None:
            self.__sn = self.input.groupby(self.id).cumcount()
            self.__sn.index = self.__index
            self.__sn.name = "rle_sn"

        return self.__sn

    @property
    def count(self) -> pandas.Series:
        """
        Series named `rle_count` with number of elements in each consecutive run
        """
        if self.__count is None:
            self.__count = self.data.runs.repeat(self.data.runs)
            self.__count.index = self.__index
            self.__count.name = "rle_count"

        return self.__count
