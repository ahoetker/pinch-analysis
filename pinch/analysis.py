import numpy as np
import pandas as pd
from typing import Dict, List
from pathlib import Path
from pinch import ureg, Q_, get_units
from pinch.plots import cold_composite, combined_composite, grand_composite, hot_composite


def classify_streams(df: pd.DataFrame) -> pd.Series:
    """
    Classify each stream in a table as either HOT or COLD.

    :param df: DataFrame containing stream data.
    :return: Series corresponding to each stream.
    """
    temp_diff = df["Supply Temperature"] - df["Target Temperature"]
    cond = ["HOT" if x > 0 else "COLD" for x in temp_diff]
    return pd.Series({"Condition": cond})


def composite_plots(cold_df: pd.DataFrame, hot_df: pd.DataFrame, unit_system: str, outputdir: Path) -> Dict[str, Path]:
    """
    Generate the following plots from the input data:

        - Cold composite
        - Hot composite
        - Combined composite
        - Grand composite

    :param cold_df: DataFrame containing input data for cold streams.
    :param hot_df: DataFrame containing input data for hot streams.
    :param unit_system: Units for physical quantities.
    :param outputdir: Path to output folder for plots to be saved.
    :return: Dictionary of file paths to generated plots.
    """
    cold_temp = np.concatenate([cold_df["Supply Temperature"].values, [cold_df["Target Temperature"][0]]])
    hot_temp = np.concatenate([[hot_df["Target Temperature"][0]], hot_df["Supply Temperature"].values])

    units = get_units(unit_system)
    cold_temp_phys = Q_(cold_temp, units["Supply Temperature"])
    hot_temp_phys = Q_(hot_temp, units["Supply Temperature"])

    cold_comp_file = outputdir / "cold_composite.pdf"
    hot_comp_file = outputdir / "hot_composite.pdf"
    comb_comp_file = outputdir / "combined_composite.pdf"
    grand_comp_file = outputdir / "grand_composite.pdf"

    return {
        "cold composite": cold_comp_file,
        "hot composite": hot_comp_file,
        "combined composite": comb_comp_file,
        "grand composite": grand_comp_file,
    }


def prob_design_table(df: pd.DataFrame, unit_system: str, filename: Path) -> None:
    """
    Generate the problem design table.

    :param df: DataFrame containing input data.
    :param unit_system: Units for physical quantities.
    :param filename: Path to file destination for problem design table.
    :return:
    """
    units = get_units(unit_system)
    supply_label = r"$T_i~({:Lx})$".format(units["Supply Temperature"])
    target_label = r"$T_o~({:Lx})$".format(units["Target Temperature"])
    fcp_label = r"$FC_p~({:Lx})$".format(units["Heat Capacity Flowrate"])
    deltah_label = r"$\Delta H~({:Lx})$".format(units["Heat Flow"])

    pdt = pd.DataFrame(index=df.index)
    pdt[r"\#"] = df["#"]
    pdt[supply_label] = df["Supply Temperature"]
    pdt[target_label] = df["Target Temperature"]
    pdt[fcp_label] = df["Heat Capacity Flowrate"]
    pdt[deltah_label] = df["Heat Flow"]

    pdt.to_latex(str(filename), bold_rows=True, escape=False)


def tables(df: pd.DataFrame, unit_system: str, outputdir: Path) -> Dict[str, Path]:
    """
    Generate tables to be included in the pinch analysis report.

    :param df: DataFrame containing input data.
    :param unit_system: Units for physical quantities.
    :param outputdir: Path to output folder for plots to be saved.
    :return: Dictionary of filenames for generated tables.
    """
    units = get_units(unit_system)
    pd.set_option("precision", 2)

    pdt_file = outputdir / "problem_design_table.tex"

    prob_design_table(df, unit_system, pdt_file)

    return {
        "problem design table": pdt_file
    }


def overall_analysis(df: pd.DataFrame, unit_system: str, outputdir: Path) -> Dict:
    """
    Main function for performing analysis on input data.

    :param df: DataFrame containing input data.
    :param unit_system: Units for physical quantities.
    :param outputdir: Path to output folder for plots to be saved.
    :return: None
    """
    df["Condition"] = classify_streams(df)
    cold_streams = df[df["Condition"] == "COLD"]
    hot_streams = df[df["Condition"] == "HOT"]
    # plot_paths = composite_plots(cold_streams, hot_streams, unit_system, outputdir)

    contents = {
        "tables": tables(df, unit_system, outputdir),
        "plots": composite_plots(cold_streams, hot_streams, unit_system, outputdir)
    }
    return contents
