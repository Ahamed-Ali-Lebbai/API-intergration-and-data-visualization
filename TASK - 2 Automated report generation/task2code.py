import pandas as pd
from fpdf import FPDF

# Step 1: Read Data from CSV File
data = pd.read_csv("sample_data.csv")  # Ensure this file is in your directory

# Step 2: Analyze Data (example: basic statistics)
summary = data.describe(include='all').transpose().round(2)

# Step 3: Generate PDF using FPDF
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(200, 10, "Data Analysis Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def add_table(self, df):
        self.set_font("Arial", "B", 10)
        col_widths = [40, 25, 25, 25, 25, 25, 25, 25]
        columns = df.columns.tolist()
        for i, col in enumerate(columns):
            self.cell(col_widths[i % len(col_widths)], 10, str(col), 1, 0, 'C')
        self.ln()
        self.set_font("Arial", "", 10)
        for index, row in df.iterrows():
            self.cell(col_widths[0], 10, str(index), 1)
            for i in range(1, len(columns)):
                self.cell(col_widths[i % len(col_widths)], 10, str(row[columns[i]]), 1)
            self.ln()

# Create PDF
pdf = PDFReport()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(0, 10, "Summary Statistics:", ln=True)
pdf.ln(5)
pdf.add_table(summary.reset_index())

# Save the PDF
pdf.output("Data_Analysis_Report.pdf")
print("PDF report generated successfully as 'Data_Analysis_Report.pdf'")