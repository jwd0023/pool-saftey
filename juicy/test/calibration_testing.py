import os
import numpy as np

import RPi.GPIO as GPIO
from mpu9250.mpu9250 import mpu9250
from juicy.signal_processing.sensor_calibration import SensorModel

if __name__ == "__main__":

    # Initialize sensor with external library class.
    sensor = mpu9250()

    # Setup GPIO modes and initial values.
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(18, GPIO.IN)
    GPIO.output(12, 0)

    # Initialize first magnitude to 10 - this was it won't trigger immediately every time...
    last_mag = 10

    # Initialize sensor model that calibrates system to some degree.
    sensor_model = SensorModel()

    # Main loop.
    while True:

        # Get sensor data.
        sensor_accel = sensor.accel
        sensor_gyro  = np.asarray(sensor.gyro)

        # Threshold gyro to eliminate error.
        sensor_gyro[sensor_gyro < 10] = 0

        # Get estimated "true" accelerometer measurement from model.
        sensor_model.update_state(sensor_gyro)
        cal_accel = sensor_model.convert_accelerometer_measurement(sensor_accel)

        # Clear console before printing new information.
        os.system('clear')

        # Print sensor data and the magnitude of the acceleration.
        next_mag     = np.linalg.norm(sensor_accel)
        next_cal_mag = np.linalg.norm(cal_accel)

        # Print uncalibrated measurement.
        print('Uncalibrated measurement: (%2.3f,%2.3f,%2.3f)    |    Magnitude = %2.3f'
              % (*sensor_accel, next_mag))

        # Print calibrated measurement.
        print('Calibrated measurement:   (%2.3f,%2.3f,%2.3f)    |    Magnitude = %2.3f'
              % (*cal_accel, next_cal_mag))

        # Print calibrated measurement.
        print('Gyroscope measurement:    (%2.3f,%2.3f,%2.3f)'
              % sensor_gyro)


        # Thresholding for alarm detection - uncomment else for software LED/alarm reset.
        if 1.4 * last_mag < next_mag:
            GPIO.output(12, 1)

        # Set the next value to compare.
        last_mag = next_mag

        # Allows LED to be reset by external input (currently button).
        if GPIO.input(18) == 1:
            GPIO.output(12, 0)
