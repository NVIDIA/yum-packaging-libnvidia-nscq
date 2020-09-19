%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:       libnvidia-nscq-%{major}
Version:    %{version}
Release:    1
Summary:    NVSwitch Configuration and Query library
License:    NVIDIA Proprietary
URL:        http://nvidia.com
Source:     %{pkg_folder}.tar.gz
#AutoReq:    0

Provides:   libnvidia-nscq
Provides:   nscq%{SONAME} = %{so_api}
Provides:   nscq-api = %{so_api}

%description
NVIDIA NVSwitch Configuration and Query (NSCQ) library provides a
stable driver API used by DCGM for monitoring NVSwitch devices.

%post -n libnvidia-nscq-%{major} -p /sbin/ldconfig

%postun -n libnvidia-nscq-%{major} -p /sbin/ldconfig

%prep
%setup -c

#%build

%install
export DONT_STRIP=1
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}
cp -R -a %{pkg_folder}/* %{buildroot}/%{_libdir}

%files
#%license LICENSE
%{_libdir}/libnvidia-nscq.so
%{_libdir}/libnvidia-nscq.so.1
%{_libdir}/libnvidia-nscq.so.1.*
%{_libdir}/libnvidia-nscq.so.*
