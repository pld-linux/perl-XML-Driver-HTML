#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Driver-HTML
Summary:	XML::Driver::HTML - SAX Driver for non wellformed HTML
Summary(pl):	XML::Driver::HTML - sterownik SAX dla niekoniecznie dobrze sformu�owanego HTML-a
Name:		perl-XML-Driver-HTML
Version:	0.06
Release:	3
# (c) 2001 GNU General Public License
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	43f29d0060b4e22687ed91e651f0addb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Parser >= 3.07
BuildRequires:	perl-HTML-Tree	 >= 2.96
BuildRequires:	perl-XML-Handler-YAWriter >= 0.20
BuildRequires:	perl-libxml >= 0.06
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Driver::HTML is a SAX Driver for HTML. There is no need for the
HTML input to be well formed, as XML::Driver::HTML is generating its
SAX events by walking a HTML::TreeBuilder object. The simplest kind of
use, is a filter from HTML to XHTML using XML::Handler::YAWriter as a
SAX Handler.

%description -l pl
XML::Driver::HTML to sterownik SAX dla HTML-a. Nie wymaga on, aby
wej�cie w HTML-u by�o dobrze sformu�owane, jako �e XML::Driver::HTML
generuje zdarzenia SAX w�druj�c po obiekcie HTML::TreeBuilder.
Najprostszym zastosowaniem jest filtr z HTML-a do XHTML-a przy u�yciu
modu�u XML::Handler::YAWriter jako procedury obs�ugi SAX.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/XML/Driver
%{perl_vendorlib}/XML/Driver/*.pm
%{_mandir}/man?/*
