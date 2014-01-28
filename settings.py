" Static values that restate the problem description "

# An Entry consists of a list of lines (as strings)
# An Entry has a defined number of lines
lines_per_entry = 4
# An Entry has only whitespace in its final line
last_line_empty = True
# An Entry represents an Account String composed of Account Characters
# The four lines in this example Entry represent the Account String '123456789'
# an_example_entry_list = ['    _  _     _  _  _  _  _ ',
#                          '  | _| _||_||_ |_   ||_||_|',
#                          '  ||_  _|  | _||_|  ||_| _|',
#                          '                           ',]
# A Figure consist of one string that represents one Account Character
# A Figure results by joining veritcally adjacent Substrings across all Lines
# All Substrings have a known length
figure_width = 3
# All Figures have a known length
figure_length = figure_width * lines_per_entry  # 12
# The single string in this example Figure represents the Account Character '5'
# an_example_figure_string =\
#    ' _ '+\
#    '|_ '+\
#    ' _|'+\
#    '   '
# Every Figure is composed only of spaces, underscores, and pipes
valid_figure_characters = tuple('_ |')
# Every Account Character consists of a single digit string
valid_account_characters = tuple('0123456789')
# Every Figure uniquely represents a unique Account Character
figures = {' _ '+
           '| |'+
           '|_|'+
           '   ':'0',
           '   '+
           '  |'+
           '  |'+
           '   ':'1',
           ' _ '+
           ' _|'+
           '|_ '+
           '   ':'2',
           ' _ '+
           ' _|'+
           ' _|'+
           '   ':'3',
           '   '+
           '|_|'+
           '  |'+
           '   ':'4',
           ' _ '+
           '|_ '+
           ' _|'+
           '   ':'5',
           ' _ '+
           '|_ '+
           '|_|'+
           '   ':'6',
           ' _ '+
           '  |'+
           '  |'+
           '   ':'7',
           ' _ '+
           '|_|'+
           '|_|'+
           '   ':'8',
           ' _ '+
           '|_|'+
           ' _|'+
           '   ':'9'}

# All Entries contain the same number of Figures
figures_per_entry = 9
# All Lines have a known length
line_length = figure_width * figures_per_entry  # 27

# All Input Files contain _approximately_ the same number of entries
approximate_entries_per_file = 500

# The Checksum differentiates between 'valid' and 'invalid' account strings
def checksum(account_string):
    " return True for a valid ccount_string and False for invalid account string "
    value = lambda index: int(account_string[index]) * (9 - index)
    return sum(value(i) for i in range(figures_per_entry)).__mod__(11) == 0
# The Checksum will return True for these strings
some_known_valid_account_strings = ('123456789', '490867715', '899999999',
                                    '000000051', '686666666', '559555555')
# The Checksum will return False for these strings
some_known_invalid_account_strings = ('490067715', '888888888', '555555555',
                                      '333333333', '111111111', '777777777')
