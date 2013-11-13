from openpyxl.reader.excel import load_workbook

filename="xxx.xls"
RequestFile = load_workbook(filename = r'%s' % filename)
ws = RequestFile.get_sheet_by_name(sheetnames[0])
print ws.cell(row = 8,column = 1).value
