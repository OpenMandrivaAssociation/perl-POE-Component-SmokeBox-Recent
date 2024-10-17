%define upstream_name    POE-Component-SmokeBox-Recent
%define upstream_version 1.32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	An extremely minimal HTTP client
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CPAN::Recent::Uploads)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(Net::IP)
BuildRequires:	perl(POE)
BuildRequires:	perl(POE::Component::Client::DNS)
BuildRequires:	perl(POE::Filter::HTTP::Parser)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::POE::Client::TCP)
BuildRequires:	perl(Test::POE::Server::TCP)
BuildRequires:	perl(URI)
Requires:	perl(POE::Component::Client::DNS)
Requires:	perl(Test::POE::Client::TCP)
Requires:	perl(CPAN::Recent::Uploads)
BuildArch:	noarch

%description
POE::Component::SmokeBox::Recent is a the POE manpage component for
retrieving recently uploaded CPAN distributions from the CPAN mirror of
your choice.

It accepts a url and an event name and attempts to download and parse the
RECENT file from that given url.

It is part of the SmokeBox toolkit for building CPAN Smoke testing
frameworks.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
export PERL_MM_USE_DEFAULT=1
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.320.0-1mdv2011.0
+ Revision: 688826
- update to new version 1.32

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 1.300.0-4
+ Revision: 658249
- more runtime req
- add runtime req

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.300.0-2
+ Revision: 657459
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.300.0-1
+ Revision: 643454
- update to new version 1.30

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 1.280.0-3mdv2011.0
+ Revision: 625065
- Add Net::IP to the build requries
- Add the export PERL_MM_USE_DEFAULT=1
- import perl-POE-Component-SmokeBox-Recent

