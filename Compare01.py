#!python

3

import numpy

import numpy.core._methods
import numpy.lib.format

import pandas as pd
import xlrd as xr


#import easygui
print("выберите файл 1")
excelreed1 = xr.open_workbook('2.xlsx')
#excelreed1 = xr.open_workbook(easygui.fileopenbox())
oneexcel = excelreed1.sheet_by_index(0)

print("выберите файл 2")
excelreed2 = xr.open_workbook('1.xlsx')
#excelreed2 = xr.open_workbook(easygui.fileopenbox())
twoexcel = excelreed2.sheet_by_index(0)

list_j = []

for i in range(0,oneexcel.nrows):
    for j in range(0,twoexcel.nrows):
        ##print(i)
        ##print(j)
        ##print(oneexcel.row_values(i)[0])
        ##print(twoexcel.row_values(j)[0])
        if twoexcel.row_values(j)[0] == oneexcel.row_values(i)[0]:
            break
        else:
            if j==(twoexcel.nrows-1):
                list_j.append(oneexcel.row_values(i))
                print("err",i)
                print(j)
                print("error")
                print(list_j)
df = pd.DataFrame(list_j)
df.to_excel('crm_lack.xlsx', header=False, index=False)


##excelreed = xr.open_workbook('1.xlsx')
oneexcel = excelreed2.sheet_by_index(0)
##excelreed = xr.open_workbook('2.xlsx')
twoexcel = excelreed1.sheet_by_index(0)

list_j = []

for i in range(0,oneexcel.nrows):
    for j in range(0,twoexcel.nrows):
        ##print(i)
        ##print(j)
        ##print(oneexcel.row_values(i)[0])
        ##print(twoexcel.row_values(j)[0])
        if twoexcel.row_values(j)[0] == oneexcel.row_values(i)[0]:
            break
        else:
            if j==(twoexcel.nrows-1):
                list_j.append(oneexcel.row_values(i))
                print("err",i)
                print(j)
                print("error")
                print(list_j)
df = pd.DataFrame(list_j)
df.to_excel('1c_lack.xlsx', header=False, index=False)
