import pytest
import pkg_resources
import numpy as np
import pandas as pd
from pathlib import Path
from pinch import ureg, Q_
from pinch.intake import parse_column_units, attach_units, df_with_units

resources = Path(pkg_resources.resource_filename("tests", "resources"))


def test_parse_column_units():
    csv = Path(resources / "input_table.csv")
    xlsx = Path(resources / "input_table.xlsx")
    correct_units = {
        "Supply Temperature": ureg.celsius,
        "Target Temperature": ureg.celsius,
        "Heat Capacity Flowrate": ureg.kW / ureg.K,
        "Enthalpy": ureg.MJ / ureg.hour,
    }
    assert parse_column_units(csv) == correct_units
    assert parse_column_units(xlsx) == correct_units


def test_attach_units():
    column = pd.Series([1, 2, 3, 4, 5])
    correct_series = Q_(np.array([1, 2, 3, 4, 5]), "watt")
    with_units = attach_units(column, ureg["watt"])
    assert np.array_equal(with_units, correct_series)


def test_df_with_units():
    csv = Path(resources / "input_table.csv")
    xlsx = Path(resources / "input_table.xlsx")
    csv_mks = df_with_units(csv, "mks")
    csv_english = df_with_units(csv, "English")
    xlsx_si = df_with_units(xlsx, "SI")
    xlsx_imperial = df_with_units(xlsx, "Imperial")

    assert np.isclose(csv_mks["Supply Temperature"]["Compressor 1 out"], 159.2)
    assert np.isclose(csv_mks["Enthalpy"]["Compressor 1 out"], 41605.3)
    assert np.isclose(xlsx_si["Supply Temperature"]["Compressor 1 out"], 159.2)
    assert np.isclose(xlsx_si["Heat Capacity Flowrate"]["Compressor 1 out"], 101.2)

    assert np.isclose(csv_english["Supply Temperature"]["Compressor 1 out"], 318.56)
    assert np.isclose(xlsx_imperial["Enthalpy"]["Compressor 1 out"], 39434215.63577166)
