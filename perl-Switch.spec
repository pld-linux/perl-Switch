#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Switch
Summary:	Switch - a switch statement for Perl
Summary(pl):	Switch - instrukcja switch dla Perla
Name:		perl-%{pdir}
Version:	2.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/R/RG/RGARCIA/%{pdir}-%{version}.tar.gz
# Source0-md5:	29650eb2782955446c70ee4376f61066
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Switch.pm provides the syntax and semantics for an explicit case
mechanism for Perl.  The syntax is minimal, introducing only the
keywords "switch" and "case" and conforming to the general pattern of
existing Perl control structures.  The semantics are particularly
rich, allowing any one (or more) of nearly 30 forms of matching to be
used when comparing a switch value with its various cases.

%description -l pl
Switch.pm udostêpnia sk³adniê i semantykê dla jawnego mechanizmu
rozpatrywania przypadku dla Perla.  Sk³adnia jest minimalna, wprowadza
jedynie s³owa kluczowe ,,switch'' i ,,case'' i zachowuj±c zgodno¶æ
z ogólnym wzorcem istniej±cych procedur kontroli przep³ywu Perla.

%prep
%setup -q -n %{pdir}-%{version}

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
%doc Changes README
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
