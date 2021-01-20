import xlwt
import xlrd
import re

wb = xlrd.open_workbook(filename='movie_data.xlsx') #打开文件

sheet = wb.sheet_by_index(1)#通过索引获取表格

