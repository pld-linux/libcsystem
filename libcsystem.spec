Summary:	Library to support cross-platform C system functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje systemowe w C
Name:		libcsystem
Version:	20150101
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libcsystem/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	22ffa008d350a3279250238e2225723b
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libcsystem/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libclocale-devel >= 20120425
BuildRequires:	libcnotify-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libuna-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcerror >= 20120425
Requires:	libclocale >= 20120425
Requires:	libcnotify >= 20120425
Requires:	libcstring >= 20120425
Requires:	libuna >= 20120425
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcsystem is a library to support cross-platform C system functions.

%description -l pl.UTF-8
libcsystem to biblioteka wspierająca wieloplatformowe funkcje
systemowe w C.

%package devel
Summary:	Header files for libcsystem library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcsystem
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= 20120425
Requires:	libclocale-devel >= 20120425
Requires:	libcnotify-devel >= 20120425
Requires:	libcstring-devel >= 20120425
Requires:	libuna-devel >= 20120425

%description devel
Header files for libcsystem library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcsystem.

%package static
Summary:	Static libcsystem library
Summary(pl.UTF-8):	Statyczna biblioteka libcsystem
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcsystem library.

%description static -l pl.UTF-8
Statyczna biblioteka libcsystem.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcsystem.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcsystem.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcsystem.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcsystem.so
%{_includedir}/libcsystem
%{_includedir}/libcsystem.h
%{_pkgconfigdir}/libcsystem.pc
%{_mandir}/man3/libcsystem.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcsystem.a
