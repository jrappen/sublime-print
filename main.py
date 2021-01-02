#!/usr/bin/env python
# coding: utf-8


PKG_NAME = __package__.split('.')[0]


try:
    from package_control import events
except ImportError:
    pass
else:
    if events.post_upgrade(PKG_NAME):
        import sys
        prefix = PKG_NAME + '.'
        modules_to_clear = {
            module_name
            for module_name in sys.modules
            if module_name.startswith(prefix) and module_name != __name__
        }
        print('{}: Cleaning up "{}" cached modules after update…'.format(PKG_NAME, modules_to_clear))
        for module_name in modules_to_clear:
            del sys.modules[module_name]



from .src import *


def plugin_loaded():
    .src.window_commands.plugin_loaded()

# def plugin_unloaded():
    # .src.window_commands.plugin_unloaded()
