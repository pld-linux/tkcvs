Summary:	Tk interface for CVS
Summary(pl):	Interfejs Tk dla CVS
Name:		tkcvs
Version:	7.0.2
Release:	1
License:	GPL
Group:		Development/Version Control
Group(de):	Entwicklung/Versionkontrolle
Group(pl):	Programowanie/Zarz±dzanie wersjami
Source0:	http://www.twobarleys.net/%{name}-%{version}.tar.gz
URL:		http://www.twobarleys.net/tkcvs.html
Requires:	cvs
Requires:	rcs
Requires:	nedit
Requires:	tcl

BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Tk interface for CVS.

%description -l pl
Interfejs Tk dla CVS.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
./doinstall.tcl -nox $RPM_BUILD_ROOT%{_prefix}
perl -i -p -e 's/^(set TclRoot )\/.*$/\1\/usr\/X11R6\/lib\;/g' \
	$RPM_BUILD_ROOT%{_bindir}/tkcvs

gzip -9nf  COPYING FAQ README.tkcvs CHANGELOG INSTALL README.windows tkdiff/COPYING tkdiff/PATCHES tkcvs/vendor.readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz tkdiff/*gz tkcvs/*gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/tkcvs
%{_mandir}/mann/*
