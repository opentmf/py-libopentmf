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

from .const import *
from .types import *
from .exceptions import *


def chk(status):
    if status >= SUCCESS:
        return
    elif status == E_NO_MEMORY:
        raise NoMemoryError()
    elif status == E_NOT_SUPPORTED:
        raise NotSupportedError()
    elif status == E_FAILED:
        raise FailedError()
    elif status == E_INVALID_HANDLE:
        raise InvalidHandleError()
    else:
        raise OpenTMFError(status, '')


def convert_version(version):
    return Version(version.major, version.minor, version.patch, version.extra)
