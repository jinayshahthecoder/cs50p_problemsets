# Problem Set 8 Question 3
# To add user's name and a png of a shirt to a program created pdf file

# Importing FPDF to be used later
from fpdf import FPDF

# Defining class pdf to use FPDF
class pdf:
    # Class method to created the pdf
    def create(name):
        # See necessary syntax in fpdp documentation
        pdf = FPDF()
        pdf.add_page(orientation="portrait", format="a4")
        pdf.set_font("helvetica", "", 40)
        pdf.text(x = 50, y = 50, text="CS50 Shirtificate")
        pdf.image("shirtificate.png", 25, 70, w=160)
        pdf.set_font("Helvetica", "B", size=40)
        pdf.set_text_color(255,255,255)
        pdf.cell(0, 255, f"{name} took CS50", align="C")
        pdf.output("shirtificate.pdf")

# Defining main to get input
def main():
    pdf.create(input("Name: "))

# To execute the program
if __name__ == "__main__":
    main()