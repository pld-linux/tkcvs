Summary:	Tk interface for CVS
Summary(pl):	Interfejs Tk dla CVS
Name:		tkcvs
Version:	7.0.3
%define tar_version	7_03
Release:	2
License:	GPL
Group:		Development/Version Control
Source0:	http://www.twobarleycorns.net/%{name}-%{tar_version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-EDITOR.patch
URL:		http://www.twobarleycorns.net/tkcvs.html
Icon:		tkcvs.xpm
Requires:	cvs
Requires:	rcs
Requires:	tcl
Requires:	tk >= 8.1
BuildRequires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Tk interface for CVS.

%description -l pl
Interfejs Tk dla CVS.

%prep
%setup -q -n %{name}-%{tar_version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Development,%{_pixmapsdir}}

./doinstall.tcl -finallib %{_libdir} $RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development/tkcvs.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README.tkcvs CHANGELOG FAQ tkcvs/vendor.readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz tkcvs/*gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/tkcvs
%{_mandir}/man?/*
%{_applnkdir}/Development/tkcvs.desktop
%{_pixmapsdir}/tkcvs.png
