import pdfplumber
import re


def get_numbered_list_bbox(lines):
    # Going through each line item in our lines dictionary, and if it matches our regex we add that line to
    # our list_items
    list_items = [line for line in lines if re.match(r"^\d+\.", line["text"])]

    if not list_items:
        return None

    x0 = min(item["x0"] for item in list_items)
    top = min(item["top"] for item in list_items)
    x1 = max(item["x1"] for item in list_items)
    bottom = max(item["bottom"] for item in list_items)
    return (x0, top, x1, bottom)
