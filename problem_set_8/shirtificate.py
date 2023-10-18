"""
Problem Set 8 - CS50 Shirtificate
https://cs50.harvard.edu/python/2022/psets/8/shirtificate/
"""

from fpdf import FPDF

class Shirtificate(FPDF):

    def create_shirtificate(self, name):
        # Add a page with 'Portrait' and size 'A4'
        self.add_page(orientation="portrait", format="a4")

        # Set the font
        self.set_font("Helvetica", 'B', 24)

        # Add title "CS50 Shirtificate" centered at the top
        self.cell(0, 60, "CS50 Shirtificate", align="C")

        # Determine the width of the image to center it
        img_width = 190  # This assumes your image width is set to 190mm. Adjust if necessary.
        x_centered = (210 - img_width) / 2

        # Add the shirt image
        self.image("./shirtificate.png", x_centered, 80, img_width)

        # Set the font and color for the user's name
        self.set_font("Helvetica", 'B', 20)
        self.set_text_color(255, 255, 255)  # Set text color to white

        # Calculate position to place the name centered on the shirt
        name_width = self.get_string_width(name)
        x_name = (210 - name_width) / 2
        y_name = 150

        # Place the user's name on the PDF (over the shirt)
        self.text(x_name, y_name, name)

if __name__ == "__main__":
    name = input("Name: ")

    pdf = Shirtificate()
    pdf.create_shirtificate(name)
    pdf.output("shirtificate.pdf")