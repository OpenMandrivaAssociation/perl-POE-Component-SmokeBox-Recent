%define upstream_name    POE-Component-SmokeBox-Recent
%define upstream_version 1.30

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    An extremely minimal HTTP client
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CPAN::Recent::Uploads)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Date)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(Net::IP)
BuildRequires: perl(POE)
BuildRequires: perl(POE::Component::Client::DNS)
BuildRequires: perl(POE::Filter::HTTP::Parser)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::POE::Client::TCP)
BuildRequires: perl(Test::POE::Server::TCP)
BuildRequires: perl(URI)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


