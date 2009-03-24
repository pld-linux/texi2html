Summary:	texi2html is a Perl script that converts Texinfo files to HTML
Summary(hu.UTF-8):	texi2html egy Perl szkript, amely Texinfo fájlokat konvertál HTML-be
Name:		texi2html
Version:	1.82
Release:	0.1
License:	GPL
Group:		Documentation
Source0:	http://ftp.cc.uoc.gr/mirrors/nongnu.org/texi2html/%{name}-%{version}.tar.bz2
# Source0-md5:	a8a9193c0ac1bec2f3ca7be40a5a82eb
URL:		http://www.nongnu.org/texi2html/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
texi2html is a Perl script that converts Texinfo files to HTML.

%description -l hu.UTF-8
texi2html egy Perl szkript, amely Texinfo fájlokat konvertál HTML-be.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/texi2html
%{_mandir}/man1/texi2html*
%{_datadir}/texi2html
%doc %{_datadir}/texinfo/html/texi2html.html
%doc %{_datadir}/info/texi2html*
