# Get Started

## Usage

```py
mender = Mender(base_url = 'https://docker.mender.io/api/management/v1')

# List devices on page 1
devices = await mender.get_devices_paged(page=1)
print(devices)

# List all devices
async for device in mender.get_devices():
    print(device)

# Filter all devices by attributes
async for device in mender.get_devices(attributes={"hostname": 'xxx-ffffffffffff'}):
    print(device)
```

## Installation

Using pip:

```sh
pip install mender
```

Using pipenv:

```sh
pipenv install mender
```

## Deployment

```sh
pipenv run python3 setup.py sdist bdist_wheel
pipenv run twine upload dist/*
```

