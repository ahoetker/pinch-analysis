import pkg_resources
from jinja2 import FileSystemLoader
from latex.jinja2 import make_env
from latex import build_pdf
from pathlib import Path
from typing import Dict

def generate_report(contents: Dict, filename: Path, outputdir: Path) -> None:
    """
    Generate and save a PDF report of the pinch analysis.

    :param contents: Dictionary containing the filenames of generated tables and figures.
    :param filename: Path to the destination where the report should be saved.
    :param outputdir: Path to the directory where tables and figures should be saved.
    :return: None
    """
    resources = Path(pkg_resources.resource_filename("pinch", "resources"))
    template_file = resources / "report_template.tex"
    env = make_env(loader=FileSystemLoader(str(template_file.parent)))
    tpl = env.get_template(str(template_file.name))
    rendered_latex = tpl.render(contents=contents)

    pdf = build_pdf(rendered_latex, texinputs=[str(outputdir), ""])
    pdf.save_to(str(filename))

