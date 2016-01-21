""" Python bindings for Open Test & Measurement Framework library

Copyright (c) 2016 Reinder Feenstra <reinderfeenstra@gmail.com>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library;  If not, see <http://www.gnu.org/licenses/>.
"""

from ctypes import *
from .const import *
from .library import lib
from .utils import *


class Driver(object):
    """"""

    def __init__(self, ctx, handle):
        super(Driver, self).__init__()
        self._ctx = ctx
        self._handle = handle

        info = lib.opentmf_drv_get_info(handle).contents
        self._version = convert_version(info.version)
        self._name = info.name
        self._description = info.description
        self._authors = info.authors
        self._license = info.license
        self._non_free = (info.non_free != FALSE)

    def _get_version(self):
        return self._version

    def _get_name(self):
        return self._name

    def _get_authors(self):
        return self._authors

    def _get_description(self):
        return self._description

    def _get_license(self):
        return self._license

    def _get_non_free(self):
        return self._non_free

    version = property(_get_version)
    name = property(_get_name)
    description = property(_get_description)
    authors = property(_get_authors)
    license = property(_get_license)
    non_free = property(_get_non_free)
