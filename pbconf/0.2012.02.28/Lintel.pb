#
# Project Builder configuration file
# For project Lintel
#
# $Id$
#

#
# What is the project URL
#
#pburl Lintel = svn://svn.Lintel.org/Lintel/devel
#pburl Lintel = svn://svn+ssh.Lintel.org/Lintel/devel
#pburl Lintel = cvs://cvs.Lintel.org/Lintel/devel
#pburl Lintel = http://www.Lintel.org/src/Lintel-devel.tar.gz
#pburl Lintel = ftp://ftp.Lintel.org/src/Lintel-devel.tar.gz
#pburl Lintel = file:///src/Lintel-devel.tar.gz
#pburl Lintel = dir:///src/Lintel-devel
pburl Lintel = file:///home/anderse/projects/Lintel-0.2012.02.28.tar.gz

# Repository
pbrepo Lintel = http://tesla.hpl.hp.com/opensource
#pbml Lintel = Lintel-announce@lists.Lintel.org
#pbsmtp Lintel = localhost

# Check whether project is well formed 
# when downloading from ftp/http/...
# (containing already a directory with the project-version name)
pbwf Lintel = 1

#
# Packager label
#
pbpackager Lintel = Eric Anderson <eric.anderson4@hp.com>
#

# For delivery to a machine by SSH (potentially the FTP server)
# Needs hostname, account and directory
#
#sshhost Lintel = www.Lintel.org
#sshlogin Lintel = bill
#sshdir Lintel = /Lintel/ftp
#sshport Lintel = 22

#
# For Virtual machines management
# Naming convention to follow: distribution name (as per ProjectBuilder::Distribution)
# followed by '-' and by release number
# followed by '-' and by architecture
# a .vmtype extension will be added to the resulting string
# a QEMU rhel-3-i286 here means that the VM will be named rhel-3-i386.qemu
#
#vmlist Lintel = mandrake-10.1-i386,mandrake-10.2-i386,mandriva-2006.0-i386,mandriva-2007.0-i386,mandriva-2007.1-i386,mandriva-2008.0-i386,redhat-7.3-i386,redhat-9-i386,fedora-4-i386,fedora-5-i386,fedora-6-i386,fedora-7-i386,fedora-8-i386,rhel-3-i386,rhel-4-i386,rhel-5-i386,suse-10.0-i386,suse-10.1-i386,suse-10.2-i386,suse-10.3-i386,sles-9-i386,sles-10-i386,gentoo-nover-i386,debian-3.1-i386,debian-4.0-i386,ubuntu-6.06-i386,ubuntu-7.04-i386,ubuntu-7.10-i386,mandriva-2007.0-x86_64,mandriva-2007.1-x86_64,mandriva-2008.0-x86_64,fedora-6-x86_64,fedora-7-x86_64,fedora-8-x86_64,rhel-4-x86_64,rhel-5-x86_64,suse-10.2-x86_64,suse-10.3-x86_64,sles-10-x86_64,gentoo-nover-x86_64,debian-4.0-x86_64,ubuntu-7.04-x86_64,ubuntu-7.10-x86_64,solaris-10-x86_64
#vmlist=debian-6.0-x86_64
vmlist Lintel = centos-5-i386

#
# Valid values for vmtype are
# qemu, (vmware, xen, ... TBD)
# vmtype Lintel = qemu

# Hash for VM stuff on vmtype
#vmntp default = pool.ntp.org

# We suppose we can commmunicate with the VM through SSH
#vmhost Lintel = localhost
#vmlogin Lintel = pb
#vmport Lintel = 2222

# Timeout to wait when VM is launched/stopped
#vmtmout default = 120

# per VMs needed paramaters
#vmopt Lintel = -m 384 -daemonize
#vmpath Lintel = /home/qemu
#vmsize Lintel = 5G

# 
# For Virtual environment management
# Naming convention to follow: distribution name (as per ProjectBuilder::Distribution)
# followed by '-' and by release number
# followed by '-' and by architecture
# a .vetype extension will be added to the resulting string
# a chroot rhel-3-i286 here means that the VE will be named rhel-3-i386.chroot
#
velist Lintel = debian-6.0-i386,debian-6.0-x86_64,debian-7.0-i386,debian-7.0-x86_64,ubuntu-8.04-i386,ubuntu-8.04-x86_64,ubuntu-11.10-i386,ubuntu-11.10-x86_64

# VE params
#vetype Lintel = chroot
#ventp default = pool.ntp.org
#velogin Lintel = pb
# vepath Lintel = /var/cache/rpmbootstrap
#rbsconf Lintel = /etc/mock
#verebuild Lintel = false

install_deps_hook ubuntu-8.04 = sudo apt-get -y --force-yes install texlive-latex-base; sudo perl -i.bak -ne 's/^(.ifnum.count..)65/${1}99/; print' /usr/share/texmf-texlive/tex/latex/base/latex.ltx; sudo dpkg --configure -a
#
# Global version/tag for the project
#
projver Lintel = 0.2012.02.28
projtag Lintel = 1

# Hash of valid version names

# Additional repository to add at build time
# addrepo centos-5-x86_64 = http://packages.sw.be/rpmforge-release/rpmforge-release-0.3.6-1.el5.rf.x86_64.rpm,ftp://ftp.project-builder.org/centos/5/pb.repo
# addrepo centos-5-x86_64 = http://packages.sw.be/rpmforge-release/rpmforge-release-0.3.6-1.el5.rf.x86_64.rpm,ftp://ftp.project-builder.org/centos/5/pb.repo
#version Lintel = devel,stable

# Is it a test version or a production version
testver Lintel = false
# Which upper target dir for delivery
delivery Lintel = production

# Additional repository to add at build time
# addrepo centos-5-x86_64 = http://packages.sw.be/rpmforge-release/rpmforge-release-0.3.6-1.el5.rf.x86_64.rpm,ftp://ftp.project-builder.org/centos/5/pb.repo
# addrepo centos-4-x86_64 = http://packages.sw.be/rpmforge-release/rpmforge-release-0.3.6-1.el4.rf.x86_64.rpm,ftp://ftp.project-builder.org/centos/4/pb.repo

# Adapt to your needs:
# Optional if you need to overwrite the global values above
#
#pkgver Lintel = stable
#pkgtag Lintel = 3
# Hash of default package/package directory
defpkgdir Lintel = Lintel-0.2012.02.28
# Hash of additional package/package directory
#extpkgdir minor-pkg = dir-minor-pkg

# List of files per pkg on which to apply filters
# Files are mentioned relatively to pbroot/defpkgdir
#filteredfiles Lintel = Makefile.PL,configure.in,install.sh,Lintel.8
#supfiles Lintel = Lintel.init

# For perl modules, names are different depending on distro
# Here perl-xxx for RPMs, libxxx-perl for debs, ...
# So the package name is indeed virtual
#namingtype Lintel = perl

sshhost Lintel = localhost
sshdir Lintel = /home/anderse/cache-project-builder/repos
