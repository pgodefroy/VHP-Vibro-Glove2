import serial
import time
import argparse

class VibroGloveController:
    def __init__(self, port, baudrate=115200):
        """Initialize serial connection to the device"""
        self.ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Wait for connection to establish
        
    def send_command(self, command):
        """Send a command and wait for response"""
        self.ser.write(f"{command}\n".encode())
        return self.ser.readline().decode().strip()
        
    def close(self):
        """Close the serial connection"""
        self.ser.close()

def main():
    parser = argparse.ArgumentParser(description='Control Vibro Glove via Serial')
    parser.add_argument('port', help='Serial port (e.g. COM3 or /dev/ttyACM0)')
    parser.add_argument('command', choices=['start', 'stop', 'status'], 
                       help='Command to send')
    
    args = parser.parse_args()
    
    try:
        controller = VibroGloveController(args.port)
        response = controller.send_command(args.command)
        print(f"Response: {response}")
        controller.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
