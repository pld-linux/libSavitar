Summary:	C++ implementation of 3mf loading with SIP Python bindings
Name:		libSavitar
Version:	2.7.0
Release:	3
License:	AGPLv3+
Group:		Libraries
Source0:	https://github.com/Ultimaker/libSavitar/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	584cd4f3dacdcdbe69edcd42b83a4c6c
Patch0:		no-pugixml.patch
Patch1:		system-pugixml.patch
Patch2:		lib-suffix.patch
Patch3:		PyQt5-sip.patch
URL:		https://github.com/Ultimaker/libSavitar
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	pugixml-devel
BuildRequires:	python3-devel
BuildRequires:	python3-sip-devel
BuildRequires:	sip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Savitar is a C++ implementation of 3mf loading with SIP Python
bindings. 3mf is a 3D printing file format.

%package devel
# The cmake scripts are BSD
Summary:	Development files for libsavitar
License:	AGPLv3+ and BSD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Savitar is a C++ implementation of 3mf loading with SIP Python
bindings. 3mf is a 3D printing file format.

Development files.

%package -n python3-savitar
Summary:	Python 3 libSavitar bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-savitar
Savitar is a C++ implementation of 3mf loading with SIP Python
bindings. 3mf is a 3D printing file format.

The Python bindings.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
mkdir build
cd build
%{cmake} .. \
	-DCMAKE_SKIP_RPATH:BOOL=ON
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libSavitar.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSavitar.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSavitar.so
%{_includedir}/Savitar
%{_libdir}/cmake/Savitar

%files -n python3-savitar
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{py3_sitedir}/Savitar.so
