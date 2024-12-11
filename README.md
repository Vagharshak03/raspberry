# Project Setup and Run Instructions

Step 1: Clone the Git Repository
Firstly, clone the repository to your local machine using the following command:
        git clone repository-url

Secondly, Navigate into the project directory:

        cd project-directory

Step 2: Install Virtual Environment
Create a virtual environment to manage your project dependencies:
        python -m venv venv

Step 3: Activate the Virtual Environment
        source venv/bin/activate

Step 4: Install Requirements
Once the virtual environment is activated, install the project dependencies by running:
        pip freeze > requirements.txt
        pip install -r requirements.txt

This will install all the necessary Python packages.

Step 5. Run the Flask Application
Finally, start the Flask app with the following command:
        python3 main.py

# Sensor Data Collection with Raspberry Pi
This project involves the integration of three environmental sensors with a Raspberry Pi 3 to measure various environmental parameters. The sensors used are:

## BME289: Measures temperature, humidity, and barometric pressure.
## LTR390: Measures ambient light levels (lux).
## PMS5003: Measures particulate matter (PM2.5, PM10) concentration in the air.
These sensors are interfaced with the Raspberry Pi 3 and the sensor data is read using Python scripts. The project aims to read and process data from these sensors for further analysis or monitoring.

Project Overview
### The system connects to three sensors:

BME289 (Temperature, Humidity, Pressure):
Temperature: Measures the air temperature in degrees Celsius (°C).
Humidity: Measures relative humidity in percentage (%).
Pressure: Measures atmospheric pressure in hectopascals (hPa).
LTR390 (Ambient Light):
Measures ambient light intensity in lux (lx).
PMS5003 (Air Quality):
Measures particulate matter (PM2.5, PM10) concentration in µg/m³.
Hardware Setup
Raspberry Pi 3: Used as the microcontroller to read sensor data and process it.
BME289: Connected to the Raspberry Pi via I2C.
LTR390: Connected to the Raspberry Pi via I2C.
PMS5003: Connected via UART or serial communication.
Software Overview
The project utilizes Python to read data from the sensors. The following libraries are used:

## Python scripts are written to:
Initialize and configure the sensors.
Periodically read measurements.
Print or store the sensor data.

