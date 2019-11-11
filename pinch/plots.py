import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path


def cold_composite(
    enth: np.array, temp: np.array, show: bool = False, filename: Path = None
) -> None:
    """Cold composite curve

    :param enth: array of enthalpy values
    :param temp: array of cold temperatures
    :param show: display the generated plot using `pyplot.show`
    :param filename: file destination to save the figure
    :return: None
    """
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_xlabel(r"Enthalpy (${:L}$)".format(enth.units))
    ax1.set_ylabel(r"Temperature (${:L}$)".format(temp.units))
    ax1.plot(enth, temp, color="tab:blue")

    if filename is not None:
        plt.savefig(str(filename), bbox_inches="tight")

    if show is True:
        plt.show()


def combined_composite(
    enth_cold: np.array,
    enth_hot: np.array,
    temp_cold: np.array,
    temp_hot: np.array,
    show: bool = False,
    filename: Path = None,
) -> None:
    """Combined composite curve

    :param enth_cold: array of enthalpy values corresponding to cold stream temperatures
    :param enth_hot: array of enthalpy values corresponding to hot stream temperatures
    :param temp_cold: array of cold temperatures
    :param temp_hot: array of hot temperatures
    :param show: display the generated plot using `pyplot.show`
    :param filename: file destination to save the figure
    :return: None
    """
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_xlabel("Enthalpy (${:L}$)".format(enth_cold.units))
    ax1.set_ylabel("Temperature (${:L}$)".format(temp_cold.units))
    ax1.plot(enth_cold, temp_cold, color="tab:blue", label="Cold")
    ax1.plot(enth_hot, temp_hot, color="tab:red", label="Hot")
    ax1.legend()

    if filename is not None:
        plt.savefig(str(filename), bbox_inches="tight")

    if show is True:
        plt.show()


def hot_composite(
    enth: np.array, temp: np.array, show: bool = False, filename: Path = None
) -> None:
    """Cold composite curve

    :param enth: array of enthalpy values
    :param temp: array of hot temperatures
    :param show: display the generated plot using `pyplot.show`
    :param filename: file destination to save the figure
    :return: None
    """
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_xlabel(r"Enthalpy (${:L}$)".format(enth.units))
    ax1.set_ylabel(r"Temperature (${:L}$)".format(temp.units))
    ax1.plot(enth, temp, color="tab:red")

    if filename is not None:
        plt.savefig(str(filename), bbox_inches="tight")

    if show is True:
        plt.show()


def grand_composite(
    enth: np.array, temp: np.array, show: bool = False, filename: Path = None
) -> None:
    """Grand composite curve

    :param enth: array of enthalpy values
    :param temp: array of temperatures
    :param show: display the generated plot using `pyplot.show`
    :param filename: file destination to save the figure
    :return: None
    """
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_xlabel(r"Enthalpy (${:L}$)".format(enth.units))
    ax1.set_ylabel(r"Temperature (${:L}$)".format(temp.units))
    ax1.plot(enth, temp, "-k")

    if filename is not None:
        plt.savefig(str(filename), bbox_inches="tight")

    if show is True:
        plt.show()


def stream_matching() -> None:
    """Steam matching diagram
    I am still unsure how to create this diagram, so this is a pure stub with no parameters.

    :return:
    """
    pass
