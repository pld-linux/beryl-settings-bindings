Summary:	Bindings to beryl settings library
Summary(pl.UTF-8):	Dowiązania do biblioteki beryl settings
Name:		beryl-settings-bindings
Version:	0.2.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	dc3d35b7d2e53cc5fa6905e26ff194f3
URL:		http://beryl-project.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	beryl-core-devel >= 1:%{version}
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	python-Pyrex
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	xorg-lib-libX11-devel
%pyrequires_eq	python-libs
Requires:	beryl-core >= 1:%{version}
Requires:	glib2 >= 1:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bindings to beryl settings library.

%description -l pl.UTF-8
Dowiązania do biblioteki beryl settings.

%package devel
Summary:	Development files for beryl settings bindings
Summary(pl.UTF-8):	Pliki programistyczne dowiązań do biblioteki beryl settings
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Development files for beryl settings bindings.

%description devel -l pl.UTF-8
Pliki programistyczne dowiązań do biblioteki beryl settings.

%prep
%setup -q
echo '#beryl version header' > VERSION
echo VERSION=%{version} >> VERSION

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON=%{__python} \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/berylsettings.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/berylsettings.so

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/beryl-settings-bindings.pc
