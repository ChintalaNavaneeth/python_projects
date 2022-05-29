#Writing file from excel
import openpyxl

path = (r"C:/Users/navan/OneDrive/Desktop/new.xlsx")
workbook = openpyxl.load_workbook(path)
sheet = workbook.active

for i in range(1,5):
    for c in range(1,4):
        sheet.cell(row=i,column=c).value="welcome"

workbook.save(path)