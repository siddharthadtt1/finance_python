# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 11:49:28 2018

@author: sd835979
"""

#
# Test suite for simple function f
# nose_test.py
#

import nose.tools as nt
from simple_function import f

def test_f_calculation():
    " Test if function f calculates correctly. "
    nt.assert_equal(f(4.), 4)
    nt.assert_equal(f(1000), 1000)
    nt.assert_equal(f(5000.5), 5000.5)
    
def test_f_type_error():
    " Test if type error is raised "
    nt.assert_raises(TypeError, f, 'test string')
    nt.assert_raises(TypeError, f, [3, 'string'])

def test_f_value_error():
    " Test if value error is raised"
    nt.assert_raises(ValueError, f, -3)
    nt.assert_raises(ValueError, f, -1.25)
    
def test_f_test_fails():
    " Test if function test fails. False positive"
    nt.assert_equal(f(4), 10)