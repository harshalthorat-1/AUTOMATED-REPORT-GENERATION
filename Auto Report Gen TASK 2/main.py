import csv
from fpdf import FPDF

# Step 1: Read Data from a File
def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Step 2: Analyze the Data
def analyze_data(data):
    if not data:  # Check if the list is empty
        return 0  # Return 0 or handle it as you wish
    total_age = sum(int(row['Age']) for row in data)
    average_age = total_age / len(data)
    return average_age

# Step 3: Generate the PDF Report
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Automated Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_report_data(self, data, average_age):
        self.add_page()
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Average Age: {average_age:.2f}', 0, 1, 'L')
        self.cell(0, 10, '', 0, 1, 'L')  # Blank line

        for row in data:
            self.cell(0, 10, f"Name: {row['Name']}, Age: {row['Age']}, Grade: {row['Grade']}", 0, 1, 'L')

# Main Script
if __name__ == '__main__':
    file_path = 'data.csv'
    data = read_data(file_path)

    if not data:
        print("No data found in the file. Please check the file content.")
    else:
        average_age = analyze_data(data)
        pdf = PDF()
        pdf.add_report_data(data, average_age)
        pdf.output('report.pdf')
        print("Report generated successfully as 'report.pdf'")
