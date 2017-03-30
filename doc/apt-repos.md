% APT-REPOS(1)
% Christoph Lutz
% March 2017

# NAME
[//]: # (!!!GENERATED PART START!!! ID: APT-REPOS/NAME)
apt-repos
[//]: # (!!!GENERATED PART END!!!)

# SYNOPSIS
[//]: # (!!!GENERATED PART START!!! ID: APT-REPOS/USAGE)
usage: apt-repos [-h] [-b BASEDIR] {list,ls,suites,show} ...

[//]: # (!!!GENERATED PART END!!!)

# DESCRIPTION
[//]: # (!!!GENERATED PART START!!! ID: APT-REPOS/DESCRIPTION)
Display information about binary PACKAGE(s) in diverse apt-repositories and suites.
   This tool uses apt-mechanisms to scan for repositories/suites that are registered in
   a suites-file. For each repository/suite combination a local caching folder
   is created in which downloaded Packages files are stored, similar to the cache
   known from apt-cache which lives in /var/lib/apt/lists.
[//]: # (!!!GENERATED PART END!!!)

# GENERAL OPTIONS
[//]: # (!!!GENERATED PART START!!! ID: APT-REPOS/OPTIONS)
  {list,ls,suites,show}
                        choose one of these subcommands
    list (ls)           search and list binary and source packages
    suites              list configured suites
    show                show details about packages similar to apt-cache show

  -h, --help            Show a (subcommand specific) help message
  -b BASEDIR, --basedir BASEDIR
                        Set a new/custom basedir for config-data and caching.
                        Please provide the basedir as an absolute path. The
                        default is $HOME/.apt-repos. The basedir must at least
                        contain a file named 'suites'. The cache will be
                        created into a subfolder called '<basedir>/.apt-
                        repos_cache'.

[//]: # (!!!GENERATED PART END!!!)


