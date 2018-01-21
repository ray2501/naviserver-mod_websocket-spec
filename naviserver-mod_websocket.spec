#
# spec file for package naviserver websocket module
#

Summary:        NaviServer websocket module
Name:           naviserver-mod_websocket
Version:        0.1
Release:        0
License:        MPL-1.1
Group:          Productivity/Networking/Web/Servers
Url:            http://bitbucket.org/naviserver/websocket
BuildRequires:  make
BuildRequires:  naviserver
BuildRequires:  naviserver-devel
Requires:       naviserver
Requires:       nsf
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a NaviServer module that implements WebSockets for NaviServer
and provides an API for for it.

%prep
%setup -q %{name}-%{version}

%build

%install
mkdir -p %buildroot/var/lib/naviserver/tcl/websocket
make DESTDIR=%buildroot install NAVISERVER=/var/lib/naviserver

%clean
rm -rf %buildroot

%files
%defattr(-,nsadmin,nsadmin,-)
/var/lib/naviserver/tcl/websocket

%changelog

