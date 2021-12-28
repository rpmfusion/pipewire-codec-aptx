%global spaversion   0.2

%global pipewire_version 0.3.42

Name:           pipewire-codec-aptx
Summary:        PipeWire Bluetooth aptX codec plugin
Version:        %{pipewire_version}
Release:        1%{?dist}
License:        MIT
URL:            https://pipewire.org/
Source0:        https://gitlab.freedesktop.org/pipewire/pipewire/-/archive/%{version}/pipewire-%{version}.tar.gz

BuildRequires:  meson >= 0.49.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  sbc-devel
BuildRequires:  libfreeaptx-devel

Requires:       pipewire >= %{pipewire_version}

%description
PipeWire media server Bluetooth aptX codec plugin.

%prep
%autosetup -p1 -n pipewire-%{version}

%build
%meson  --auto-features=disabled -D examples=disabled \
          -D bluez5=enabled -D bluez5-codec-aptx=enabled \
          -D session-managers=[]
%meson_build spa-codec-bluez5-aptx

%install
mkdir -p %{buildroot}%{_libdir}/spa-%{spaversion}/bluez5
install -pm 0755 %{_vpath_builddir}/spa/plugins/bluez5/libspa-codec-bluez5-aptx.so \
   %{buildroot}%{_libdir}/spa-%{spaversion}/bluez5/

%files
%license COPYING
%{_libdir}/spa-%{spaversion}/bluez5/libspa-codec-bluez5-aptx.so

%changelog
* Tue Dec 28 2021 Gergely Gombos <gombosg@disroot.org> - 0.3.42-1
- Bump Pipewire version

* Tue Dec 28 2021 Gergely Gombos <gombosg@disroot.org> - 0.3.40-1
- Bump Pipewire version

* Wed Sep 22 2021 Gergely Gombos <gombosg@disroot.org> - 0.3.36-3
- Review fixes

* Tue Sep 21 2021 Gergely Gombos <gombosg@disroot.org> - 0.3.36-2
- Initial packaging

* Thu Sep 16 2021 Pauli Virtanen <pav@iki.fi> - 0.3.36-1
- Initial version (kudos!)
