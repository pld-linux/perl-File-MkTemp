%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	MkTemp
Summary:	File::MkTemp perl module
Summary(pl):	Modu³ perla File::MkTemp
Name:		perl-File-MkTemp
Version:	1.0.6
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::MkTemp - Make temporary filename from template.

%description -l pl
File::MkTemp umo¿liwia tworzenie pliku tymczasowego na podstawie
szablonu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_sitelib}/File/MkTemp.pm
%{_mandir}/man3/*
