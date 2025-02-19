import pdfplumber
import pandas as pd


def generate(path, outfile, extension):
    expanded_rows = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    split_cells = []
                    for cell in row:
                        if cell:
                            lines = cell.split("\n")
                        else:
                            lines = [""]
                        split_cells.append(lines)

                    max_lines = max(len(lines) for lines in split_cells)

                    for i in range(max_lines):
                        new_row = []
                        for lines in split_cells:
                            if len(lines) == 1:
                                new_row.append(lines[0])
                            else:
                                new_row.append(lines[i] if i < len(lines) else "")
                        expanded_rows.append(new_row)

    if expanded_rows:
        df = pd.DataFrame(expanded_rows)
        if extension == "csv":
            df.to_csv(f"{outfile}.csv", index=False)
        elif extension == "xsl":
            df.to_excel(f"{outfile}.xls", index=False)
    else:
        print("No tables found")
