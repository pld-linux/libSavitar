%global commit 1ad7ddb202ec36f6b486b1f70279329ec0b8cc48
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global datestamp 20170501
%global relstring %{datestamp}git%{shortcommit}
Summary:	C++ implementation of 3mf loading with SIP Python bindings
Name:		libSavitar
Version:	0
Release:	0.1.%{relstring}
License:	AGPLv3+
Group:		Libraries
Source0:	https://github.com/Ultimaker/libSavitar/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# Source0-md5:	c9da107ed1e4f954b080258b7811c85e
Patch0:		no-pugixml.patch
Patch1:		lib-suffix.patch
Patch2:		system-pugixml.patch
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
%setup -q -n %{name}-%{commit}
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
