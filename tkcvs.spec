Summary:	Tk interface for CVS
Summary(pl):	Interfejs Tk dla CVS
Name:		tkcvs
Version:	6.0
Release:	3
License:	GPL
Group:		Development/Version Control
Group(de):	Entwicklung/Versionkontrolle
Group(pl):	Programowanie/Zarz±dzanie wersjami
Source0:	ftp://ftp.neosoft.com/pub/tcl/code/%{name}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Requires:	cvs
Requires:	rcs
Requires:	nedit
Requires:	tcl
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
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/tkcvs/bitmaps,%{_mandir}/mann}
install tkcvs/cvscheck.blank $RPM_BUILD_ROOT%{_bindir}/cvscheck
install tkcvs/tkcvs.blank    $RPM_BUILD_ROOT%{_bindir}/tkcvs
install tkcvs/*.tcl          $RPM_BUILD_ROOT%{_libdir}/tkcvs
install tkcvs/tclIndex       $RPM_BUILD_ROOT%{_libdir}/tkcvs
install bitmaps/*            $RPM_BUILD_ROOT%{_libdir}/tkcvs/bitmaps
install tkdiff/tkdiff.blank  $RPM_BUILD_ROOT%{_bindir}/tkdiff
install tkdiff/*.n           $RPM_BUILD_ROOT%{_mandir}/mann
install tkcvs/*.n            $RPM_BUILD_ROOT%{_mandir}/mann

gzip -9nf tkcvs.README README.tkcvs tkdiff/README tkcvs/vendor.readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz tkdiff/*gz tkcvs/*gz
%attr(755,root,root) {_bindir}/*
%{_libdir}/tkcvs
%{_mandir}/mann/*
