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
- [Building Manually](#Building-Manually)
- [Related](#Related)
  * [Fabric Manager](#Fabric-Manager)
  * [NVIDIA driver](#NVIDIA-driver)
- [See also](#See-also)
  * [Debian](#Debian)
- [Contributing](#Contributing)


## Deliverables

This repo contains the `.spec` file used to build the following **RPM** packages:


> _note:_ `XXX` is the first `.` delimited field in the driver version, ex: `460` in `460.32.03`

```shell
- libnvidia-nscq-XXX
> ex: libnvidia-nscq-460-460.32.03-1.x86_64.rpm
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

### Download a NSCQ tarball:

* https://developer.download.nvidia.com/compute/cuda/redist/libnvidia_nscq/

  *ex:* libnvidia_nscq-linux-x86_64-460.32.03.tar.gz

### Install build dependencies
> *note:* these are only needed for building not installation

```shell
# objdump
yum install binutils
# Packaging
yum install rpm-build
```


## Building Manually

### Parse JSON to retrieve download URL
```shell
baseURL="https://developer.download.nvidia.com/compute/cuda/redist"
curl -s $baseURL/redistrib_460.32.03.json | \
jq -r '."libnvidia_nscq" | ."460.32.03" | ."linux-x86_64"' | \
sed "s|^|$baseURL/|"
```

### Prepare build directory
```shell
cd yum-packaging-libnvidia-nscq
mkdir SPECS SOURCES
cp *.spec SPECS/
cp ../libnvidia_nscq*.tar.gz SOURCES/
```

### Check API version
```shell
tar -tvf SOURCES/libnvidia_nscq*.tar.gz | \
    grep ^l | awk '{print $(NF-2)}' | grep ".so." | \
    sort -uVr | awk -F ".so." '{print $2}' | awk NR==1
> 1.1
```

### Check SONAME
```shell
tar --strip-components=1 -xf ../libnvidia_nscq*.tar.gz libnvidia_nscq/libnvidia-nscq.so.[4-9][0-9][0-9]*
objdump -p libnvidia-nscq.so.[4-9][0-9][0-9]* | grep SONAME | awk -F ".so." '{print $2}'
> 1
```

### Generate .rpm packages
```shell
rpmbuild \
    --define "%_topdir $(pwd)" \
    --define "%version 460.32.03" \
    --define "%branch 460" \
    --define "%so_api 1.1" \
    --define "%SONAME 1" \
    --define "%_arch x86_64" \
    --define "%_build_arch x86_64" \
    --target=x86_64 \
    -v -ba SPECS/*.spec

cd RPMS/x86_64
ls *.rpm
```
> _note:_ branch is the first `.` delimited field in the driver version, ex: `460` in `460.32.03`


## Related

### Fabric Manager

- fabricmanager
  * [https://github.com/NVIDIA/yum-packaging-fabric-manager](https://github.com/NVIDIA/yum-packaging-fabric-manager)

### NVIDIA driver

- nvidia-driver
  * [https://github.com/NVIDIA/yum-packaging-nvidia-driver](https://github.com/NVIDIA/yum-packaging-nvidia-driver)


## See also

### Debian

  * [https://github.com/NVIDIA/apt-packaging-libnvidia-nscq](https://github.com/NVIDIA/apt-packaging-libnvidia-nscq)


## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)
