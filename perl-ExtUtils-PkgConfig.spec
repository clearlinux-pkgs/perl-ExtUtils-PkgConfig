#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-ExtUtils-PkgConfig
Version  : 1.16
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/X/XA/XAOC/ExtUtils-PkgConfig-1.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/X/XA/XAOC/ExtUtils-PkgConfig-1.16.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : LGPL-2.1
Requires: perl-ExtUtils-PkgConfig-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
ExtUtils::PkgConfig - simplistic interface to pkg-config
SYNOPSIS
use ExtUtils::PkgConfig;

%package dev
Summary: dev components for the perl-ExtUtils-PkgConfig package.
Group: Development
Provides: perl-ExtUtils-PkgConfig-devel = %{version}-%{release}
Requires: perl-ExtUtils-PkgConfig = %{version}-%{release}

%description dev
dev components for the perl-ExtUtils-PkgConfig package.


%package perl
Summary: perl components for the perl-ExtUtils-PkgConfig package.
Group: Default
Requires: perl-ExtUtils-PkgConfig = %{version}-%{release}

%description perl
perl components for the perl-ExtUtils-PkgConfig package.


%prep
%setup -q -n ExtUtils-PkgConfig-1.16
cd %{_builddir}/ExtUtils-PkgConfig-1.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/ExtUtils::PkgConfig.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
