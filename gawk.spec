#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gawk
Version  : 4.1.4
Release  : 35
URL      : http://ftp.gnu.org/gnu/gawk/gawk-4.1.4.tar.xz
Source0  : http://ftp.gnu.org/gnu/gawk/gawk-4.1.4.tar.xz
Source1  : gawk.gcov
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-3.0+
Requires: gawk-bin
Requires: gawk-lib
Requires: gawk-data
Requires: gawk-doc
Requires: gawk-locales
BuildRequires : bison
BuildRequires : gmp-dev
BuildRequires : libc6-locale
BuildRequires : ncurses-dev
BuildRequires : readline-dev

%description
This is GNU Awk 4.1.4. It is upwardly compatible with Brian Kernighan's
version of Unix awk.  It is almost completely compliant with the
2008 POSIX 1003.1 standard for awk. (See the note below about POSIX.)

%package bin
Summary: bin components for the gawk package.
Group: Binaries
Requires: gawk-data

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
Requires: gawk-lib
Requires: gawk-bin
Requires: gawk-data
Provides: gawk-devel

%description dev
dev components for the gawk package.


%package doc
Summary: doc components for the gawk package.
Group: Documentation

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
Requires: gawk-data

%description lib
lib components for the gawk package.


%package locales
Summary: locales components for the gawk package.
Group: Default

%description locales
locales components for the gawk package.


%prep
%setup -q -n gawk-4.1.4

%build
export LANG=C
export CFLAGS="$CFLAGS -O3 -Os -fauto-profile=%{SOURCE1} -ffunction-sections "
export FCFLAGS="$CFLAGS -O3 -Os -fauto-profile=%{SOURCE1} -ffunction-sections "
export FFLAGS="$CFLAGS -O3 -Os -fauto-profile=%{SOURCE1} -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fauto-profile=%{SOURCE1} -ffunction-sections "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang gawk

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/awk
/usr/bin/gawk
/usr/bin/gawk-4.1.4
/usr/bin/igawk
/usr/libexec/awk/grcat
/usr/libexec/awk/pwcat

%files data
%defattr(-,root,root,-)
%exclude /usr/share/awk/assert.awk
%exclude /usr/share/awk/bits2str.awk
%exclude /usr/share/awk/cliff_rand.awk
%exclude /usr/share/awk/ctime.awk
%exclude /usr/share/awk/ftrans.awk
%exclude /usr/share/awk/getopt.awk
%exclude /usr/share/awk/gettime.awk
%exclude /usr/share/awk/group.awk
%exclude /usr/share/awk/inplace.awk
%exclude /usr/share/awk/join.awk
%exclude /usr/share/awk/libintl.awk
%exclude /usr/share/awk/noassign.awk
%exclude /usr/share/awk/ord.awk
%exclude /usr/share/awk/passwd.awk
%exclude /usr/share/awk/processarray.awk
%exclude /usr/share/awk/quicksort.awk
%exclude /usr/share/awk/readable.awk
%exclude /usr/share/awk/readfile.awk
%exclude /usr/share/awk/rewind.awk
%exclude /usr/share/awk/round.awk
%exclude /usr/share/awk/shellquote.awk
%exclude /usr/share/awk/strtonum.awk
%exclude /usr/share/awk/walkarray.awk
%exclude /usr/share/awk/zerofile.awk

%files dev
%defattr(-,root,root,-)
/usr/include/*.h

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

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
/usr/lib64/gawk/ordchr.so
/usr/lib64/gawk/readdir.so
/usr/lib64/gawk/readfile.so
/usr/lib64/gawk/revoutput.so
/usr/lib64/gawk/revtwoway.so
/usr/lib64/gawk/rwarray.so
/usr/lib64/gawk/testext.so
/usr/lib64/gawk/time.so

%files locales -f gawk.lang 
%defattr(-,root,root,-)

