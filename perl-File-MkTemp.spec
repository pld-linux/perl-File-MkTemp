#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	MkTemp
Summary:	File::MkTemp - make temporary filename from template
Summary(pl.UTF-8):	File::MkTemp - tworzenie tymczasowych nazw plików z szablonów
Name:		perl-File-MkTemp
Version:	1.0.6
Release:	9
License:	free
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	23bcfab64d97595c89938665038a9fe2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::MkTemp Perl module makes temporary filename from template.

%description -l pl.UTF-8
Moduł Perla File::MkTemp umożliwia tworzenie pliku tymczasowego na
podstawie szablonu.

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
%doc CHANGES README
%{perl_vendorlib}/File/MkTemp.pm
%{_mandir}/man3/*
