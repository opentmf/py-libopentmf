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


class opentmf_driver_info(Structure):
    _fields_ = [
        ("version", opentmf_version),
        ("name", c_char_p),
        ("description", c_char_p),
        ("authors", c_char_p),
        ("license", c_char_p),
        ("non_free", c_uint8)]


lib = CDLL('libopentmf.so.0')

# Core:
lib.opentmf_init.argtypes = [POINTER(c_void_p)]
lib.opentmf_init.restype = c_int
lib.opentmf_exit.argtypes = [c_void_p]
lib.opentmf_exit.restype = c_int
lib.opentmf_get_version.argtypes = []
lib.opentmf_get_version.restype = POINTER(opentmf_version)
lib.opentmf_get_status_str.argtypes = [c_int]
lib.opentmf_get_status_str.restype = c_char_p
lib.opentmf_open.argtypes = [c_void_p, c_char_p, POINTER(c_void_p)]
lib.opentmf_open.restype = c_int
lib.opentmf_close.argtypes = [c_void_p]
lib.opentmf_close.restype = c_int
lib.opentmf_get_handle_type.argtypes = [c_void_p]
lib.opentmf_get_handle_type.restype = c_int

# Driver:
lib.opentmf_drv_get_info.argtypes = [c_void_p]
lib.opentmf_drv_get_info.restype = POINTER(opentmf_driver_info)