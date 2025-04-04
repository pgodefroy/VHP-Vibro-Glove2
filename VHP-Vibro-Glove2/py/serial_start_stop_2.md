0. Implementation Notes

Baud Rate: Make sure the baud rate in the Python script matches what's set in your Arduino code (default is usually 115200).

Error Handling: The Python script includes basic error handling through the serial responses.

Thread Safety: If you're using this in a multi-threaded environment, you may want to add mutex protection around the stream control functions.

Port Name: The Python script assumes /dev/ttyACM0 as the port name - adjust this for your system (Windows would use something like COM3).

Existing Functionality: This implementation reuses the existing StartStream(), StopStream(), and SendStatus() functions, so it maintains compatibility with the other control methods.

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
