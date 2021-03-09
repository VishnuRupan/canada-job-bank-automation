import openpyxl as op
import time
from datetime import datetime


def createSpreadsheet(final_data=[]):

    try:
        wb = op.Workbook()
        ws = wb.active

        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        for col in letters:
            ws.column_dimensions[col].width = 35


        ws.append(["Title", "Posted By", "Email", "Job Bank ID", "Salary", "Date Applied"])

        for row in final_data:
            ws.append(row)

        date = datetime.today().strftime('%Y-%m-%d')
        wb.save("table_{0}.xlsx".format(date))
    except:
        print("\nThe spreadsheet function of this program has crashed. Please manually close the program and try again.\nIf this error persists, please contact the developer\n.")
        time.sleep(30)
        print('please close the program')
        time.sleep(30)