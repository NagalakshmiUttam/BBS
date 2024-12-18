import xlsxwriter

class TestXlsxWriter():
 

    

    workbook = xlsxwriter.Workbook("AllAboutPythonExcel.xlsx")
    worksheet = workbook.add_worksheet("menu")

    scores = (
    ['HOME', 1000],
    ['COMPANY',   100],
    ['SERVICES',  300],
    ['DESIGN LAB',    50],
    )

    row=0
    col=0

    for name, score in (scores):
        worksheet.write(row, col, name)
        worksheet.write(row, col + 1, score)
        row += 1
    


    workbook.close()




