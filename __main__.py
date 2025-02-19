# Import our used packages
import argparse
import os


# Import our relative package PDFExtractor
from . import PDFExtractor
from __enum__ import Output


def main():
    output = Output.Table

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
        raise argparse.ArgumentError(None, "File give was not found.")

    if args.output is None:
        args.output = output
    else:
        if args.output in [Output.value for _ in Output]:
            args.output = Output(args.output)
        else:
            raise argparse.ArgumentError(
                None,
                f"{args.output} is not a valid input. Must be {Output.Table} or {Output.Text}",
            )

    if args.outfile is None:
        args.outfile = os.path.splitext(os.path.basename(args.file))[0]

    if args.extension is None and args.output == Output.Table:
        args.extension = "csv"
    elif args.extension is None and args.output == Output.Text:
        args.extension = "txt"
    else:
        if args.extension in ["csv", "xlsx"] and args.output != Output.Table:
            raise argparse.ArgumentError(
                None,
                f"invalid extension: {args.extension}. when output is {args.output}",
            )
        elif args.extension == "txt" and args.output != Output.Text:
            raise argparse.ArgumentError(
                None,
                f"invalid extension: {args.extension}. when output is {args.output}",
            )

    PDFExtractor.run(args.file, args.outfile, args.output, args.extension)


if __name__ == "__main__":
    main()
