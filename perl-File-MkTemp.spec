%include	/usr/lib/rpm/macros.perl
Summary:	File-MkTemp perl module
Summary(pl):	Modu³ perla File-MkTemp
Name:		perl-File-MkTemp
Version:	1.0.5
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-MkTemp-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-MkTemp - Make temporary filename from template. 

%description -l pl
File-MkTemp umo¿liwia tworzenie pliku tymczasowego na podstawie szablonu.

%prep
%setup -q -n File-MkTemp-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/File
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz

%{perl_sitelib}/File/MkTemp.pm
%{perl_sitearch}/auto/File/.packlist

%{_mandir}/man3/*
