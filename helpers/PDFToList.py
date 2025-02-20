import pdfplumber
import re

from . import PDFGetNumberedList


def generate(path, outfile):
    with pdfplumber.open(path) as pdf:
        page = pdf.pages[-1]
        lines = page.extract_text_lines()
        bbox = PDFGetNumberedList.get_numbered_list_bbox(lines)

        if not bbox:
            print("No numbered list found")
            return

        with open(f"{outfile}.txt", "w") as file:
            cropped_page = page.within_bbox(bbox)
            lines = cropped_page.extract_text_lines()

            lines = _replace_text(lines, r" Tax.*| Total.*")

            for line in lines:
                file.write(line["text"] + "\n")

            print(f"Wrote file {outfile}.txt")


def _replace_text(lines, regExp):
    # returning our list_items item dictionary with a modified text value, removing Tax and Total and its following
    # text from the line, as it is possible when reading the lines out to build our list of numbered items
    # that we get values from the table as it could end up being on the same line
    # NOTE: THIS WILL PRORABLY NEED MODIFIED ONCE TESTED WITH MULTIPLE WO DOCUMENTS
    return [{**line, "text": re.sub(regExp, "", line["text"])} for line in lines]
