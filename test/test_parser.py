#!/usr/bin/env python

""" Test the scanner_parser module"""

import pytest

import settings

from tools.decorators import repeats
from tools.makers.input_lines import MakeInputLines
from tools.makers.input_file import MakeInputFile
from tools.makers.entry_lines import MakeEntryLines
from parser.parser import Parser, InputError

def test_instantiation_with_no_argument():
    " confirm Parser requires more than zero arguments "
    with pytest.raises(TypeError):
        p = Parser()

def test_instantiation_with_multiple_arguments(min=2,max=10):
    " confirm Parser requires fewer than 2 arguments "
    for arg_count in range(min,max+1):
        pytest.raises(TypeError, Parser, *range(arg_count))
    
def test_instantiation_with_valid_file(tmpdir):
    " confirm Parser instantiates when given the path to valid file "
    lines = MakeInputLines.random()
    valid_file_path = MakeInputFile.write(tmpdir,lines)
    p = Parser(valid_file_path)
    assert isinstance(p, Parser)
    
@repeats(1000)
def test_instantiation_with_valid_lines():
    " confirm Parser instantiates with a valid path string argument "
#    path = 
#    p = Entry(MakeInputLines.random())
#    assert isinstance(e,Entry)
    pass



FileErrors = """
    can't open file
    file empty
    file ended mid-entry
"""

full_check = """
def test_recognition_of_numbers_in_valid_file():
    " confirm scanner_parser parses valid file into correct account numbers "
    account_number = random_account_number()
    entry_lines = account_number_to_lines(account_number)
    e = Entry(tuple(entry_lines))
    assert e.account_number == account_number
"""
#def test_handling_of_file_containing_faulty_figures():

# NOT a real test - just briefly testing MakeInputFile
def test_file(tmpdir):
    lines = MakeInputLines.random()
    F = MakeInputFile.write(tmpdir,lines).open()
    A = F.readline()
    B = F.readline()
    assert A != B

    #more
