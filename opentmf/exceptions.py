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
from .library import lib


class OpenTMFError(Exception):
    """Base class for all OpenTMF exceptions."""
    def __init__(self, status, message=None):
        if message is None:
            message = lib.opentmf_get_status_str(status)
        super(OpenTMFError, self).__init__(message)
        self.status = status


class NoMemoryError(OpenTMFError):
    """"""

    def __init__(self):
        super(NoMemoryError, self).__init__(E_NO_MEMORY)


class NotSupportedError(OpenTMFError):
    """"""

    def __init__(self):
        super(NotSupportedError, self).__init__(E_NOT_SUPPORTED)


class FailedError(OpenTMFError):
    """"""

    def __init__(self):
        super(FailedError, self).__init__(E_FAILED)


class InvalidParamError(OpenTMFError):
    """"""

    def __init__(self):
        super(InvalidParamError, self).__init__(E_INVALID_PARAM)


class InvalidURLError(OpenTMFError):
    """"""

    def __init__(self):
        super(InvalidURLError, self).__init__(E_INVALID_URL)
