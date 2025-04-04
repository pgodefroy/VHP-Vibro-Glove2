1. Finding Your Serial Port
Windows:

Look in Device Manager under "Ports (COM & LPT)"

Typically named COM3, COM4, etc.

Linux/macOS:

Run ls /dev/tty* in terminal

Typically named /dev/ttyACM0 or /dev/ttyUSB0

2. Running Commands
Basic commands:

bash

# Start vibration sequence
python serial_start_stop_2.py COM3 start

# Stop vibration sequence
python serial_start_stop_2.py COM3 stop

# Get current status
python serial_start_stop_2.py COM3 status

Replace COM3 with your actual port name.
