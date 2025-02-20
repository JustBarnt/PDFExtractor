__all__ = ["run"]

from .helpers import PDFToTable as pdf_to_table, PDFToList as pdf_to_list
from .enums import Output


def run(path, outfile, output, extension):
    if output == Output.Table:
        _build_table(path, outfile, extension)
    elif output == Output.Text:
        _build_list(path, outfile)


def _build_table(path, outfile, extension):
    pdf_to_table.generate(path, outfile, extension)


def _build_list(path, outfile):
    pdf_to_list.generate(path, outfile)
