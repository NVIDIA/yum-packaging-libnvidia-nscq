# The MIT License (MIT)
# 
# Copyright (c) 2020 NVIDIA Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:       libnvidia-nscq-%{branch}
Version:    %{version}
Release:    1
Summary:    NVSwitch Configuration and Query library
License:    NVIDIA Proprietary
URL:        http://nvidia.com
Source:     libnvidia_nscq-linux-%{_arch}-%{version}.tar.gz
#AutoReq:    0

Provides:   nscq%{SONAME} = %{so_api}
Provides:   nscq-api = %{so_api}
Provides:   libnvidia-nscq = %{version}
Obsoletes:  libnvidia-nscq < %{version}
Conflicts:  libnvidia-nscq

%description
NVIDIA NVSwitch Configuration and Query (NSCQ) library provides a
stable driver API used by DCGM for monitoring NVSwitch devices.

%post -n libnvidia-nscq-%{branch} -p /sbin/ldconfig

%postun -n libnvidia-nscq-%{branch} -p /sbin/ldconfig

%prep
%setup -q -n libnvidia_nscq

#%build

%install
export DONT_STRIP=1
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}
cp -R -a * %{buildroot}/%{_libdir}

%files
#%license LICENSE
%{_libdir}/libnvidia-nscq.so
%{_libdir}/libnvidia-nscq.so.1
%{_libdir}/libnvidia-nscq.so.1.*
%{_libdir}/libnvidia-nscq.so.*
