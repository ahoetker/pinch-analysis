import numpy as np
from matplotlib import pyplot as plt


def cold_composite(enth: np.array, temp: np.array) -> None:
    """Cold composite curve

    :param enth: array of enthalpy values
    :param temp: array of cold temperatures
    :return: None
    """
    pass


def combined_composite(
    enth: np.array,
    temp_cold: np.array,
    temp_hot: np.array,
    dtmin: np.float64,
    pinch_temp: np.float64,
    min_cooling: np.float64,
    min_heating: np.float64,
) -> None:
    """Combined composite curve

    :param enth: array of enthalpy values
    :param temp_cold: array of cold temperatures
    :param temp_hot: array of hot temperatures
    :param dtmin: minimum allowable temperature difference
    :param pinch_temp: temperature at the pinch
    :param min_cooling: minimum allowable cooling heat flux
    :param min_heating: minimum allowable heating heat flux
    :return: None
    """
    pass


def hot_composite(enth: np.array, temp: np.array) -> None:
    """Hot composite curve

    :param enth: array of enthalpy values
    :param temp: array of hot temperatures
    :return: None
    """
    pass


def grand_composite(enth: np.array, temp: np.array) -> None:
    """Grand composite curve

    :param enth: array of enthalpy values
    :param temp: array of temperatures
    :return: None
    """
    pass


def stream_matching() -> None:
    """Steam matching diagram
    I am still unsure how to create this diagram, so this is a pure stub with no parameters.

    :return:
    """
    pass
