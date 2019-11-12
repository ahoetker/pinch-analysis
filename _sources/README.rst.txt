pinch-analysis
==============

Pinch-point technique for heat integration analysis in chemical plants.

Getting Started
---------------

No package is provided. No docker image is provided. Simply clone
https://github.com/ahoetker/pinch-analysis.git, and run
``pip install -r requirements.txt`` to create the Python environment.

Usage
-----

In this stage of development, the only target is a run script. Run
``python main.py``.

Input Data Format
~~~~~~~~~~~~~~~~~

Data is provided to the program as either a CSV file, or a sheet in an
Excel workbook. An example of how the data must be formatted is given
below. The units given in the second row can be written in any way such
that `Pint <https://pint.readthedocs.io/en/latest/pint-pandas.html>`__
is able to parse them to valid quantities.

+---------------+---+------------+------------+---------------+-------+
| Stream        | # | Supply     | Target     | Heat Capacity | Entha |
|               |   | Temperatur | Temperatur | Flowrate      | lpy   |
|               |   | e          | e          |               |       |
+===============+===+============+============+===============+=======+
|               |   | degC       | degC       | kW/K          | MJ/ho |
|               |   |            |            |               | ur    |
+---------------+---+------------+------------+---------------+-------+
| Compressor 1  | 3 | 159.2      | 45         | 101.2         | 41605 |
| out           |   |            |            |               | .3    |
+---------------+---+------------+------------+---------------+-------+
| Compressor 2  | 5 | 206.1      | 45         | 102           | 59155 |
| out           |   |            |            |               | .9    |
+---------------+---+------------+------------+---------------+-------+
| Reactor 1 out | 1 | 240        | 45         | 219.5         | 15408 |
|               | 2 |            |            |               | 9     |
+---------------+---+------------+------------+---------------+-------+
| Reactor 2 out | 2 | 240        | 45         | 215.7         | 15142 |
|               | 0 |            |            |               | 1.4   |
+---------------+---+------------+------------+---------------+-------+
| Mixed         | 2 | 52.1       | 45         | 597           | 15259 |
| absorber      | 9 |            |            |               | .3    |
| effluent      |   |            |            |               |       |
+---------------+---+------------+------------+---------------+-------+
| Cold reactor  | 1 | 106.7      | 240        | 216           | -1036 |
| 1 feed        | 0 |            |            |               | 54.1  |
+---------------+---+------------+------------+---------------+-------+
| Cold reactor  | 1 | 30.3       | 240        | 215           | -1623 |
| 2 feed        | 6 |            |            |               | 07.8  |
+---------------+---+------------+------------+---------------+-------+

Testing
-------

Unit tests are provided in the ``tests`` directory. Running tests
requires the ``pytest`` package.

Authors
-------

============== ================ ============
Name           Contact          Github
============== ================ ============
Andrew Hoetker ahoetker@asu.edu ahoetker
Emma Holle     eholle@asu.edu   eholle123
James Taylor   jetayl14@asu.edu notthesinger
============== ================ ============
