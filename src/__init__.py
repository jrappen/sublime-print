#!/usr/bin/env python
# coding: utf-8


import sublime

from .window_commands import *


PKG_NAME = __package__.split('.')[0]


def plugin_loaded():
    try:
        from package_control import events
        if events.install(PKG_NAME):
            sublime.active_window().run_command(
                'print_open_docs',
                {
                    'resource_path': '.sublime/messages/install.md'
                }
            )
        elif events.post_upgrade(PKG_NAME):
            sublime.active_window().run_command(
                'print_open_docs',
                {
                    'resource_path': '.sublime/messages/upgrade.md'
                }
            )
    except Exception as e:
        pass
