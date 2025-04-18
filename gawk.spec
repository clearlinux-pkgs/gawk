#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v23
# autospec commit: 247c192
#
# Source0 file verified with key 0xDF597815937EC0D2 (arnold@skeeve.com)
#
Name     : gawk
Version  : 5.3.2
Release  : 70
URL      : https://mirrors.kernel.org/gnu/gawk/gawk-5.3.2.tar.gz
Source0  : https://mirrors.kernel.org/gnu/gawk/gawk-5.3.2.tar.gz
Source1  : https://mirrors.kernel.org/gnu/gawk/gawk-5.3.2.tar.gz.sig
Source2  : DF597815937EC0D2.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-3.0+
Requires: gawk-bin = %{version}-%{release}
Requires: gawk-data = %{version}-%{release}
Requires: gawk-info = %{version}-%{release}
Requires: gawk-lib = %{version}-%{release}
Requires: gawk-libexec = %{version}-%{release}
Requires: gawk-license = %{version}-%{release}
Requires: gawk-locales = %{version}-%{release}
Requires: gawk-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : gmp-dev
BuildRequires : gnupg
BuildRequires : libc6-locale
BuildRequires : ncurses-dev
BuildRequires : readline-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025

This is GNU Awk 5.3.2. It is upwardly compatible with Brian Kernighan's
version of Unix awk.  It is almost completely compliant with the
2024 POSIX 1003 standard for awk. (See the note below about POSIX.)

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


%package extras
Summary: extras components for the gawk package.
Group: Default

%description extras
extras components for the gawk package.


%package info
Summary: info components for the gawk package.
Group: Default

%description info
info components for the gawk package.


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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) DF597815937EC0D2' gpg.status
%setup -q -n gawk-5.3.2
cd %{_builddir}/gawk-5.3.2
pushd ..
cp -a gawk-5.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1743691213
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1743691213
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gawk
cp %{_builddir}/gawk-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gawk/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/gawk-%{version}/extension/COPYING %{buildroot}/usr/share/package-licenses/gawk/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/gawk-%{version}/missing_d/COPYING.LIB %{buildroot}/usr/share/package-licenses/gawk/0e8e850b0580fbaaa0872326cb1b8ad6adda9b0d || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang gawk
## install_append content
ln -s gawk.1 %{buildroot}/usr/share/man/man1/awk.1
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gawk
/V3/usr/bin/gawk-5.3.2
/usr/bin/awk
/usr/bin/gawk
/usr/bin/gawk-5.3.2
/usr/bin/gawkbug

%files data
%defattr(-,root,root,-)
/usr/share/awk/have_mpfr.awk
/usr/share/awk/intdiv0.awk
/usr/share/awk/isnumeric.awk
/usr/share/awk/ns_passwd.awk
/usr/share/awk/tocsv.awk

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

%files info
%defattr(0644,root,root,0755)
/usr/share/info/gawk.info
/usr/share/info/gawk_api-figure1.png
/usr/share/info/gawk_api-figure2.png
/usr/share/info/gawk_api-figure3.png
/usr/share/info/gawk_array-elements.png
/usr/share/info/gawk_general-program.png
/usr/share/info/gawk_process-flow.png
/usr/share/info/gawk_statist.jpg
/usr/share/info/gawkinet.info
/usr/share/info/gawkworkflow.info
/usr/share/info/pm-gawk.info

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gawk/filefuncs.so
/V3/usr/lib64/gawk/fnmatch.so
/V3/usr/lib64/gawk/fork.so
/V3/usr/lib64/gawk/inplace.so
/V3/usr/lib64/gawk/intdiv.so
/V3/usr/lib64/gawk/ordchr.so
/V3/usr/lib64/gawk/readdir.so
/V3/usr/lib64/gawk/readfile.so
/V3/usr/lib64/gawk/revoutput.so
/V3/usr/lib64/gawk/revtwoway.so
/V3/usr/lib64/gawk/rwarray.so
/V3/usr/lib64/gawk/time.so
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
/V3/usr/libexec/awk/grcat
/V3/usr/libexec/awk/pwcat
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
/usr/share/man/man1/gawkbug.1
/usr/share/man/man1/pm-gawk.1

%files locales -f gawk.lang
%defattr(-,root,root,-)

