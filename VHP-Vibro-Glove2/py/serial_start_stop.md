Command Protocol
The serial protocol is simple text-based:

start - Starts the stream

stop - Stops the stream

status - Requests current status

Each command should be followed by a newline character (\n).

Implementation Notes

Baud Rate: Make sure the baud rate in the Python script matches what's set in your Arduino code (default is usually 115200).

Error Handling: The Python script includes basic error handling through the serial responses.

Thread Safety: If you're using this in a multi-threaded environment, you may want to add mutex protection around the stream control functions.

Port Name: The Python script assumes /dev/ttyACM0 as the port name - adjust this for your system (Windows would use something like COM3).

Existing Functionality: This implementation reuses the existing StartStream(), StopStream(), and SendStatus() functions, so it maintains compatibility with the other control methods.
