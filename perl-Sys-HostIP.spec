%define upstream_name    Sys-HostIP
%define upstream_version 1.81

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl module to get ip address related info
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/~bluelines/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BL/BLUELINES//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::TinyMocker)
BuildRequires:	perl(Test::Exception)
BuildArch:	noarch

%description
Sys::HostIP does what it can to determine the ip address of your machine.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc Changes README 
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.810.0-1mdv2011.0
+ Revision: 636230
- new version

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.700.0-1mdv2011.0
+ Revision: 596678
- update to 1.7

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.3.1-5mdv2010.0
+ Revision: 430547
- rebuild

* Thu Jul 03 2008 Michael Scherer <misc@mandriva.org> 1.3.1-4mdv2009.0
+ Revision: 230903
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 1.3.1-3mdv2008.0
+ Revision: 23837
- rebuild


* Tue Dec 27 2005 Michael Scherer <misc@mandriva.org> 1.3.1-2mdk
- Do not ship empty dir

* Wed Sep 21 2005 Michael Scherer <misc@mandriva.org> 1.3.1-1mdk
- First mandriva package

