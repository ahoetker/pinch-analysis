import click
from pathlib import Path
from pinch.analysis import overall_analysis
from pinch.intake import df_with_units
from pinch.report import generate_report

@click.command()
@click.option("--unitsystem", default="mks", help="Unit system used in tables and graphs.")
@click.option("-a", is_flag=True, help="Save all generated tables and figures to disk.")
@click.argument("datafile", type=click.Path(exists=True))
@click.argument("reportfile", type=click.Path())
@click.argument("outputdir", type=click.Path(), default="output")
def cli(unitsystem, a, datafile, reportfile, outputdir):
    """
    Run script for `pinch-analysis`.
    """

    # Ensure outputfiles dir exists if needed
    Path(outputdir).mkdir(exist_ok=True)

    with_units = df_with_units(Path(datafile), unitsystem)

    contents = overall_analysis(with_units, unitsystem, Path(outputdir))
    generate_report(contents, Path(reportfile), Path(outputdir))