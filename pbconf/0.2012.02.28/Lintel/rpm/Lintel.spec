#
# (c) Copyright 2012, Hewlett-Packard Development Company, LP
#
#  See the file named COPYING for license details
#
#
# SPEC file for Lintel
#
Name:           Lintel
Version:        PBVER
URL:            http://tesla.hpl.hp.com/opensource.html
Source:         %{name}-%{version}.tar.gz
# TODO-package-reviewer: can we have a no-release package?  We'll do a Lintel re-release on packaging glitches
Release:        1
Summary:        Support tools and library 
Group:          Development/Libraries
License:        BSD
Packager:	Lintel-Users <lintel-users@lists.sourceforge.net>
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc-c++, libstdc++-devel
BuildRequires: boost-devel, doxygen, sg3_utils, gnuplot, perl-DBI, libxml2-devel
BuildRequires: PBNONSTANDARD
BuildRequires: PBPERL
BuildRequires: PBNETPBM
BuildRequires: PBOPENSSH
BuildRequires: PBTEX

# TODO-package-reviewer: do we split shared libraries as in debian?
%package	libs
Summary:        Lintel library files
Group:          Development/Libraries
License:        BSD

%package	devel
Summary:        Lintel devel files
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}
Requires:       boost-devel, libxml2-devel
License:        BSD

%package	utils
Summary:        Lintel utilities
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}, perl-Lintel
#if-fedora Requires: ghostscript, tetex-dvips, tetex-latex
#if-centos Requires: ghostscript, tetex-dvips, tetex-latex
#if-scilinux Requires: ghostscript, tetex-dvips, tetex-latex
#if-opensuse Requires: ghostscript-library, texlive-latex
License:        BSD

# TODO-package-reviewer: how do we make this package architecture independent?
%package	docs
Summary:        Lintel development files documentation
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}
License:        BSD

%package        -n perl-Lintel
Summary:        Lintel perl files
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}
License:        BSD

%description
This is the meta-package for Lintel, the -{libs,devel,utils,docs,perl} sub-packages contain
the actual contents.

__DESCRIPTION_liblintel-dev__

%description	libs
The redhat packaging combinds the two Lintel C++ libraries into a single
package.

libLintel: PBDESC_liblintel

libLintelPThread: PBDESC_liblintelpthread

%description	devel
PBDESC_liblintel_dev

%description    utils
PBDESC_lintel_utils

%description    docs
PBDESC_liblintel_dev_doc

%description    -n perl-Lintel
PBDESC_liblintel_perl

%prep
%setup -q

%build
mkdir rpm-build
cd rpm-build
cmake -D CMAKE_INSTALL_PREFIX=/usr ..
make -j 6
ctest

%install
cd rpm-build
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
pwd
../dist/fix-install.sh $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/Lintel-%{version}
cp ../Release.info ../ChangeLog ../COPYING $RPM_BUILD_ROOT%{_docdir}/Lintel-%{version}
# TODO: can we make cmake automatically figure out that centos wants libs in /usr/lib64
if [ %{_libdir} != /usr/lib ]; then
        mkdir -p $RPM_BUILD_ROOT%{_libdir}
        mv $RPM_BUILD_ROOT/usr/lib/libLintel*so* $RPM_BUILD_ROOT%{_libdir}
fi
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/Lintel-devel
cat >$RPM_BUILD_ROOT/usr/share/doc/Lintel-devel/README <<EOF 
__DESCRIPTION_liblintel-dev__
EOF

strip $RPM_BUILD_ROOT/usr/lib/perl5/libLintelPerl.so
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/perl-Lintel
cat >$RPM_BUILD_ROOT/usr/share/doc/perl-Lintel/README <<EOF 
__DESCRIPTION_liblintel-perl__
EOF

strip $RPM_BUILD_ROOT/usr/bin/drawRandomLogNormal
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/Lintel-utils
cat >$RPM_BUILD_ROOT/usr/share/doc/Lintel-utils/README <<EOF 
__DESCRIPTION_lintel-utils__
EOF

strip $RPM_BUILD_ROOT/usr/lib*/libLintel*.so.*.*

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT rpm-build

# rpmlint complains about libLintel calling exit(), but that's intentional; 
# libLintel includes the equivalent of assert().
%files libs
%{_libdir}/libLintel.so.*
%{_libdir}/libLintelPThread.so.*
%{_docdir}/Lintel-%{version}/COPYING
%{_docdir}/Lintel-%{version}/Release.info

%files devel
%{_includedir}/Lintel/*
%{_bindir}/lintel-config
%{_libdir}/libLintel*.so
/usr/share/cmake*/Modules
/usr/share/packaging/redhat-rules
/usr/share/lintel-latex-rebuild
/usr/share/Lintel/doxygen.config.in
/usr/share/doc/Lintel-devel

%files utils
%{_bindir}/batch-parallel
%{_bindir}/deptool
%{_bindir}/drawRandomLogNormal
%{_bindir}/lintel-disktool
%{_bindir}/lintel-flock
%{_bindir}/lintel-latex-rebuild
%{_bindir}/mercury-plot
/usr/share/bp_modules/BatchParallel
/usr/share/doc/Lintel-utils
/usr/share/man/man1/*

# rpmlint complains about the manpages being compressed with gz instead of bz2,
# but all of the centos5 manpages are compressed with gz
%files docs
/usr/share/man/man3/*
/usr/share/doc/Lintel
%{_docdir}/Lintel-%{version}/ChangeLog

%files -n perl-Lintel
/usr/lib/perl5
/usr/share/perl5
/usr/share/doc/perl-Lintel

%changelog

* Tue Feb 28 2012 anderse@hpl.hp.com 0.2012.02.28-1
- release testing

* Mon Jun 13 2011 anderse@hpl.hp.com 0.2011.06.13-1
- Release.  See NEWS for major changes.

* Fri Mar 25 2011 anderse@hpl.hp.com 0.2011.03.12-1
- Initial rpm packaging.

