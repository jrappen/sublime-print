#!/usr/bin/env python3.3
# coding: utf-8


#[ Reload package after update ]################################################


import sys                                                                      # https://docs.python.org/3.3/library/sys.html


prefix = __package__ + "."
for module_name in [
    module_name
    for module_name in sys.modules
    if module_name.startswith(prefix) and module_name != __name__
]:
    del sys.modules[module_name]
prefix = None


################################################################################


from .src import *
