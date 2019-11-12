import numpy as np
import pandas as pd
from pathlib import Path
from typing import Callable, Dict, Optional
from . import ureg, Q_, mks_units, imperial_units


def map_input_method(filepath: Path) -> Optional[Callable]:
    """
    Determine which pandas method should be used to create a DataFrame.

    :param filepath: path to data file to be read.
    :return: pandas method suitable for data intake.
    """
    filetypes = {".xls": pd.read_excel, ".xlsx": pd.read_excel, ".csv": pd.read_csv}
    try:
        method = filetypes[filepath.suffix]
        return method
    except KeyError as e:
        print("Invalid file extension for input data: {}".format(filepath.suffix))


def parse_column_units(
    filepath: Path, sheet_name: str = None
) -> Dict[str, ureg.Quantity]:
    """
    Parse units for each column containing physical data in the data file.

    :param filepath: Path to data file to be read.
    :param sheet_name: optional sheet name for multiple-sheet Excel workbooks.
    :return: Dictionary of units for each input column
    """
    method = map_input_method(filepath)
    unit_header = method(str(filepath), nrows=1, header=0)
    given_unit = lambda s: unit_header[s].values[0]
    parsed_units = {}
    required_columns = [
        "Supply Temperature",
        "Target Temperature",
        "Heat Capacity Flowrate",
    ]

    for column in required_columns:
        units = ureg.parse_units(given_unit(column))
        parsed_units[column] = units

    return parsed_units


def attach_units(column: pd.Series, units: ureg.Quantity) -> np.array:
    """
    Attach units to a DataFrame column.

    :param column: DataFrame column or Series to have units attached.
    :param units: pint Quantity to be attached.
    :return: Numpy array wrapped with the correct Quantity.
    """
    a = np.array(column)
    with_units = Q_(a, units)
    return with_units


def df_with_units(
    filepath: Path, unit_system: str, sheet_name: str = None
) -> pd.DataFrame:
    """
    Take in a file containing the product design table, and produce a DataFrame with
    the correct units applied to relevant columns. The output DataFrame will contain only scalars, and is
    not labeled with units. This is because it has already been converted to the output unit system.

    :param filepath: Path to data file to be read.
    :param sheet_name: optional sheet name for multiple-sheet Excel workbooks.
    :return: DataFrame containing table data with units attached
    """
    method = map_input_method(filepath)
    df = method(str(filepath), index_col=0, skiprows=[1])
    parsed_units = parse_column_units(filepath)

    for column in parsed_units:
        parsed_unit = parsed_units[column]
        data_with_given_units = attach_units(df[column], parsed_unit)
        if unit_system.lower() in ["english", "imperial", "us"]:
            data_with_output_units = data_with_given_units.to(imperial_units[column])
        elif unit_system.lower() in ["si", "mks", "cgs", "metric"]:
            data_with_output_units = data_with_given_units.to(mks_units[column])
        else:
            raise KeyError("Invalid unit system: {}".format(unit_system))
        df[column] = data_with_output_units.magnitude

    return df
