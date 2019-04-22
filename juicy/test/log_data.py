import sys
import time
#import json
from mpu9250.mpu9250 import mpu9250


if __name__ == "__main__":

     # Initialize sensor with external library class.
    sensor = mpu9250()
    log_file = open(str(int(round(time.time()*1000))) + '_juicy.log', 'w')
    log_file.write('time,ax,ay,az,gx,gy,gy\n')

    # Main loop.
    while True:

        movement = sensor.accel
        orientation = sensor.gyro

        line = str(int(round(time.time()*1000)))
        line = line + ',{accel[0]},{accel[1]},{accel[2]}'.format(accel=movement)
        line = line + ',{gyro[0]},{gyro[1]},{gyro[2]}'.format(gyro=orientation)
        line = line + '\n'

        log_file.write(line)
        time.sleep(0.01)
        # Make url request every WAIT_TIME seconds.
        if (time.time() - last_send_time) > SEND_DELAY:
            # Send bulk update, clear measurement buffer, and update timing information.
            print("Sending measurement buffer of size " + str(len(measurement_buffer)))
            # Flush logs for journalctl
            sys.stdout.flush()
            bulk_update_channel(measurement_buffer)
            measurement_buffer = []
            last_send_time = time.time()
