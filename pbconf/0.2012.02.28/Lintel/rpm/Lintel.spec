#
# $Id$
#
# Used if virtual name != real name (perl, ...) - replace hash by percent in the below line
#define srcname	PBPKG

Summary:        PBSUMMARY
Summary(fr):    french bla-bla

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

%description -l fr
french desc

%prep
%setup -q
# Used if virtual name != real name (perl, ...)
#%setup -q -n %{srcname}-%{version}
#PBPATCHCMD

%build
%configure
make %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog
%doc INSTALL COPYING README AUTHORS NEWS

%changelog
PBLOG

