#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
UnderFucking - The real vulnerable web site - Copyright (C) 2011-2013

Authors:
  Daniel Garcia Garcia a.k.a cr0hn | cr0hn<@>cr0hn.com

UnderFucking project site: https://github.com/cr0hn/UnderFucking

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

#----------------------------------------------------------------------
# Fix the module load path when running as a portable script and during installation.

import sys
from sys import version_info, exit
if __name__ == "__main__":
    if version_info < (2, 7) or version_info > (3, 0):
        print "[!] You must use Python version 2.7"
        exit(1)

from os import path, getcwd, environ
import argparse

#
# This code was borrowed from GoLismero Project
if __name__ == "__main__":

    # Change path. Adding thirdparty_libs
    try:
        _FIXED_PATH_
    except NameError:
        here = path.split(path.abspath(__file__))[0]
        if not here:  # if it fails use cwd instead
            here = path.abspath(getcwd())
        thirdparty_libs = path.join(here, "thirdparty_libs")
        if path.exists(thirdparty_libs):
            if __name__ == "__main__":
                # As a portable script: use our versions always
                sys.path.insert(0, thirdparty_libs)
                sys.path.insert(0, here)
            else:
                # When installing: prefer system version to ours
                sys.path.insert(0, here)
                sys.path.append(thirdparty_libs)
        _FIXED_PATH_ = True

    # Add command line options
    parser = argparse.ArgumentParser()

    # Main options
    gr_main = parser.add_argument_group("main options")
    gr_main.add_argument("-p", "--listen-port", metavar="LISTEN_PORT", dest="listen_port", help="listen port (default 8080)", default=8080, type=int)
    gr_main.add_argument("-l", "--listen-ip", metavar="LISTEN_IP", dest="listen_ip", help="listen ip (default 127.0.0.1)", default="127.0.0.1")

    P = parser.parse_args()

    m_listen = "%s:%s" % (P.listen_ip, str(P.listen_port))

    # Run it
    environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line([sys.argv[0],'runserver', m_listen])
