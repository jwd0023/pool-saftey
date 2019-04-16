# Installation
## Enable Hardware
```bash
raspi-config
```
Make sure I2C is enabled under Interfaces Options -> I2C

## Dependencies
```bash
apt install -y git neovim python-venv i2ctools
git clone https://github.com/pool-saftey/pool-saftey.git
python3 -m venv ~/venvs/juicy
source ~/venvs/juicy/bin/activate
# Hack because of mpu9250 
pip install build_utils
pip3 install -r juicy/requirments.txt
```

## Verifying Installation
```bash
cd juicy
source ~/venvs/juicy/bin/activate
python3 -m juicy.test.accelerometer_test
```

## Installing Data Collection Service
Using the srv folder as an example (make sure you have permissions)
```bash
cd /srv/
git clone https://github.com/pool-saftey/pool-saftey.git
cd ./pool-saftey
python3 -m venv ./service_env
./service_env/bin/pip install build_utils
./service_env/bin/pip3 install -r requirments.txt
ln -s pool-saftey.service /etc/systemd/system/
# Check that the service installed
systemd-analyze verify pool-saftey.service
# Start service
systemctl start pool-saftey.service
# Tell service to start on boot
systemctl enable pool-saftey.service
```
[Then go to the dashboard][1]

# Manual Data Collection
```bash
cd juicy
source ~/venvs/juicy/bin/activate
python3 -m juicy.test.log_data
```
[Then go to the dashboard][1]

[1]: thingspeak.com/channels/753579

