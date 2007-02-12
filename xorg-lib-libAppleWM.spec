Summary:	AppleWM extension library
Summary(pl.UTF-8):   Biblioteka rozszerzenia AppleWM
Name:		xorg-lib-libAppleWM
Version:	1.0.0
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/lib/libAppleWM-%{version}.tar.bz2
# Source0-md5:	48a403c45be2206ee900729ced3a0e62
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-applewmproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AppleWM extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia AppleWM.

%package devel
Summary:	Header files for AppleWM library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki AppleWM
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-applewmproto-devel

%description devel
AppleWM extension library.

This package contains the header files needed to develop programs that
use libAppleWM.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia AppleWM.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libAppleWM.

%package static
Summary:	Static AppleWM library
Summary(pl.UTF-8):   Biblioteka statyczna AppleWM
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
AppleWM extension library.

This package contains the static libAppleWM library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia AppleWM.

Pakiet zawiera statyczną bibliotekę libAppleWM.

%prep
%setup -q -n libAppleWM-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libAppleWM.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAppleWM.so
%{_libdir}/libAppleWM.la
%{_pkgconfigdir}/applewm.pc
%{_mandir}/man3/AppleWM.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libAppleWM.a