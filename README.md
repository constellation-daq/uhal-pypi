# uHAL PyPI Distribution

[![PyPI - Version](https://img.shields.io/pypi/v/uhal)](https://pypi.org/project/uhal/)
[![PyPI - Python Versions](https://img.shields.io/pypi/pyversions/uhal)](https://pypi.org/project/uhal/#files)

This project provides an easy way to install the uHAL Python API from the [IPbus software](https://github.com/ipbus/ipbus-software) via [PyPI](https://pypi.org/).
This vastly simplies the installation, which is notoriously hard to get right especially with virtual environments.

## Installation

The uHAL component can be installed via:

```sh
pip install uhal
```

Binary releases are available for Linux. Other platforms are not supported by IPbus.

## Building ControlHub

While this project focuses on the install of the uHAL Python API, building the ControlHub is another challenge itself.
However, since the uHAL part is now not required anymore, the installation can be done in an Erlang container.

First, the IPbus software repository needs to be cloned:

```sh
git clone --depth=1 -b v2.8.22 https://github.com/ipbus/ipbus-software.git
```

Then an Erlang container with the IPbus software mounted needs to be started via docker or podman:

```sh
docker run -v $(pwd)/ipbus-software:/ipbus-software -it erlang:26 /bin/bash
```

Inside the container, a build of the ControlHub can be achieved with the `Set` variable:

```sh
cd ipbus-software
make Set=controlhub
```

Finally after exiting the container, the ControlHub can be installed on the host:

```sh
cd ipbus-software
sudo make Set=controlhub install
```

## Developer Notes

### Adding new Python Versions

Since uHAL is a C++ library at its core, binaries for each Python version need to compiled separately.
Thus if a new Python version is released, a new upload to PyPI is required.
For this reason, and additional number is added to the IPbus version in `meson.build` which allows to create a new tag without needing a new IPbus version.

The new Python version needs to be added in `pyproject.toml` and `.github/workflows/wheels.yml`.
Once a corresponding tag is created in the repository, a new version is uploaded to PyPI automatically.

### Updating the IPbus Software

When updating the IPbus software, the version needs to updated manually in the following places:

- everything in `ipbus-software.wrap`
- the project version in `meson.build`
- the project version in `subprojects/packagefiles/ipbus-software/meson.build`
- the git tag mentioned in the README

Additionally it is worth checking if:

- any of the other subprojects have a new version released
- a newer Erlang version can be used to compile ControlHub
