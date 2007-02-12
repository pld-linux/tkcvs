Summary:	Tk interface for CVS
Summary(pl.UTF-8):	Interfejs Tk dla CVS
Name:		tkcvs
Version:	7.2.1
%define tar_version	%(echo %{version} | tr . _)
Release:	2
License:	GPL
Group:		Development/Version Control
Source0:	http://www.twobarleycorns.net/%{name}_%{tar_version}.tar.gz
# Source0-md5:	a552cdccd7cde73eaa8a41294f499cfc
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-EDITOR.patch
URL:		http://www.twobarleycorns.net/tkcvs.html
BuildRequires:	perl-base
BuildRequires:	tcl
Requires:	cvs
Requires:	rcs
Requires:	tcl
Requires:	tk >= 8.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define _ulibdir /usr/lib

%description
TkCVS is a Tcl/Tk-based graphical interface to the CVS configuration
management system.  It displays the status of the files in the current
working directory, and provides buttons and menus to execute CVS commands
on the selected files.  TkDiff is included for browsing and merging your
changes.

%description -l pl.UTF-8
TkCVS jest opartym o Tcl/Tk graficznym interfejsem do systemu zarządzania
wersjami CVS. Program wyświetla stan plików w aktualnym katalogu roboczym,
potrafi wyświetlić historię wybranego pliku w postaci wykresu oraz pozwala
na wykonywanie poleceń CVS przy użyciu menu i guzików. W skład pakietu
wchodzi TkDiff - narzędzie do przeglądania i łączenia naniesionych
modyfikacji.

%prep
%setup -q -n %{name}_%{tar_version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_mandir}/man1}

./doinstall.tcl -nox -finallib %{_ulibdir} $RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install tkcvs/tkcvs.1 $RPM_BUILD_ROOT%{_mandir}/man1/tkcvs.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG FAQ vendor5readme.pdf
%attr(755,root,root) %{_bindir}/*
%{_ulibdir}/tkcvs
%{_desktopdir}/*.desktop
%{_pixmapsdir}/tkcvs.png
%{_mandir}/man1/*
