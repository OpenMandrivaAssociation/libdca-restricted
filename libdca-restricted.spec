%define distsuffix plf
%define _disable_rebuild_configure 1
%define _disable_lto 1

%define major 0
%define libname %mklibname dca %{major}
%define develname %mklibname -d dca

Summary:	DTS Coherent Acoustics decoder
Name:	libdca
Version:	0.0.7
Release:	2
License:	GPLv2+
Group:	Sound
Url:		https://www.videolan.org/developers/libdca.html
Source0:	http://download.videolan.org/pub/videolan/libdca/%{version}/%{name}-%{version}.tar.bz2
Patch0:	libdca-0.0.7-fix-typos-in-Makefile_am.patch

%description
This is a free decoder for the DTS Coherent Acoustics format. It consists of a
library and a command line decoder. DTS is a high quality multi-channel (5.1)
digital audio format used in DVDs and DTS audio CDs.
This package is in restricted as it might violate some patents.

#-----------------------------------------------------------------------------

%package tools
Summary:	DTS Coherent Acoustics decoder
Group:		Sound
%rename	dtsdec

%description tools
This is a free decoder for the DTS Coherent Acoustics format. It consists of a
library and a command line decoder. DTS is a high quality multi-channel (5.1)
digital audio format used in DVDs and DTS audio CDs.
This package is in restricted as it might violate some patents.

%files tools
%doc ChangeLog NEWS README TODO
%{_bindir}/dtsdec
%{_bindir}/dcadec
%{_bindir}/extract_dca
%{_bindir}/extract_dts
%{_mandir}/man1/dcadec.1*
%{_mandir}/man1/extract_dca.1*
%{_mandir}/man1/dtsdec.1*
%{_mandir}/man1/extract_dts.1*

#-----------------------------------------------------------------------------

%package -n %{libname}
Group:		System/Libraries
Summary:	DTS Coherent Acoustics decoder shared library

%description -n %{libname}
This is a free decoder for the DTS Coherent Acoustics format. It consists of a
library and a command line decoder. DTS is a high quality multi-channel (5.1)
digital audio format used in DVDs and DTS audio CDs.
This package contains the main library. It is in restricted as it might
violate some patents.

%files -n %{libname}
%{_libdir}/libdca.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{develname}
Group:		Development/C
Summary:	Library for decoding DTS audio - C development files
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
%rename dtsdec-devel

%description -n %{develname}
This is a free decoder for the DTS Coherent Acoustics format. It consists of a
library and a command line decoder. DTS is a high quality multi-channel (5.1)
digital audio format used in DVDs and DTS audio CDs.
This package contains a library and the required header files to develop with
libdts.
This is in restricted as it might violate some patents.

%files -n %{develname}
%doc TODO doc/libdca.txt
%{_includedir}/dts.h
%{_includedir}/dca.h
%{_libdir}/libdca.so
%{_libdir}/libdts.so
%{_libdir}/pkgconfig/libdca.pc
%{_libdir}/pkgconfig/libdts.pc

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
autoreconf -vfi
%configure --disable-static
%make_build


%install
%make_install

# The build installs a broken libdts.a compatibility symlink;
# replace it with shared devel symlink
rm -f %{buildroot}%{_libdir}/libdts.a
ln -s libdca.so %{buildroot}%{_libdir}/libdts.so
