# Import our used packages
import argparse
import os

# Import our relative package PDFExtractor
from . import PDFExtractor


def main():
    description = "A simple Python CLI tool to read tables out of a PDF and export them to a spreadsheet"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("file", help="Path to the PDF to export tables out of.")
    parser.add_argument(
        "-o",
        "--outfile",
        help="""
        The path and name (without an extension) to export the tables to
        defaults to the same directory as the file
        """,
    )

    parser.add_argument(
        "--output",
        help="""
        Type of data returned: currently supports 'table' which outputs to an excel or csv file,
        or 'text' which just outputs to a txt file.
        """,
    )

    parser.add_argument(
        "-e",
        "--extension",
        help="""
        Type of spreadsheet (xsl, csv, txt).
        Defaults to '.csv'
        """,
    )

    args = parser.parse_args()

    if os.path.isfile(args.file) is False:
        raise Exception(print(f"{args.file} is not a file."))

    if args.outfile is None:
        args.outfile = os.path.splitext(os.path.basename(args.file))[0]

    if args.output is None:
        args.output = "table"

    if args.extension is None:
        if args.output == "table":
            args.extension = "csv"
        elif args.output == "text":
            args.extensions = "txt"
        else:
            raise argparse.ArgumentError(
                args.output, f"Output type: {args.output} is not supported"
            )

    PDFExtractor.run(args.file, args.outfile, args.output, args.extension)


if __name__ == "__main__":
    main()
