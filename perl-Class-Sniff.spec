%define upstream_name    Class-Sniff
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Look for class composition code smells
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(B::Concise)
BuildRequires: perl(Devel::Symdump)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Graph::Easy)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Sub::Information)
BuildRequires: perl(Test::Most)
BuildRequires: perl(Text::SimpleTable)
BuildRequires: perl(Tree)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
*ALPHA* code. You've been warned.

The interface is rather ad-hoc at the moment and is likely to change. After
creating a new instance, calling the 'report' method is your best option.
You can then visually examine it to look for potential problems:

 my $sniff = Class::Sniff->new({class => 'Some::Class'});
 print $sniff->report;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


