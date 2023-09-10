#
# This file is part of the Robotic Observatory Control Kit (rockit)
#
# rockit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rockit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rockit.  If not, see <http://www.gnu.org/licenses/>.

"""Constants and status codes used by domed"""

from rockit.common import TFmt


class CommandStatus:
    """Numeric return codes"""
    # General error codes
    Succeeded = 0
    Failed = 1
    Blocked = 2
    HeartbeatTimedOut = 3
    HeartbeatCloseInProgress = 4
    HeartbeatUnavailable = 5
    HeartbeatInvalidTimeout = 6
    EngineeringModeRequiresHeartbeatDisabled = 7
    EngineeringModeActive = 8
    InvalidControlIP = 10

    _messages = {
        # General error codes
        1: 'error: command failed',
        2: 'error: another command is already running',
        10: 'error: command not accepted from this IP',

        # dome specific codes
        3: 'error: heartbeat monitor has tripped',
        4: 'error: heartbeat monitor is closing the dome',
        5: 'error: heartbeat monitor is not available',
        6: 'error: heartbeat timeout must be less than 120s',
        7: 'error: heartbeat monitor must be disabled before enabling engineering mode',
        8: 'error: dome is in engineering mode',

        -100: 'error: terminated by user',
        -101: 'error: unable to communicate with dome daemon'
    }

    @classmethod
    def message(cls, error_code):
        """Returns a human readable string describing an error code"""
        if error_code in cls._messages:
            return cls._messages[error_code]
        return f'error: Unknown error code {error_code}'


class DomeShutterStatus:
    """Status of the dome shutters"""
    Closed, Open, PartiallyOpen, Opening, Closing, HeartbeatMonitorForceClosing = range(6)

    _labels = {
        0: 'CLOSED',
        1: 'OPEN',
        2: 'PARTIALLY OPEN',
        3: 'OPENING',
        4: 'CLOSING',
        5: 'FORCE CLOSING',
    }

    _formats = {
        0: TFmt.Red + TFmt.Bold,
        1: TFmt.Green + TFmt.Bold,
        2: TFmt.Cyan + TFmt.Bold,
        3: TFmt.Yellow + TFmt.Bold,
        4: TFmt.Yellow + TFmt.Bold,
        5: TFmt.Red + TFmt.Bold,
    }

    @classmethod
    def label(cls, status, formatting=False):
        """
        Returns a human readable string describing a status
        Set formatting=true to enable terminal formatting characters
        """
        if formatting:
            if status in cls._formats and status in cls._formats:
                return cls._formats[status] + cls._labels[status] + TFmt.Clear
            return TFmt.Red + TFmt.Bold + 'UNKNOWN' + TFmt.Clear

        if status in cls._labels:
            return cls._labels[status]
        return 'UNKNOWN'


class DomeHeartbeatStatus:
    """Status of the dome heartbeat monitoring"""
    Disabled, Active, TrippedClosing, TrippedIdle, Unavailable = range(5)

    _labels = {
        0: 'DISABLED',
        1: 'ACTIVE',
        2: 'CLOSING DOME',
        3: 'TRIPPED',
        4: 'UNAVAILABLE',
    }

    _formats = {
        0: TFmt.Bold,
        1: TFmt.Green + TFmt.Bold,
        2: TFmt.Red + TFmt.Bold,
        3: TFmt.Red + TFmt.Bold,
        4: TFmt.Yellow + TFmt.Bold,
    }

    @classmethod
    def label(cls, status, formatting=False):
        """
        Returns a human readable string describing a status
        Set formatting=true to enable terminal formatting characters
        """
        if formatting:
            if status in cls._formats and status in cls._formats:
                return cls._formats[status] + cls._labels[status] + TFmt.Clear
            return TFmt.Red + TFmt.Bold + 'UNKNOWN' + TFmt.Clear

        if status in cls._labels:
            return cls._labels[status]
        return 'UNKNOWN'
