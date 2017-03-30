% APT-REPOS-SHOW(1)
% Christoph Lutz
% March 2017

# NAME
[//]: # (!!!GENERATED PART START!!! ID: APT-REPOS-SHOW/NAME)
apt-repos show
[//]: # (!!!GENERATED PART END!!!)

# SYNOPSIS
[//]: # (!!!GENERATED PART START!!! ID: APT-REPOS-SHOW/USAGE)
usage: apt-repos show [-h] [-d] [-s SUITE] [-a ARCHITECTURE] [-c COMPONENT]
                      [-r] [-col COLUMNS] [-di DIFF] [-dt DIFF_TOOL] [-nu]
                      package [package ...]

[//]: # (!!!GENERATED PART END!!!)

# DESCRIPTION
[//]: # (!!!GENERATED PART START!!! ID: APT-REPOS-SHOW/DESCRIPTION)
subcommand show: print details about packages similar to what apt-cache show does
[//]: # (!!!GENERATED PART END!!!)

# GENERAL OPTIONS
[//]: # (!!!GENERATED PART START!!! ID: APT-REPOS-SHOW/OPTIONS)
  package               Name of a binary PACKAGE or source-package name
                        prefixed as src:SOURCENAME

  -h, --help            show this help message and exit
  -d, --debug           Switch on debugging message printed to stderr.
  -s SUITE, --suite SUITE
                        Only show info for these SUITE(s). The list of SUITEs
                        is specified comma-separated. The default value is
                        'default:'.
  -a ARCHITECTURE, --architecture ARCHITECTURE
                        Only show info for ARCH(s). The list of ARCHs is
                        specified comma-separated.
  -c COMPONENT, --component COMPONENT
                        Only show info for COMPONENT(s). The list of
                        COMPONENTs is specified comma-separated. Note:
                        component and section fields are not exactly the same.
                        A component is only the first part of a section
                        (everything before the '/'). There is also a special
                        treatment for sections in the component 'main', in
                        which case 'main/' is typically not named in a
                        section-field. For this switch -c we have to specify
                        'main' to see packages from the component 'main'.
  -r, --regex           Treat PACKAGE as a regex. Searches for binary package-
                        names or binary packages that were built from a source
                        prefixed with 'src:'. Examples: Use regex '.' to show
                        all packages. Use regex '^pkg' to show all packages
                        starting with 'pkg'. Use regex '^src:source' to show
                        packages that were built from a source starting with
                        'source'.
  -col COLUMNS, --columns COLUMNS
                        Specify the columns that should be printed. Default is
                        'sR'. Possible characters are: (p)=Package,
                        (v)=Version, (s)=Suite, (a)=Arch, (S)=Section,
                        (P)=Priority, (C)=Source, (L)=Long-Desc, (R)=Full-
                        Record
  -di DIFF, --diff DIFF
                        Similar to -s switch, but expects in DIFF exactly two
                        comma separated parts ("suiteA,suiteB"), calculates
                        the output for suiteA and suiteB separately and diff's
                        this output with the diff tool specified in --diff-
                        tool.
  -dt DIFF_TOOL, --diff-tool DIFF_TOOL
                        Diff-Tool used to compare the separated results from
                        --diff. Default is 'diff,--side-by-side,--suppress-
                        common-lines,--width=<ttyWidth>'. Use _ instead of
                        spaces if this command has arguments.
  -nu, --no-update      Skip downloading of packages list.

[//]: # (!!!GENERATED PART END!!!)

