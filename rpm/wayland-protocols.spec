Name:       wayland-protocols

Summary:    Wayland protocols that adds functionality not available in the core protocol
Version:    1.14.0
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://wayland.freedesktop.org/
Source0:    wayland-protocols-%{version}.tar.xz
BuildRequires: pkgconfig(wayland-scanner)

%description
This package contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%package devel
Summary:        Wayland protocols that adds functionality not available in the core protocol
Group:          Development/Libraries/C and C++

%description devel
This package contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%prep
%setup -q -n %{name}-%{version}/wayland-protocols

%build
%reconfigure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files devel
%defattr(-,root,root,-)
%doc README COPYING
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/
