Summary:	Tk interface for CVS
Summary(pl):	Interfejs Tk dla CVS
Name:		tkcvs
Version:	7.0.3
%define tar_version	7_03
Release:	1
License:	GPL
Group:		Development/Version Control
Source0:	http://www.twobarleycorns.net/%{name}-%{tar_version}.tar.gz
Patch0:		%{name}-EDITOR.patch
URL:		http://www.twobarleycorns.net/tkcvs.html
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

./doinstall.tcl -finallib %{_libdir} $RPM_BUILD_ROOT%{_prefix}

# install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/tkcvs/bitmaps,%{_mandir}/mann}
# install tkcvs/cvscheck.blank $RPM_BUILD_ROOT%{_bindir}/cvscheck
# install tkcvs/tkcvs.blank    $RPM_BUILD_ROOT%{_bindir}/tkcvs
# install tkcvs/*.tcl          $RPM_BUILD_ROOT%{_libdir}/tkcvs
# install tkcvs/tclIndex       $RPM_BUILD_ROOT%{_libdir}/tkcvs
# install bitmaps/*            $RPM_BUILD_ROOT%{_libdir}/tkcvs/bitmaps
# install tkdiff/tkdiff.blank  $RPM_BUILD_ROOT%{_bindir}/tkdiff
# install tkdiff/*.n           $RPM_BUILD_ROOT%{_mandir}/mann
# install tkcvs/*.n            $RPM_BUILD_ROOT%{_mandir}/mann

gzip -9nf README.tkcvs CHANGELOG FAQ tkcvs/vendor.readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz tkcvs/*gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/tkcvs
%{_mandir}/man?/*
