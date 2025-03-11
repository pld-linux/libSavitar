Summary:	C++ implementation of 3mf loading with SIP Python bindings
Summary(pl.UTF-8):	Implementacja C++ ładowania 3mf w wiązaniami Pythona SIP
Name:		libSavitar
# keep in sync with CuraEngine, cura, libArgus, python3-Uranium
Version:	4.13.2
Release:	2
License:	AGPL v3+
Group:		Libraries
#Source0Download: https://github.com/Ultimaker/libSavitar/tags
Source0:	https://github.com/Ultimaker/libSavitar/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	25e943379dbe7f3fc0e6ca55318ab1b0
Patch0:		no-pugixml.patch
Patch1:		system-pugixml.patch
URL:		https://github.com/Ultimaker/libSavitar
BuildRequires:	cmake >= 3.8
# C++17
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	pugixml-devel
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-sip-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Savitar is a C++ implementation of 3mf loading with SIP Python
bindings. 3mf is a 3D printing file format.

%description -l pl.UTF-8
Savitar to zaimplementowane w C++ ładowanie formatu 3mf z wiązaniami
Pythona SIP. 3mf to format plików do wydruków 3D.

%package devel
Summary:	Development files for libSavitar
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libSavitar
# The cmake scripts are BSD
License:	AGPL v3+ and BSD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:7

%description devel
Savitar is a C++ implementation of 3mf loading with SIP Python
bindings. 3mf is a 3D printing file format.

Development files.

%description devel -l pl.UTF-8
Savitar to zaimplementowane w C++ ładowanie formatu 3mf z wiązaniami
Pythona SIP. 3mf to format plików do wydruków 3D.

Ten pakiet zawiera pliki programistyczne.

%package -n python3-savitar
Summary:	Python 3 libSavitar bindings
Summary(pl.UTF-8):	Wiązania Pythona 3 do biblioteki libSavitar
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-savitar
Savitar is a C++ implementation of 3mf loading with SIP Python
bindings. 3mf is a 3D printing file format.

The Python bindings.

%description -n python3-savitar -l pl.UTF-8
Savitar to zaimplementowane w C++ ładowanie formatu 3mf z wiązaniami
Pythona SIP. 3mf to format plików do wydruków 3D.

Ten pakiet zawiera wiązania Pythona.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

%build
mkdir build
cd build
%cmake .. \
	-DCMAKE_SKIP_RPATH:BOOL=ON
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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
