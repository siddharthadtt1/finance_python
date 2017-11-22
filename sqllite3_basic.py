# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 22:18:00 2017

@author: sid
"""

import numpy as np
import sqlite3 as sq3
import os

def create_table(file_name):
    conn = sq3.Connection(file_name)
    query_create = 'CREATE TABLE numbers (No1 real, No2 real,\
                    No3 real, No4 real, No5 real)'
    conn.execute(query_create)
    conn.commit()
    conn.close()
    
    
def populate_table(file_name):
    conn = sq3.Connection(file_name)
    query_insert = 'INSERT INTO numbers values (?, ?, ?, ?, ?)'
    data = np.random.standard_normal((1000000, 5)).round(5)
    conn.executemany(query_insert, data)
    conn.commit()
    conn.close()
    
    
def fetch_all_entries(file_name):
    conn = sq3.Connection(file_name)
    query_fetch = 'SELECT * FROM numbers'
    return conn.execute(query_fetch).fetchall()

def fetch_select_entries(file_name):
    conn = sq3.Connection(file_name)
    query_cfetch = 'SELECT * FROM numbers WHERE No1 > 0 AND No2 < 0'
    return np.array(conn.execute(query_cfetch).fetchall()).round(3)
    

file_name=os.getcwd() + '\\numbr.db' 

""" create table  """
#create_table(file_name)   

""" insert data into table """
#populate_table(file_name)

""" fetch all entries from table """
entries = fetch_all_entries(file_name)

""" fetch filtered entries from table """
c_entries = fetch_select_entries(file_name)

