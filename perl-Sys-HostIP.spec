%define realname   Sys-HostIP

Name:		perl-%{realname}
Version:    1.3.1
Release: %mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Perl module to get ip address related info
Source0:    http://search.cpan.org/CPAN/authors/id/B/BL/BLUELINES//%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/~bluelines/%{realname}
BuildRequires:	perl-devel
BuildArch:      noarch

%description
Sys::HostIP does what it can to determine the ip address of your machine.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README 
%{perl_vendorlib}/*
%{_mandir}/man3/*
