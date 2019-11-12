import pytest
import numpy as np
from pinch import ureg, Q_
from pinch.plots import (
    cold_composite,
    combined_composite,
    grand_composite,
    hot_composite,
)


def test_cold_composite():
    cold_temp = Q_(np.array([30.30, 106.70, 240.00]), "celsius")
    enth = Q_(np.array([187479.5040, 246613.1040, 453441.3840]), "MJ")
    cold_composite(enth, cold_temp, show=True)


def test_grand_composite():
    temp = Q_(
        np.array([40.30, 45.00, 52.10, 116.70, 159.20, 206.10, 240.00, 250.00]),
        "celsius",
    )
    enth = Q_(
        np.array(
            [
                187479.504,
                191117.304,
                1.640166e5,
                5.627682e4,
                18443.376,
                512.568,
                0,
                15516.0,
            ]
        ),
        "MJ",
    )
    grand_composite(enth, temp, show=True)


def test_combined_composite():
    cold_enth = Q_(np.array([187479.5040, 246613.1040, 453441.3840]), "MJ")
    cold_temp = Q_(np.array([30.30, 106.70, 240.00]), "celsius")
    hot_enth = Q_(np.array([0, 3.259609e4, 294112.728, 384813.576, 437925.384]), "MJ")
    hot_temp = Q_(np.array([45.00, 52.10, 159.20, 206.10, 240.00]), "celsius")
    enth = Q_(np.array([0, 3.259609e4, 294112.728, 384813.576, 437925.384]), "MJ")
    combined_composite(cold_enth, hot_enth, cold_temp, hot_temp, show=True)


def test_hot_composite():
    hot_temp = Q_(np.array([45.00, 52.10, 159.20, 206.10, 240.00]), "celsius")
    enth = Q_(np.array([0, 3.259609e4, 294112.728, 384813.576, 437925.384]), "MJ")
    hot_composite(enth, hot_temp, show=True)
