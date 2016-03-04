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

from ctypes import c_void_p, c_char_p, byref, POINTER
from .library import lib
from .utils import chk


class Context(object):
    """OpenTMF context"""

    def __init__(self):
        super(Context, self).__init__()
        self.value = c_void_p(None)
        chk(lib.opentmf_init(byref(self.value)))

    def __del__(self):
        chk(lib.opentmf_exit(self.value))

    def get_driver_list(self):
        driver_names = []
        lst = POINTER(c_char_p)()

        chk(lib.opentmf_get_driver_list(self.value, byref(lst)))

        for item in lst:
            if item is None:
                break
            driver_names.append(item)

        chk(lib.opentmf_free_driver_list(self.value, lst))

        return driver_names
