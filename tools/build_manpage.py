#!/usr/bin/env python
"""
manpage creation tooling derived from 'script to install pwman3'
"""

import datetime
import argparse
import sys
import os


# The BuildManPage code is distributed
# under the same License of Python
# Copyright (c) 2014 Oz Nahum Tiram  <nahumoz@gmail.com>

"""
Add a `build_manpage` command  to your setup.py.
To use this Command class import the class to your setup.py,
and add a command to call this class::

    from build_manpage import BuildManPage

    ...
    ...

    setup(
    ...
    ...
    cmdclass={
        'build_manpage': BuildManPage,
    )

You can then use the following setup command to produce a man page::

    $ python setup.py build_manpage --output=prog.1
        --parser=yourmodule:argparser

Alternatively, set the variable AUTO_BUILD to True, and just invoke::

    $ python setup.py build

If automatically want to build the man page every time you invoke your build,
add to your ```setup.cfg``` the following::

    [build_manpage]
    output = <appname>.1
    parser = <path_to_your_parser>
"""


class ManPageFormatter(argparse.HelpFormatter):

    """
    Formatter class to create man pages.
    This class relies only on the parser, and not distutils.
    The following shows a scenario for usage::

        from pwman import parser_options
        from build_manpage import ManPageFormatter

        # example usage ...

        dist = distribution
        mpf = ManPageFormatter(appname,
                               desc=dist.get_description(),
                               long_desc=dist.get_long_description(),
                               ext_sections=sections)

        # parser is an ArgumentParser instance
        m = mpf.format_man_page(parsr)

        with open(self.output, 'w') as f:
            f.write(m)

    The last line would print all the options and help infomation wrapped with
    man page macros where needed.
    """

    def __init__(self,
                 prog,
                 indent_increment=2,
                 max_help_position=24,
                 width=None,
                 section=1,
                 desc=None,
                 long_desc=None,
                 ext_sections=None,
                 authors=None,
                 ):

        super(ManPageFormatter, self).__init__(prog)

        self._prog = prog
        self._section = 1
        self._today = datetime.date.today().strftime('%Y\\-%m\\-%d')
        self._desc = desc
        self._long_desc = long_desc
        self._ext_sections = ext_sections

    def _get_formatter(self, **kwargs):
        return self.formatter_class(prog=self.prog, **kwargs)

    def _markup(self, txt):
        return txt

    def _underline(self, string):
        return "__" + string + "__"

    def _bold(self, string):
        if not string.strip().startswith('**'):
            string = '**' + string
        if not string.strip().endswith('**'):
            string = string + '**'
        return string

    def _mk_synopsis(self, parser):
        self.add_usage(parser.usage, parser._actions,
                       parser._mutually_exclusive_groups, prefix='')
        usage = self._format_usage(None, parser._actions,
                                   parser._mutually_exclusive_groups, '')
        usage = usage.replace('%s ' % self._prog, '')
        usage = '# SYNOPSIS\n%s %s\n' % (self._markup(self._prog), usage)
        return usage

    def _mk_title(self, prog):
        return ''

    def _make_name(self, parser):
        return ''

    def _mk_description(self):
        if self._long_desc:
            long_desc = self._long_desc
            return '# DESCRIPTION\n%s\n' % self._markup(long_desc)
        else:
            return ''

    def _mk_footer(self, sections):
        if not hasattr(sections, '__iter__'):
            return ''

        footer = []
        for section, value in sorted(sections.items()):
            part = "# {}\n {}".format(section.upper(), value)
            footer.append(part)

        return '\n'.join(footer)

    def format_man_page(self, parser):
        page = []
        page.append(self._mk_title(self._prog.replace(" ", "-")))
        page.append(self._mk_synopsis(parser))
        page.append(self._mk_description())
        page.append(self._mk_options(parser))
        page.append(self._mk_footer(self._ext_sections))

        return ''.join(page)

    def _mk_options(self, parser):

        formatter = parser._get_formatter()

        # positionals, optionals and user-defined groups
        for action_group in parser._action_groups:
            formatter.start_section(None)
            formatter.add_text(None)
            formatter.add_arguments(action_group._group_actions)
            formatter.end_section()

        # epilog
        formatter.add_text(parser.epilog)

        # determine help from format above
        return '# OPTIONS\n' + formatter.format_help()

    def _format_action_invocation(self, action):
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar

        else:
            parts = []

            # if the Optional doesn't take a value, format is:
            #    -s, --long
            if action.nargs == 0:
                parts.extend([self._bold(action_str) for action_str in
                              action.option_strings])

            # if the Optional takes a value, format is:
            #    -s ARGS, --long ARGS
            else:
                default = self._underline(action.dest.upper())
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append('%s %s' % (self._bold(option_string),
                                            args_string))

            return ', '.join(parts)

