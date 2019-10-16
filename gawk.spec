#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDF597815937EC0D2 (arnold@skeeve.com)
#
Name     : gawk
Version  : 5.0.1
Release  : 54
URL      : https://mirrors.kernel.org/gnu/gawk/gawk-5.0.1.tar.xz
Source0  : https://mirrors.kernel.org/gnu/gawk/gawk-5.0.1.tar.xz
Source1 : https://mirrors.kernel.org/gnu/gawk/gawk-5.0.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-3.0+
Requires: gawk-bin = %{version}-%{release}
Requires: gawk-data = %{version}-%{release}
Requires: gawk-lib = %{version}-%{release}
Requires: gawk-libexec = %{version}-%{release}
Requires: gawk-license = %{version}-%{release}
Requires: gawk-locales = %{version}-%{release}
Requires: gawk-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : gmp-dev
BuildRequires : libc6-locale
BuildRequires : ncurses-dev
BuildRequires : readline-dev

%description
This is GNU Awk 5.0.1. It is upwardly compatible with Brian Kernighan's
version of Unix awk.  It is almost completely compliant with the
2018 POSIX 1003.1 standard for awk. (See the note below about POSIX.)

%package bin
Summary: bin components for the gawk package.
Group: Binaries
Requires: gawk-data = %{version}-%{release}
Requires: gawk-libexec = %{version}-%{release}
Requires: gawk-license = %{version}-%{release}

%description bin
bin components for the gawk package.


%package data
Summary: data components for the gawk package.
Group: Data

%description data
data components for the gawk package.


%package dev
Summary: dev components for the gawk package.
Group: Development
Requires: gawk-lib = %{version}-%{release}
Requires: gawk-bin = %{version}-%{release}
Requires: gawk-data = %{version}-%{release}
Provides: gawk-devel = %{version}-%{release}
Requires: gawk = %{version}-%{release}

%description dev
dev components for the gawk package.


%package doc
Summary: doc components for the gawk package.
Group: Documentation
Requires: gawk-man = %{version}-%{release}

%description doc
doc components for the gawk package.


%package extras
Summary: extras components for the gawk package.
Group: Default

%description extras
extras components for the gawk package.


%package lib
Summary: lib components for the gawk package.
Group: Libraries
Requires: gawk-data = %{version}-%{release}
Requires: gawk-libexec = %{version}-%{release}
Requires: gawk-license = %{version}-%{release}

%description lib
lib components for the gawk package.


%package libexec
Summary: libexec components for the gawk package.
Group: Default
Requires: gawk-license = %{version}-%{release}

%description libexec
libexec components for the gawk package.


%package license
Summary: license components for the gawk package.
Group: Default

%description license
license components for the gawk package.


%package locales
Summary: locales components for the gawk package.
Group: Default

%description locales
locales components for the gawk package.


%package man
Summary: man components for the gawk package.
Group: Default

%description man
man components for the gawk package.


%prep
%setup -q -n gawk-5.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571202677
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1571202677
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gawk
cp %{_builddir}/gawk-5.0.1/COPYING %{buildroot}/usr/share/package-licenses/gawk/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gawk-5.0.1/extension/COPYING %{buildroot}/usr/share/package-licenses/gawk/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/gawk-5.0.1/missing_d/COPYING.LIB %{buildroot}/usr/share/package-licenses/gawk/0e8e850b0580fbaaa0872326cb1b8ad6adda9b0d
%make_install
%find_lang gawk
## install_append content
ln -s gawk.1 %{buildroot}/usr/share/man/man1/awk.1
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/awk
/usr/bin/gawk
/usr/bin/gawk-5.0.1

%files data
%defattr(-,root,root,-)
/usr/share/awk/have_mpfr.awk
/usr/share/awk/intdiv0.awk
/usr/share/awk/ns_passwd.awk

%files dev
%defattr(-,root,root,-)
/usr/include/gawkapi.h
/usr/share/man/man3/filefuncs.3am
/usr/share/man/man3/fnmatch.3am
/usr/share/man/man3/fork.3am
/usr/share/man/man3/inplace.3am
/usr/share/man/man3/ordchr.3am
/usr/share/man/man3/readdir.3am
/usr/share/man/man3/readfile.3am
/usr/share/man/man3/revoutput.3am
/usr/share/man/man3/revtwoway.3am
/usr/share/man/man3/rwarray.3am
/usr/share/man/man3/time.3am

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files extras
%defattr(-,root,root,-)
/usr/share/awk/assert.awk
/usr/share/awk/bits2str.awk
/usr/share/awk/cliff_rand.awk
/usr/share/awk/ctime.awk
/usr/share/awk/ftrans.awk
/usr/share/awk/getopt.awk
/usr/share/awk/gettime.awk
/usr/share/awk/group.awk
/usr/share/awk/inplace.awk
/usr/share/awk/join.awk
/usr/share/awk/libintl.awk
/usr/share/awk/noassign.awk
/usr/share/awk/ord.awk
/usr/share/awk/passwd.awk
/usr/share/awk/processarray.awk
/usr/share/awk/quicksort.awk
/usr/share/awk/readable.awk
/usr/share/awk/readfile.awk
/usr/share/awk/rewind.awk
/usr/share/awk/round.awk
/usr/share/awk/shellquote.awk
/usr/share/awk/strtonum.awk
/usr/share/awk/walkarray.awk
/usr/share/awk/zerofile.awk

%files lib
%defattr(-,root,root,-)
/usr/lib64/gawk/filefuncs.so
/usr/lib64/gawk/fnmatch.so
/usr/lib64/gawk/fork.so
/usr/lib64/gawk/inplace.so
/usr/lib64/gawk/intdiv.so
/usr/lib64/gawk/ordchr.so
/usr/lib64/gawk/readdir.so
/usr/lib64/gawk/readfile.so
/usr/lib64/gawk/revoutput.so
/usr/lib64/gawk/revtwoway.so
/usr/lib64/gawk/rwarray.so
/usr/lib64/gawk/time.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/awk/grcat
/usr/libexec/awk/pwcat

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gawk/0e8e850b0580fbaaa0872326cb1b8ad6adda9b0d
/usr/share/package-licenses/gawk/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/awk.1
/usr/share/man/man1/gawk.1

%files locales -f gawk.lang
%defattr(-,root,root,-)

