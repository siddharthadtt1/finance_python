# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:29:45 2017

@author: sid
"""

import numpy as np
import pandas as pd
import xlrd, xlwt
import xlsxwriter
import os

# populate xls file 
def func_populate_xls_file(file_name, data):    
    # create a workbook
    wb = xlwt.Workbook()
    
    # add worksheets
    ws_1 = wb.add_sheet('sheet_1')
    ws_2 = wb.add_sheet('sheet_2')
    
    dump_data(ws_1, ws_2, file_name, data)
    
    wb.save(file_name)
    
# populates xlsx file
def func_populate_xlsx_file(file_name, data):
    #create a workbook
    wb = xlsxwriter.Workbook(file_name)
    
    # add worksheets
    
    ws_1 = wb.add_worksheet('sheet_1')
    ws_2 = wb.add_worksheet('sheet_2')
    
    dump_data(ws_1, ws_2, file_name, data)
    
    wb.close()

def create_chart(file_name, data):
    wb = xlsxwriter.Workbook(file_name)
    
    ws_1 = wb.add_worksheet('first_sheet')
    ws_1.write_column('A1', data)
    
    # create a new chart object
    chart = wb.add_chart({'type': 'line'})
    
    # add a series to the chart
    chart.add_series({'values': '=first_sheet!$A$1:$A$15', 
                      'marker': {'type': 'diamond'}, })

    # series with marker diamond
    ws_1.insert_chart('C1', chart)
    
    wb.close()
    
def func_read_xls_file(file_name):
    # read book from xls file
    book = xlrd.open_workbook(file_name)
    
    # fetch the sheet names
    sheet_names = book.sheet_names()
    print 'Sheet names : ' + str(sheet_names)
    
    # print content of each sheet
    for sheet_name in sheet_names:
        sheet = book.sheet_by_name(sheet_name)
        print ' ****** ' + sheet_name + ' ******** '
        for r in range(sheet.nrows):
            for c in range(sheet.ncols):
                print '%i' % sheet.cell(r, c).value , 
            print
    
def dump_data(ws_1, ws_2, file_name, data):
    for c in range(data.shape[0]):
        for r in range(data.shape[1]):
            ws_1.write(c, r, data[c, r])
            ws_2.write(c, r, data[r, c])




file_name_xls = os.getcwd() + "\\workbook.xls"

data = np.arange(1, 65).reshape((8, 8))

func_populate_xls_file(file_name_xls, data)

file_name_xlsx = os.getcwd() + "\\workbook_1.xlsx"
func_populate_xlsx_file(file_name_xlsx, data)

func_read_xls_file(file_name_xlsx)

file_name  = os.getcwd() + "\\chart.xlsx"
data = np.random.standard_normal(15).cumsum()
create_chart(file_name, data)

