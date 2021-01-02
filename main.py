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


def is_installed():
    try:
        pkgctrl_settings = sublime.load_settings('Package Control.sublime-settings')
        return PKG_NAME in set(pkgctrl_settings.get('installed_packages', []))
    except Exception as e:
        return False


def plugin_loaded():
    try:
        from package_control import events
    except ImportError:
        pass
    else:
        w = sublime.active_window()
        if events.install(PKG_NAME) and not is_installed():
            w.run_command('print_open_docs', {'resource_path': '.sublime/messages/install.md'})
        elif events.post_upgrade(PKG_NAME):
            w.run_command('print_open_docs', {'resource_path': '.sublime/messages/upgrade.md'})


# def plugin_unloaded():
