Name:       wayland-protocols

Summary:    Wayland protocols that adds functionality not available in the core protocol
Version:    1.41.0
Release:    1
License:    MIT
URL:        http://wayland.freedesktop.org/
Source0:    wayland-protocols-%{version}.tar.xz
BuildArch:     noarch
BuildRequires: meson
BuildRequires: pkgconfig(wayland-scanner)

%description
This package contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%package devel
Summary:        Wayland protocols that adds functionality not available in the core protocol

%description devel
This package contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%prep
%autosetup -n %{name}-%{version}/wayland-protocols

%build
%meson

%meson_build

%install
%meson_install

%files devel
%license COPYING
%doc README.md
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/
%{_includedir}/%{name}/
