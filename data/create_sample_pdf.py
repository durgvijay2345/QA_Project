# create_sample_pdf.py
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

lines = [
    "Company HR Policy Document",
    "",
    "Leave Policy:",
    "Employees are entitled to 20 days of annual leave per year.",
    "Sick leave allowance is 10 days per year.",
    "Maternity leave is 6 months for female employees.",
    "Paternity leave is 15 days for male employees.",
    "",
    "Work Hours:",
    "Office hours are 9 AM to 6 PM Monday to Friday.",
    "Saturday is optional work from home day.",
    "",
    "Salary:",
    "Salaries are credited on last working day of every month.",
    "Annual increment is based on performance review in December.",
    "",
    "Company Rules:",
    "All employees must follow the code of conduct.",
    "Remote work is allowed twice a week.",
    "Notice period is 30 days for resignation.",
]

for line in lines:
    pdf.cell(0, 10, line, ln=True)

pdf.output("data/sample.pdf")
print("Sample PDF ready!")
