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


# Structs:
class opentmf_version(Structure):
    _fields_ = [
        ("major", c_uint16),
        ("minor", c_uint16),
        ("patch", c_uint16),
        ("extra", c_char_p)]


lib = CDLL('libopentmf.so.0')

# Core:
lib.opentmf_init.argtypes = [POINTER(c_void_p)]
lib.opentmf_init.restype = c_int
lib.opentmf_exit.argtypes = [c_void_p]
lib.opentmf_exit.restype = c_int
lib.opentmf_get_version.argtypes = []
lib.opentmf_get_version.restype = POINTER(opentmf_version)
