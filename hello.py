
# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = ("C:\Python") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0)
