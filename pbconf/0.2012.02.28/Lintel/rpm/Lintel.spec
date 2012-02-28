#
# $Id$
#
# Used if virtual name != real name (perl, ...) - replace hash by percent in the below line
#define srcname	PBPKG

Summary:        Support tools and library

Name:           PBREALPKG
Version:        PBVER
Release:        PBTAGPBSUF
License:        PBLIC
Group:          PBGRP
Url:            PBURL
Source:         PBREPO/PBSRC
#PBPATCHSRC
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
#Requires:       PBDEP

%description
PBDESC

%prep
%setup -q
# Used if virtual name != real name (perl, ...)
#%setup -q -n %{srcname}-%{version}
#PBPATCHCMD

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
../debian/fix-install.sh $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/Lintel-%{version}
cp ../Release.info ../Changelog.mtn ../COPYING $RPM_BUILD_ROOT%{_docdir}/Lintel-%{version}
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
./redhat/rules clean

%files
%defattr(-,root,root)
%doc ChangeLog
%doc INSTALL COPYING README AUTHORS NEWS

%changelog
PBLOG

