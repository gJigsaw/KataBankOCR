#!/usr/bin/env python

import settings

class EntryError(Exception):
    " Base class for exceptions in this module "
    pass

class InputError(EntryError):
    " Exception raised for errors in the input "
    def __init__(self,value):
        self.value = value

class Entry():
    " Lines of characters containing figures that represent an account number "
    def __init__(self,lines):
        pass
