# m4/libcerror.m4
%define		libcerror_ver	20120425
# m4/libclocale.m4
%define		libclocale_ver	20120425
# m4/libcnotify.m4
%define		libcnotify_ver	20120425
# m4/libcstring.m4
%define		libcstring_ver	20120425
# m4/libuna.m4
%define		libuna_ver	20120425
Summary:	Library to support cross-platform C system functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje systemowe w C
Name:		libcsystem
Version:	20150629
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libcsystem/releases
Source0:	https://github.com/libyal/libcsystem/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	0a4c89767cb52d26110097f894d81a8d
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libcsystem/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcstring-devel >= %{libcstring_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libcerror >= %{libcerror_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcstring >= %{libcstring_ver}
Requires:	libuna >= %{libuna_ver}
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
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libclocale-devel >= %{libclocale_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libcstring-devel >= %{libcstring_ver}
Requires:	libuna-devel >= %{libuna_ver}

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
