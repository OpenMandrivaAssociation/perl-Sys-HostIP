%define upstream_name    Sys-HostIP
%define upstream_version 1.7

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl module to get ip address related info
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/~bluelines/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/B/BL/BLUELINES//%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Sys::HostIP does what it can to determine the ip address of your machine.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
