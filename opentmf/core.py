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

from ctypes import c_void_p, byref
from .library import lib
from .utils import convert_version, chk
from .const import HT_DRIVER
from .exceptions import InvalidURLError
from .context import Context
from .driver import Driver


def new_context():
    return Context()


def get_version():
    return convert_version(lib.opentmf_get_version().contents)


def get_status_str(status):
    return lib.opentmf_get_status_str(status)


def open(ctx, url):
    handle = c_void_p(None)
    chk(lib.opentmf_open(ctx.value, url, byref(handle)))
    try:
        ht = lib.opentmf_get_handle_type(handle)
        if ht == HT_DRIVER:
            return Driver(ctx, handle)
        else:
            raise InvalidURLError()
    except Exception as e:
        lib.opentmf_close(handle)
        raise e
