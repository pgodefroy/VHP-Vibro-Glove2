
import serial
import time
import cmd

class VibroShell(cmd.Cmd):
    intro = 'Vibro Glove Control Shell. Type help or ? to list commands.\n'
    prompt = '(vibro) '

    def __init__(self, port):
        super().__init__()
        self.device = serial.Serial(port, 115200, timeout=1)
        time.sleep(2)  # Connection settling time
        print(f"Connected to {port}")

    def do_start(self, arg):
        'Start the vibration sequence: start'
        self.device.write(b'start\n')
        print(self.device.readline().decode().strip())

    def do_stop(self, arg):
        'Stop the vibration sequence: stop'
        self.device.write(b'stop\n')
        print(self.device.readline().decode().strip())

    def do_status(self, arg):
        'Get device status: status'
        self.device.write(b'status\n')
        # Read multiple lines if needed
        print(self.device.readline().decode().strip())

    def do_exit(self, arg):
        'Exit the application: exit'
        self.device.close()
        print("Connection closed")
        return True

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <serial_port>")
        sys.exit(1)
    
    VibroShell(sys.argv[1]).cmdloop()
