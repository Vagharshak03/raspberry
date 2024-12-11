import serial
import struct
import time

class PMS5003:
    def __init__(self, serial_port='/dev/ttyS0', baud_rate=9600):
        self.serial_port = serial_port
        self.baud_rate = baud_rate

    def read_pms_data(self):
        try:
            # Open the serial connection
            ser = serial.Serial(self.serial_port, self.baud_rate, timeout=3)
            
            # Wait for the sensor to initialize (just to be safe)
            time.sleep(2)
            
            # Send the "start measurement" command (header bytes)
            ser.write(b'\x42\x4D')  # Header for PMS5003
            ser.write(b'\xE2')      # Command to read the data

            # Wait for the data to be sent back
            time.sleep(1)

            # Read 32 bytes of data from the sensor
            data = ser.read(32)

            # Print the raw data for debugging
            print(f"Received data: {data}")

            # Check if we received exactly 32 bytes (valid response)
            if len(data) == 32:
                # Extract PM2.5 and PM10 values from the sensor's data response
                pm25 = struct.unpack('>H', data[10:12])[0]  # PM2.5 concentration (2 bytes)
                pm10 = struct.unpack('>H', data[12:14])[0]  # PM10 concentration (2 bytes)

                # Close the serial connection
                ser.close()
                
                return {"PM2.5": pm25, "PM10": pm10}
            else:
                ser.close()
                return {"error": "Invalid data received from PMS5003"}
        
        except serial.SerialException as e:
            # Handle serial port errors (e.g., sensor not connected)
            return {"error": f"Serial connection error: {e}"}
        except Exception as e:
            # Handle any other unforeseen errors
            return {"error": f"Unexpected error: {e}"}


