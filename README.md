# pinch-analysis
[![Build Status](https://travis-ci.com/ahoetker/pinch-analysis.svg?branch=master)](https://travis-ci.org/ahoetker/matlabreport)

Pinch-point technique for heat integration analysis in chemical plants.

## Getting Started

The package `pinch-analysis` is defined by `setup.py`. To install, clone this repository, and run the following installation
commands:

```
pip install -r requirements.txt
pip install -e .
```

## Usage

In this stage of development, the only target is a run script. 
Run `python main.py`.

### Input Data Format

Data is provided to the program as either a CSV file, or a sheet in an Excel workbook. An example of how the
data must be formatted is given below. The units given in the second row can be written in any way such that [Pint](https://pint.readthedocs.io/en/latest/pint-pandas.html) 
is able to parse them to valid quantities.

| Stream                  | \# | Supply Temperature | Target Temperature | Heat Capacity Flowrate | Enthalpy    |
|-------------------------|----|--------------------|--------------------|------------------------|-------------|
|                         |    | degC               | degC               | kW/K                   | MJ/hour     |
| Compressor 1 out        | 3  | 159\.2             | 45                 | 101\.2                 | 41605\.3    |
| Compressor 2 out        | 5  | 206\.1             | 45                 | 102                    | 59155\.9    |
| Reactor 1 out           | 12 | 240                | 45                 | 219\.5                 | 154089      |
| Reactor 2 out           | 20 | 240                | 45                 | 215\.7                 | 151421\.4   |
| Mixed absorber effluent | 29 | 52\.1              | 45                 | 597                    | 15259\.3    |
| Cold reactor 1 feed     | 10 | 106\.7             | 240                | 216                    | \-103654\.1 |
| Cold reactor 2 feed     | 16 | 30\.3              | 240                | 215                    | \-162307\.8 |

## Testing

Unit tests are provided in the `tests` directory. Running tests requires the `pytest` package. 

## Authors

| Name | Contact | Github | 
| ---  | --- | --- |
| Andrew Hoetker | ahoetker@asu.edu | ahoetker | 
| Emma Holle | eholle@asu.edu | eholle123 | 
| James Taylor | jetayl14@asu.edu | notthesinger | 