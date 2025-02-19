import pdfplumber


def generate(path, outfile):
    with pdfplumber.open(path) as pdf:
        with open(f"{outfile}.txt", "w") as file:
            file.write(pdf.pages[0].extract_text(layout=True))
