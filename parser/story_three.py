#!/usr/bin/env python

"parse input into output per User Story 3 in kata.txt and settings.py"

from lines import lines_from_path
from entries import entries_from_lines
from figures import figures_from_entries
from numerals import numerals_from_figures
from accounts import accounts_from_numerals
from results import results_from_accounts

def parse(path):
    "return Results from input file at Path"
    lines = lines_from_path(path)
    entries = entries_from_lines(lines)
    figures = figures_from_entries(entries)
    numerals = numerals_from_figures(figures)
    accounts = accounts_from_numerals(numerals)
    results = results_from_accounts(accounts)
    for result in results:
        print(result)
        
if __name__ == "__main__":
    path = '-'  # TODO: take input and output paths from docopt
    parse(path)
