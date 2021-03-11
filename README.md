# yum packaging libnvidia nscq

[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT-license)
[![Contributing](https://img.shields.io/badge/Contributing-Developer%20Certificate%20of%20Origin-violet)](https://developercertificate.org)

## Overview

Packaging templates for `yum`, `dnf`, and `zypper` based Linux distros to build libnvidia-nscq packages.

NVIDIA NVSwitch Configuration and Query (NSCQ) library provides a stable driver API used by [DCGM](https://github.com/NVIDIA/DCGM) for monitoring NVSwitch devices.

> _note:_ the version of libnvidia-nscq must match the NVIDIA driver installed.

## Table of Contents

- [Overview](#Overview)
- [Deliverables](#Deliverables)
- [Installation](#Installation)
- [Prerequisites](#Prerequisites)
  * [Clone this git repository](#Clone-this-git-repository)
  * [Install build dependencies](#Install-build-dependencies)
- [Related](#Related)
  * [Fabric Manager](#Fabric-Manager)
  * [NVIDIA driver](#NVIDIA-driver)
- [Contributing](#Contributing)


## Deliverables

This repo contains the `.spec` file used to build the following **RPM** packages:


> _note:_ `XXX` is the first `.` delimited field in the driver version, ex: `460` in `460.32.03`

```shell
libnvidia-nscq-XXX
```


## Installation

* **RHEL8** or **Fedora** streams: `XXX`, `XXX-dkms`, `latest`, and `latest-dkms`

  The NvSwitch modularity profile (`fm`) installs all of the NVIDIA driver packages, as well as Fabric Manager and NCSQ

  ```shell
  dnf module install nvidia-driver:${stream}/fm
  ```

* **RHEL7**

  ```shell
  yum install libnvidia-nscq-XXX
  ```

* **openSUSE15** or **SLES15**

  ```shell
  zypper install libnvidia-nscq-XXX
  ```


## Prerequisites

### Clone this git repository:

Supported branches: `main`

```shell
git clone https://github.com/NVIDIA/yum-packaging-libnvidia-nscq
```

### Download a NSCQ library tarball:

* TBD

  *ex:* libnvidia-nscq-460.32.03.tar.gz

### Install build dependencies
> *note:* these are only needed for building not installation

```shell
# Packaging
yum install rpm-build
```

## Related

### Fabric Manager

- fabricmanager
  * [https://github.com/NVIDIA/yum-packaging-fabric-manager](https://github.com/NVIDIA/yum-packaging-fabric-manager)

### NVIDIA driver

- nvidia-driver
  * [https://github.com/NVIDIA/yum-packaging-nvidia-driver](https://github.com/NVIDIA/yum-packaging-nvidia-driver)


## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)
