%include	/usr/lib/rpm/macros.perl
Summary:	File-MkTemp perl module
Summary(pl):	Modu³ perla File-MkTemp
Name:		perl-File-MkTemp
Version:	1.0.6
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-MkTemp-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-MkTemp - Make temporary filename from template.

%description -l pl
File-MkTemp umo¿liwia tworzenie pliku tymczasowego na podstawie
szablonu.

%prep
%setup -q -n File-MkTemp-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/File/MkTemp.pm
%{_mandir}/man3/*
