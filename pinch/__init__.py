from pint import UnitRegistry

ureg = UnitRegistry()
Q_ = ureg.Quantity
ureg.setup_matplotlib()

mks_units = {
    "Supply Temperature": ureg.degC,
    "Target Temperature": ureg.degC,
    "Heat Capacity Flowrate": ureg.kilowatt / ureg.degK,
    "Enthalpy": ureg.megajoule / ureg.hour,
}

imperial_units = {
    "Supply Temperature": ureg.degF,
    "Target Temperature": ureg.degF,
    "Heat Capacity Flowrate": ureg.btu / ureg.delta_degF / ureg.hour,
    "Enthalpy": ureg.btu / ureg.hour,
}
