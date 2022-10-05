#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin

import os


CSS = '''
html {
    background-color: var(--background);
    margin: 16px;
}
body {
    color: var(--foreground);
    font-family: "Open Sans", "Helvetica Neue", "Segoe UI", Helvetica, Arial, sans-serif;
    line-height: 1.6;
}
h1 {
    color: color(var(--foreground) l(- 10%));
    font-size: 2.0rem;
    margin: 0.7rem 0 0 0;
}
html.dark h1 {
    color: color(var(--foreground) l(+ 10%));
}
h2 {
    color: color(var(--foreground) a(0.9));
    font-size: 1.4rem;
    margin: 1rem 0 0.4rem 0;
}
h3 {
    font-size: 1.2rem;
    margin: 1rem 0 0.1rem 0;
}
a {
    color: var(--bluish);
}
code {
    font-size: 0.9rem;
    border-radius: 2px;
    padding: 0 4px;
}
ul {
    padding-left: 1.8rem;
}
li {
    margin: 2px;
}
li ul {
    margin: 2px 0 4px;
}
'''
FRONTMATTER = {
    "allow_code_wrap": True,
    "markdown_extensions": [
        "markdown.extensions.admonition",
        "markdown.extensions.attr_list",
        "pymdownx.emoji",
        # we do not use pymdownx.magiclink here
        "pymdownx.progressbar",
        "pymdownx.saneheaders",
        {"pymdownx.smartsymbols": {"ordinal_numbers": False}},
        "pymdownx.tasklist"
    ]
}
PKG_NAME = __package__.split('.')[0]


def is_mdpopups_installed():
    try:
        import mdpopups
        return True
    except Exception:
        return False


class PrintOpenDocs(sublime_plugin.WindowCommand):

    def run(self, resource_path='docs/en/README.md'):
        try:
            w = self.window
            import mdpopups
            mdpopups.new_html_sheet(
                window=w,
                name='{}/{}'.format(PKG_NAME, resource_path),
                contents=mdpopups.format_frontmatter(FRONTMATTER) + sublime.load_resource('Packages/{}/{}'.format(PKG_NAME, resource_path)),
                md=True,
                css='{}'.format(CSS)
            )
        except Exception as e:
            print('{}: Exception: {}'.format(PKG_NAME, e))

    # def is_enabled(self): return bool

    def is_visible(self):
        return is_mdpopups_installed()

    # def description(self): return str
    # def input(self, args): return CommandInputHandler or None


class PrintPreviewCodeInBrowser(sublime_plugin.WindowCommand):

    def run(self):
        try:
            w = self.window
            v = w.active_view()
            if v is None:
                return
            import mdpopups
            l = mdpopups.get_language_from_view(v)
            md_preview = mdpopups.syntax_highlight(
                view=v,
                src=v.substr(sublime.Region(0, v.size())),
                language=l
            )
            p = os.path.join(sublime.cache_path(), PKG_NAME, 'index.html')
            os.makedirs(p[:p.rindex(os.path.sep)], exist_ok=True)
            with open(p, mode='w', newline='\n') as f:
                f.write(str(md_preview))
            # TODO: remove pathlib from dependencies.json for py3.8
            import pathlib
            w.run_command('open_url', { 'url': pathlib.Path(p).as_uri() })
        except Exception as e:
            print('{}: Exception: {}'.format(PKG_NAME, e))

    # def is_enabled(self): return bool

    def is_visible(self):
        return is_mdpopups_installed()

    # def description(self): return str
    # def input(self, args): return CommandInputHandler or None


class PrintCopyCodeToClipboard(sublime_plugin.WindowCommand):

    def run(self):
        try:
            w = self.window
            v = w.active_view()
            if v is None:
                return
            import mdpopups
            l = mdpopups.get_language_from_view(v)
            # only copy first selection if selection(s) and (v.sel()[0].__len__() > 0)
            r = v.sel()[0] or sublime.Region(0, v.size())
            md_preview = mdpopups.syntax_highlight(
                view=v,
                src=v.substr(r),
                language=l
            )
            sublime.set_clipboard(str(md_preview))
        except Exception as e:
            print('{}: Exception: {}'.format(PKG_NAME, e))

    # def is_enabled(self): return bool

    def is_visible(self):
        return is_mdpopups_installed()

    # def description(self): return str
    # def input(self, args): return CommandInputHandler or None


class PrintPreviewMarkdownInBrowser(sublime_plugin.WindowCommand):

    def run(self):
        try:
            w = self.window
            v = w.active_view()
            if v is None:
                return
            if not v.settings().get('syntax').startswith('Packages/Markdown/'):
                return
            import mdpopups
            md_preview = mdpopups.md2html(
                view=v,
                markup=v.substr(sublime.Region(0, v.size())),
                template_vars=None,
                template_env_options=None
            )
            p = os.path.join(sublime.cache_path(), PKG_NAME, 'index.html')
            os.makedirs(p[:p.rindex(os.path.sep)], exist_ok=True)
            with open(p, mode='w', newline='\n') as f:
                f.write(md_preview)
            # TODO: remove pathlib from dependencies.json for py3.8
            import pathlib
            w.run_command('open_url', { 'url': pathlib.Path(p).as_uri() })
        except Exception as e:
            print('{}: Exception: {}'.format(PKG_NAME, e))

    # def is_enabled(self): return bool

    def is_visible(self):
        try:
            VERSION = int(sublime.version())
            if VERSION < 4065:
                return False
            import mdpopups
            v = self.window.active_view()
            if v is None:
                return False
            return v.settings().get('syntax').startswith('Packages/Markdown/')
        except Exception:
            return False

    # def description(self): return str
    # def input(self, args): return CommandInputHandler or None


class PrintPreviewMarkdownViaHtmlSheet(sublime_plugin.WindowCommand):

    def run(self):
        try:
            w = self.window
            v = w.active_view()
            if v is None:
                return
            if not v.settings().get('syntax').startswith('Packages/Markdown/'):
                return
            import mdpopups
            mdpopups.new_html_sheet(
                window=w,
                name='[print] << PREVIEW >> (read-only)',
                contents=mdpopups.format_frontmatter(FRONTMATTER) + v.substr(sublime.Region(0, v.size())),
                md=True,
                css='{}'.format(CSS)
            )
            # w.run_command('new_pane')
        except Exception as e:
            print('{}: Exception: {}'.format(PKG_NAME, e))

    # def is_enabled(self): return bool

    def is_visible(self):
        try:
            VERSION = int(sublime.version())
            if VERSION < 4065:
                return False
            import mdpopups
            v = self.window.active_view()
            if v is None:
                return False
            return v.settings().get('syntax').startswith('Packages/Markdown/')
        except Exception:
            return False

    # def description(self): return str
    # def input(self, args): return CommandInputHandler or None
