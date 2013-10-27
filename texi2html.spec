# NOTE: 5.0 is likely to be the last separate texi2html release (as merged into texinfo)
%include	/usr/lib/rpm/macros.perl
Summary:	texi2html is a Perl script that converts Texinfo files to HTML
Summary(hu.UTF-8):	texi2html egy Perl szkript, amely Texinfo fájlokat konvertál HTML-be
Summary(pl.UTF-8):	texi2html - skrypt Perla konwertujący pliki Texinfo do HTML-a
Name:		texi2html
Version:	5.0
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://download.savannah.gnu.org/releases/texi2html/%{name}-%{version}.tar.bz2
# Source0-md5:	f15ac876fcdc8be865b16535f480aa54
Patch0:		%{name}-info.patch
Patch1:		%{name}-perl.patch
URL:		http://www.nongnu.org/texi2html/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel >= 0.14
BuildRequires:	perl-Encode
BuildRequires:	perl-base
BuildRequires:	rpm-perlprov
BuildRequires:	texinfo
Requires:	perl-Unicode-EastAsianWidth
Requires:	perl-libintl
Requires:	texinfo >= 5.0
Suggests:	perl-Encode
Suggests:	perl-Text-Unidecode
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
texi2html is a Perl script that converts Texinfo files to HTML.

%description -l hu.UTF-8
texi2html egy Perl szkript, amely Texinfo fájlokat konvertál HTML-be.

%description -l pl.UTF-8
texi2html to skrypt Perla konwertujący pliki Texinfo do HTML-a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
cp -f po/Makefile.in.in po_document/
cp -f po/Makefile.in.in po_messages/
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-external-Unicode-EastAsianWidth \
	--with-external-libintl-perl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir

# only .us-ascii or base exists - merge them(?)
for d in $RPM_BUILD_ROOT%{_localedir}/*.us-ascii ; do
	outd=$RPM_BUILD_ROOT%{_localedir}/$(basename $d .us-ascii)/LC_MESSAGES
	install -d $outd
	%{__mv} $d/LC_MESSAGES/texi2html_document.mo $outd
done
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{no,nb}
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/texi2html
%{_datadir}/texi2html
%{_datadir}/texinfo/init/*.init
%dir %{_datadir}/texinfo/html
%doc %{_datadir}/texinfo/html/texi2html.html
%{_mandir}/man1/texi2html*
%{_infodir}/texi2html.info*
