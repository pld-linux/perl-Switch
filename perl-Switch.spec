%include	/usr/lib/rpm/macros.perl
%define	pdir	Switch
Summary:	Switch -- A switch statement for Perl
Summary(pl):	Switch -- instrukcja switch dla Perla
Name:		perl-%{pdir}
Version:	2.09
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/DCONWAY/%{pdir}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.005
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Switch.pm provides the syntax and semantics for an explicit case mechanism
for Perl.  The syntax is minimal, introducing only the keywords C<switch>
and C<case> and conforming to the general pattern of existing Perl
control structures.  The semantics are particularly rich, allowing any
one (or more) of nearly 30 forms of matching to be used when comparing
a switch value with its various cases.

%description -l pl
Switch.pm udostêpnia sk³adniê i semantykê dla jawnego mechanizmu
rozpatrywania przypadku dla Perla.  Sk³adnia jest minimalna, wprowadza
jedynie s³owa kluczowe ,,switch'' i ,,case'' i zachowuj±c zgodno¶æ
z ogólnym wzorcem istniej±cych procedur kontroli przep³ywu Perla.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/*.pm
%{_mandir}/man3/*
