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

    _colors = {
        0: 'red',
        1: 'green',
        2: 'cyan',
        3: 'yellow',
        4: 'yellow',
        5: 'red'
    }

    @classmethod
    def label(cls, status, formatting=False):
        """
        Returns a human readable string describing a status
        Set formatting=true to enable terminal formatting characters
        """
        if formatting:
            if status in cls._labels and status in cls._colors:
                return f'[b][{cls._colors[status]}]{cls._labels[status]}[/{cls._colors[status]}][/b]'
            return '[b][red]UNKNOWN[/red][/b]'

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

    _colors = {
        0: 'default',
        1: 'green',
        2: 'red',
        3: 'red',
        4: 'yellow',
    }

    @classmethod
    def label(cls, status, formatting=False):
        """
        Returns a human readable string describing a status
        Set formatting=true to enable terminal formatting characters
        """
        if formatting:
            if status in cls._labels and status in cls._colors:
                return f'[b][{cls._colors[status]}]{cls._labels[status]}[/{cls._colors[status]}][/b]'
            return '[b][red]UNKNOWN[/red][/b]'

        if status in cls._labels:
            return cls._labels[status]
        return 'UNKNOWN'
