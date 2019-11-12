from pint import UnitRegistry
from typing import Dict

ureg = UnitRegistry()
Q_ = ureg.Quantity
ureg.setup_matplotlib()

imperial_units = {
    "Supply Temperature": ureg.degF,
    "Target Temperature": ureg.degF,
    "Heat Capacity Flowrate": ureg.btu / ureg.delta_degF / ureg.hour,
    "Heat Flow": ureg.btu / ureg.hour,
}

mks_units = {
    "Supply Temperature": ureg.degC,
    "Target Temperature": ureg.degC,
    "Heat Capacity Flowrate": ureg.kilowatt / ureg.degK,
    "Heat Flow": ureg.megajoule / ureg.hour,
}

def get_units(unit_system: str) -> Dict[str, ureg.Quantity]:
    if unit_system.lower() in ["english", "imperial", "us"]:
        return imperial_units
    elif unit_system.lower() in ["si", "mks", "cgs", "metric"]:
        return mks_units
    else:
        raise KeyError("Invalid unit system: {}".format(unit_system))