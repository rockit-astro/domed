#
# This file is part of domed.
#
# domed is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# domed is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with domed.  If not, see <http://www.gnu.org/licenses/>.

"""Helper function to validate and parse the json config file"""

# pylint: disable=too-many-instance-attributes

import json
from warwick.observatory.common import daemons, IP, validation

CONFIG_SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'required': [
        'daemon', 'log_name', 'control_machines', 'serial_port', 'serial_baud', 'serial_timeout', 'command_delay',
        'step_command_delay', 'shutter_timeout', 'has_legacy_controller', 'has_bumper_guard', 'slow_open_steps',
        'heartbeat_port', 'heartbeat_baud', 'heartbeat_timeout', 'sides', 'side_labels', 'invert_on_close'
    ],
    'properties': {
        'daemon': {
            'type': 'string',
            'daemon_name': True
        },
        'log_name': {
            'type': 'string'
        },
        'control_machines': {
            'type': 'array',
            'items': {
                'type': 'string',
                'machine_name': True
            }
        },
        'serial_port': {
            'type': 'string'
        },
        'serial_baud': {
            'type': 'integer',
            'minimum': 0
        },
        'serial_timeout': {
            'type': 'number',
            'minimum': 0
        },
        'command_delay': {
            'type': 'number',
            'minimum': 0
        },
        'step_command_delay': {
            'type': 'number',
            'minimum': 0
        },
        'shutter_timeout': {
            'type': 'number',
            'minimum': 0
        },
        'has_legacy_controller': {
            'type': 'boolean'
        },
        'has_bumper_guard': {
            'type': 'boolean'
        },
        'slow_open_steps': {
            'type': 'integer',
            'minimum': 0
        },
        'heartbeat_port': {
            'type': 'string'
        },
        'heartbeat_baud': {
            'type': 'integer',
            'minimum': 0
        },
        'heartbeat_timeout': {
            'type': 'number',
            'minimum': 0
        },
        'sides': {
            'type': 'object',
            'additionalProperties': {
                'type': 'string'
            }
        },
        'side_labels': {
            'type': 'object',
            'required': ['a', 'b'],
            'properties': {
                'a': {
                    'type': 'string'
                },
                'b': {
                    'type': 'string'
                }
            }
        },
        'invert_on_close': {
            'type': 'boolean'
        },
        'domealert_daemon': {
            'type': 'string',
            'daemon_name': True
        },
        'domealert_belt_sensors': {
            'type': 'object',
            'properties': {
                'a': {
                    'type': 'string'
                },
                'b': {
                    'type': 'string'
                }
            }
        }
    }
}


class Config:
    """Daemon configuration parsed from a json file"""
    def __init__(self, config_filename):
        # Will throw on file not found or invalid json
        with open(config_filename, 'r') as config_file:
            config_json = json.load(config_file)

        # Will throw on schema violations
        validation.validate_config(config_json, CONFIG_SCHEMA, {
            'daemon_name': validation.daemon_name_validator,
            'directory_path': validation.directory_path_validator,
        })

        self.daemon = getattr(daemons, config_json['daemon'])
        self.log_name = config_json['log_name']
        self.control_ips = [getattr(IP, machine) for machine in config_json['control_machines']]
        self.serial_port = config_json['serial_port']
        self.serial_baud = config_json['serial_baud']
        self.serial_timeout_seconds = config_json['serial_timeout']
        self.command_delay_seconds = config_json['command_delay']
        self.step_command_delay_seconds = config_json['step_command_delay']
        self.shutter_timeout_seconds = config_json['shutter_timeout']
        self.legacy_controller = config_json['has_legacy_controller']
        self.heartbeat_port = config_json['heartbeat_port']
        self.heartbeat_baud = config_json['heartbeat_baud']
        self.heartbeat_timeout_seconds = config_json['heartbeat_timeout']
        self.slow_open_steps = config_json['slow_open_steps']
        self.has_bumper_guard = config_json['has_bumper_guard']
        self.sides = config_json['sides']
        self.side_labels = config_json['side_labels']
        self.invert_on_close = config_json['invert_on_close']

        self.domealert_daemon = None
        self.domealert_belt_sensors = {
            'a': None,
            'b': None
        }

        if 'domealert_daemon' in config_json:
            self.domealert_daemon = getattr(daemons, config_json['domealert_daemon'])
            if 'domealert_belt_sensors' in config_json:
                for side in ['a', 'b']:
                    self.domealert_belt_sensors[side] = config_json['domealert_belt_sensors'].get(side, None)
