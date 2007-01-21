Summary:	bindings to beryl settings
Summary(pl):	dowi±zania do beryl settings
Name:		beryl-settings-bindings
Version:	0.1.99.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://releases.beryl-project.org/0.1.99.2/%{name}-%{version}.tar.bz2
# Source0-md5:	84a1ad03e0ba5bfed8a80e7e15c00f7d
URL:		http://beryl-project.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	beryl-core-devel >= 1:0.1.99.2
BuildRequires:	beryl-settings >= 1:0.1.99.2
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	python-Pyrex
Requires:	beryl-core >= 1:0.1.99.2
Requires:	beryl-plugins >= 1:0.1.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bindings to beryl settings.

%description -l pl
dowi±zania do beryl settings.

%prep
%setup -q
echo '#beryl version header' > VERSION
echo VERSION=0.1.99.2 > VERSION

%build
autoreconf -v --install
%configure \
	PYTHON=%{_bindir}/python \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{py_sitedir}/berylsettings.so
%{_pkgconfigdir}/beryl-settings-bindings.pc
%{py_sitedir}/berylsettings.a
