#!/usr/bin/python3

import os
import sys
import re

sys.path.append("src/")
from apt_repos import createArgparsers, __doc__, ls, show, suites


def main():	
    (parser, parser_ls, parser_show, parser_suites) = createArgparsers()

    infos = {}
    getParserInfos(infos, parser, 'apt-repos', __doc__.strip())
    getParserInfos(infos, parser_ls, 'apt-repos ls', ls.__doc__.strip())
    getParserInfos(infos, parser_show, 'apt-repos show', show.__doc__.strip())
    getParserInfos(infos, parser_suites, 'apt-repos suites', suites.__doc__.strip())

    for filename in sys.argv[1:]:
        writeParserInfosToFile(infos, filename)


def writeParserInfosToFile(infos, filename):
    res = ""
    addLine = True
    with open(filename, "r") as fh:
        for line in fh.readlines():
            m = re.match(".*\(!!!GENERATED PART START!!! ID:\s*([A-Z\\/-]+)\)\s*", line)
            if m:
                addLine = False
                res += line
                info = infos.get(m.group(1))
                if info:
                    res += info + '\n\n'
                else:
                   print("ERROR: can't generate part for id '{}'".format(m.group(1)), file=sys.stderr)

            if '(!!!GENERATED PART END!!!)' in  line:
                addLine = True

            if addLine:
                res += line
    
    with open(filename, "w") as fh:
        print(res, file=fh)


def getParserInfos(infos, parser, appname, desc):
    prefix = appname.replace(' ', '-').upper()
    infos[prefix + "/NAME"] = appname
    infos[prefix + "/DESCRIPTION"] = desc
    infos[prefix + "/USAGE"] = parser.format_usage()
    infos[prefix + "/OPTIONS"] = get_options(parser)


def get_options(parser):
    # This method is copied and adjusted from the BuildManPage code
    # that is distributed "under the same License of Python"
    # Copyright (c) 2014 Oz Nahum Tiram  <nahumoz@gmail.com>
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
    return formatter.format_help()


if __name__ == "__main__":
    main()
