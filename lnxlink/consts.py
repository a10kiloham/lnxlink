"""Constant variables to use"""

SERVICEHEADLESS = """[Unit]
Description=LNXlink
After=network-online.target

[Service]
Type=simple
Restart=always
RestartSec=5
User=root

ExecStart={exec_cmd}

[Install]
WantedBy=default.target
"""

SERVICEUSER = """[Unit]
Description=LNXlink
After=network-online.target multi-user.target graphical.target
PartOf=graphical-session.target

[Service]
Type=simple
Restart=always
RestartSec=5

ExecStart={exec_cmd}

[Install]
WantedBy=default.target
"""

CONFIGTEMP = """
mqtt:
  prefix: 'lnxlink'
  clientId: 'DESKTOP-Linux'
  server: '192.168.1.1'
  port: 1883
  auth:
    user: 'user'
    pass: 'pass'
    tls: false
    keyfile: ""
    certfile: ""
    ca_certs: ""
  discovery:
    enabled: true
  lwt:
    enabled: true
    qos: 1
    retain: false
update_interval: 5
hass_url:
hass_api:
modules:
custom_modules:
exclude:
  - audio_select
  - bash
  - battery
  - boot_select
  - brightness
  - fullscreen
  - gpio
  - gpu
  - idle
  - inference_time
  - keep_alive
  - keyboard_hotkeys
  - media
  - mouse
  - network
  - notify
  - power_profile
  - screen_onoff
  - screenshot
  - send_keys
  - speech_recognition
  - systemd
  - webcam
  - xdg_open
settings:
  systemd:
  gpio:
    inputs:
    outputs:
  hotkeys:
  disk_usage:
    include_disks: []
    exclude_disks: []
  statistics: "https://analyzer.bkbilly.workers.dev"
  bash:
    expose:
  mounts:
    autocheck: false
    directories: []
"""
