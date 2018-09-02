"""
Module with specialized dataset subclasses.
The datasets in this module are specialized versions of the general dataset,
since some kinds of data need additional information to processed, viewed or
mapped back properly.
"""
from typing import Callable, List, Tuple, Union

import numpy as np

from .dataset import HighDimentionalDataset


class FLIMDataset(HighDimentionalDataset):
    """
    Custom Data set for FLIM data
    """

    _time_units = {
        "h":   3600,
        "m":     60,
        "s":      1,
        "ms":  1e-3,
        "us":  1e-6,
        "ns":  1e-9,
        "ps":  1e-12,
        "fs":  1e-15,
    }

    def __init__(self, label: str,
                 mapper: Callable[[np.ndarray],
                                  Union[List[tuple],
                                        Tuple[tuple],
                                        np.ndarray]],
                 orig_shape: tuple, time_unit: str="s"):
        """

        Parameters
        ----------
        label: str
            Label of the dataset
        mapper: Callable[[np.ndarray],  Union[List[tuple],
        Tuple[tuple], np.ndarray ]]

        orig_shape: tuple
        """
        super().__init__(label, mapper, orig_shape)
        self._intensity_map = None
        self.mapper = mapper
        self.orig_shape = orig_shape
        self.time_unit = time_unit

    @property
    def time_unit(self) -> str:
        """the time unit [default 's'] """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, value: str):
        if value not in self._time_units:
            raise ValueError(f'Unknown time unit {value}. Supported units are '
                             f'{",".join(self._time_units.keys())}')
        self._time_unit = value

    @property
    def time_axis(self) -> np.ndarray:
        """
        Time axis of the data

        Returns
        -------
        time_axis: np.ndarray

        """
        return self.get_axis("time")

    @time_axis.setter
    def time_axis(self, value: Union[List, Tuple, np.ndarray]):
        self.set_axis("time", value)

    @property
    def pixel_axis(self) -> Union[List[tuple], Tuple[tuple], np.ndarray]:
        """
        Pixel coordinates of the time traces, which were mapped
        from the high dimensional data

        Returns
        -------
        pixel_axis: Union[List[tuple], Tuple[tuple], np.ndarray]
        """
        return self.get_axis("pixel")

    @pixel_axis.setter
    def pixel_axis(self, value: Union[List[tuple], Tuple[tuple], np.ndarray]):
        self.set_axis("pixel", value)

    @property
    def intensity_map(self) -> np.ndarray:
        """
        Intensity map (pixel map with sum over time traces as values)
        of the FLIM data

        Returns
        -------
        intensity_map: np.ndarray
        """
        return self._intensity_map

    @intensity_map.setter
    def intensity_map(self, value: np.ndarray):
        if not isinstance(value, np.ndarray):
            raise TypeError("The intensity_map needs to be a ndarray")
        if len(value.shape) is not 2:
            raise ValueError("The intensity_map needs to be 2-dimensional")
        self._intensity_map = value

    def get_estimated_axis(self):
        """ """
        return self.pixel_axis

    def get_calculated_axis(self):
        """ """
        return self.time_axis
