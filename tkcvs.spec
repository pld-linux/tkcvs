Summary:	Tk interface for CVS
Summary(pl):	Interfejs Tk dla CVS
Name:		tkcvs
Version:	6.0
Release:	3
Copyright:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Kontrola Wersji
Source:		ftp://ftp.neosoft.com/pub/tcl/code/%{name}-%{version}.tar.gz
Patch:		tkcvs-paths.patch
Requires:	cvs
Requires:	rcs
Requires:	nedit
Requires:	tcl
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch

%description
Tk interface for CVS

%description -l pl
Interfejs Tk dla CVS

%prep
%setup -q
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,lib/tkcvs/bitmaps,man/mann}
install tkcvs/cvscheck.blank $RPM_BUILD_ROOT/usr/X11R6/bin/cvscheck
install tkcvs/tkcvs.blank    $RPM_BUILD_ROOT/usr/X11R6/bin/tkcvs
install tkcvs/*.tcl          $RPM_BUILD_ROOT/usr/X11R6/lib/tkcvs
install tkcvs/tclIndex       $RPM_BUILD_ROOT/usr/X11R6/lib/tkcvs
install bitmaps/*            $RPM_BUILD_ROOT/usr/X11R6/lib/tkcvs/bitmaps
install tkdiff/tkdiff.blank  $RPM_BUILD_ROOT/usr/X11R6/bin/tkdiff
install tkdiff/*.n           $RPM_BUILD_ROOT/usr/X11R6/man/mann
install tkcvs/*.n            $RPM_BUILD_ROOT/usr/X11R6/man/mann

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/mann/* \
	tkcvs.README README.tkcvs tkdiff/README tkcvs/vendor.readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz tkdiff/*gz tkcvs/*gz

%attr(755,root,root) /usr/X11R6/bin/*

/usr/X11R6/lib/tkcvs
/usr/X11R6/man/mann/*

%changelog
* Thu Mar 25 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [6.0-3]
- removed man group from man pages,
- added "Requires: tcl",
- removed Requires (autogenerate).

* Wed Dec 23 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- initial rpm release
