## Dome daemon

`domed` communicates with the Astrohaven dome controller (PLC or legacy) attached via RS232 adaptor, and with the [dome heartbeat monitor](https://github.com/rockit-astro/dome-heartbeat-monitor) attached via USB.  Control is exposed via Pyro.

`dome` is a commandline utility that interfaces with the dome daemon.

Note that due to limitations in the serial protocol from the PLC there may be odd behaviours if the PLC buttons are used together with the dome daemon.
For example, when using the hand panel the dome status will only report "Partially Open" and never "Open" because the daemon is not informed when the limits are reached.
The serial commands may also conflict with the button commands, leading to conflicts and possible freezes. It is recommended to use one or the other, and never mix them.

### Configuration

Configuration is read from json files that are installed by default to `/etc/domed`.
A configuration file is specified when launching the dome server, and the `dome` frontend will search this location when launched.

```python
{
  "daemon": "onemetre_dome", # Run the server as this daemon. Daemon types are registered in `rockit.common.daemons`.
  "log_name": "onemetre_dome", # The name to use when writing messages to the observatory log.
  "control_machines": ["OneMetreDome", "OneMetreTCS"], # Machine names that are allowed to control (rather than just query) state. Machine names are registered in `rockit.common.IP`.
  "serial_port": "/dev/dome", # Serial FIFO for communicating with the dome PLC
  "serial_baud": 9600, # Serial baud rate (always 9600)
  "serial_timeout": 3, # Serial comms timeout
  "command_delay": 0.5, # Delay between sending individual open/close steps
  "step_command_delay": 2.0, # Delay between sending "slow_open_steps" 
  "shutter_timeout": 60, # Maximum time for opening or closing the dome
  "has_legacy_controller": false, # Use legacy (pre-PLC) serial protocol
  "has_bumper_guard": false, # Send bumper guard reset command before attempting to move the shutters
  "slow_open_steps": 0, # Number of slow jerking steps to use when first opening, to reduce belt slack on the 5 shutter domes
  "heartbeat_port": "/dev/dome-monitor", # USB FIFO for communicating with the dome heartbeat monitor
  "heartbeat_baud": 9600, # Baud rate (always 9600)
  "heartbeat_timeout": 3, # USB comms timeout
  "sides": { # Mapping from side names to the PLC a/b sides.
    "east": "a",
    "west": "b",
    "both": "ab"
  },
  "side_labels": { # Human-readable labels forthe PLC a/b sides
    "a": " East",
    "b": " West"
  },
  "invert_on_close": true, # Invert ab to ba (or vice versa) when using a "close both" command
  "domealert_daemon": "onemetre_domealert", # [optional] Domealert daemon to check belt tension when opening
  "domealert_belt_sensors": { # [optional] Domealert sensor names for the belt tension on each side
    "a": "east_belt_tensioned",
    "b": "west_belt_tensioned"
  }
}
```

The FIFO device names are defined in the .rules files installed through the `-dome-data` rpm packages.
If the physical serial port or USB adaptors change these should be updated to match.

### Initial Installation

The automated packaging scripts will push 6 RPM packages to the observatory package repository:

| Package                   | Description                                                               |
|---------------------------|---------------------------------------------------------------------------|
| rockit-dome-server        | Contains the `domed` server and systemd service file.                     |
| rockit-dome-client        | Contains the `dome` commandline utility for controlling the dome server.  |
| rockit-dome-data-onemetre | Contains the json configuration and udev rules for the W1m.               |
| rockit-dome-data-clasp    | Contains the json configuration and udev rules for the CLASP telescope.   |
| rockit-dome-data-sting    | Contains the json configuration and udev rules for the STING telescope.   |
| python3-rockit-dome       | Contains the python module with shared code.                              |

After installing packages, the systemd service should be enabled:

```
sudo systemctl enable --now domed@<config>
```

where `config` is the name of the json file for the appropriate telescope.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `rockit.common.daemons` for the daemon specified in the dome config.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl restart domed@<config>
```

### Testing Locally

The dome server and client can be run directly from a git clone:
```
./domed config/onemetre.json
DOMED_CONFIG_PATH=./config/onemetre.json ./dome status
```
