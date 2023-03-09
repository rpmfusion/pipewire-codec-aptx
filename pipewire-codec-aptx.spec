%global spaversion   0.2

%global pipewire_version 0.3.67

Name:           pipewire-codec-aptx
Summary:        PipeWire Bluetooth aptX codec plugin
Version:        %{pipewire_version}
Release:        1%{?dist}
License:        MIT
URL:            https://pipewire.org/
Source0:        https://gitlab.freedesktop.org/pipewire/pipewire/-/archive/%{version}/pipewire-%{version}.tar.gz

BuildRequires:  meson >= 0.59.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0)
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
* Thu Mar 09 2023 Leigh Scott <leigh123linux@gmail.com> - 0.3.67-1
- Bump Pipewire version

* Sat Feb 11 2023 Leigh Scott <leigh123linux@gmail.com> - 0.3.65-1
- Bump Pipewire version

* Sat Dec 17 2022 Leigh Scott <leigh123linux@gmail.com> - 0.3.63-1
- Bump Pipewire version

* Sat Nov 12 2022 Leigh Scott <leigh123linux@gmail.com> - 0.3.60-1
- Bump Pipewire version

* Wed Oct 05 2022 Leigh Scott <leigh123linux@gmail.com> - 0.3.59-1
- Bump Pipewire version

* Sat Sep 17 2022 Leigh Scott <leigh123linux@gmail.com> - 0.3.58-1
- Bump Pipewire version

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.3.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Aug 04 2022 Leigh Scott <leigh123linux@gmail.com> - 0.3.56-1
- Bump Pipewire version

* Mon Jul 04 2022 Leigh Scott <leigh123linux@gmail.com> - 0.3.53-1
- Bump Pipewire version

* Tue Apr 05 2022 Leigh Scott <leigh123linux@gmail.com> - 0.3.49-1
- Bump Pipewire version

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.3.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

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
