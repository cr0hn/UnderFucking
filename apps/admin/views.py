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


from django.shortcuts import render_to_response
from django.http import HttpResponseForbidden
from django.template import RequestContext
from underfucking.http import generate_http_error_page
from random import randint

def admin_home(request):

    # Generate a random error page
    a = HttpResponseForbidden(generate_http_error_page())
    a['Server'] = "UnderFucking Server"
    return a
