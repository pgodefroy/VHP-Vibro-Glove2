
import serial
import time

class VibroGloveController:
    def __init__(self, port='/dev/ttyACM0', baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Wait for connection to establish
        
    def start_stream(self):
        self.ser.write(b'start\n')
        return self.ser.readline().decode().strip()
        
    def stop_stream(self):
        self.ser.write(b'stop\n')
        return self.ser.readline().decode().strip()
        
    def get_status(self):
        self.ser.write(b'status\n')
        # Read multiple lines if needed for full status
        return self.ser.readline().decode().strip()
        
    def close(self):
        self.ser.close()

# Example usage
if __name__ == "__main__":
    controller = VibroGloveController()
    
    print("Starting stream...")
    print(controller.start_stream())
    time.sleep(5)
    
    print("Stopping stream...")
    print(controller.stop_stream())
    
    print("Current status:")
    print(controller.get_status())
    
    controller.close()
