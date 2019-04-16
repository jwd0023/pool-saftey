# Installation
## Enable Hardware
```bash
raspi-config
```
Make sure I2C is enabled under Interfaces Options -> I2C

## Dependencies
```bash
apt install -y git neovim python-venv i2ctools
git clone https://github.com/jwd0023/juicy.git
python3 -m venv ~/venvs/juicy
source ~/venvs/juicy/bin/activate
pip install build_utils
pip3 install -r juicy/requirments.txt
```

## Verifying Installation
```bash
cd juicy
source ~/venvs/juicy/bin/activate
python3 -m juicy.test.accelerometer_test
```

# Manual Data Collection
```bash
cd juicy
source ~/venvs/juicy/bin/activate
python3 -m juicy.test.log_data
```
[Then go to the dashboard][1]

[1]: thingspeak.com/channels/753579

