%define distsuffix plf

%define major 0
%define libname %mklibname dca %{major}
%define devname %mklibname -d dca

Summary:	DTS Coherent Acoustics decoder
Name:		libdca
Version:	0.0.5
Release:	5
License:	GPLv2+
Group:		Sound
Url:		http://www.videolan.org/developers/libdca.html
Source0:	http://download.videolan.org/pub/videolan/libdca/%{version}/%{name}-%{version}.tar.bz2

%description
This is a free decoder for the DTS Coherent Acoustics format. It
consists of a library and a command line decoder. DTS is a high
quality multi-channel (5.1) digital audio format used in DVDs and
DTS audio CDs.

This package is in restricted as it might violate some patents.

#----------------------------------------------------------------------------

%package tools
Summary:	DTS Coherent Acoustics decoder
Group:		Sound
Obsoletes:	dtsdec < %{EVRD}
Provides:	dtsdec = %{EVRD}

%description tools
This is a free decoder for the DTS Coherent Acoustics format. It
consists of a library and a command line decoder. DTS is a high
quality multi-channel (5.1) digital audio format used in DVDs and
DTS audio CDs.

This package is in restricted as it might violate some patents.

%files tools
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/dtsdec
%{_bindir}/dcadec
%{_bindir}/extract_dca
%{_bindir}/extract_dts
%{_mandir}/man1/dcadec.1*
%{_mandir}/man1/dtsdec.1*
%{_mandir}/man1/extract_dca.1*
%{_mandir}/man1/extract_dts.1*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	DTS Coherent Acoustics decoder shared library
Group:		System/Libraries

%description -n %{libname}
This is a free decoder for the DTS Coherent Acoustics format. It
consists of a library and a command line decoder. DTS is a high
quality multi-channel (5.1) digital audio format used in DVDs and
DTS audio CDs.

This package is in restricted as it might violate some patents.

%files -n %{libname}
%{_libdir}/libdca.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Library for decoding DTS audio - C development files
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	dtsdec-devel = %{EVRD}

%description -n %{devname}
This is a free decoder for the DTS Coherent Acoustics format.DTS is a
high quality multi-channel (5.1) digital audio format used in DVDs and
DTS audio CDs.

This package contains a library and the required header files to
develop with libdts.

This is in restricted as it might violate some patents.

%files -n %{devname}
%doc TODO
%{_includedir}/dts.h
%{_includedir}/dca.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libdca.pc
%{_libdir}/pkgconfig/libdts.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
# libdca installs broken libdts.a compatibility symlink;
# replace it with shared devel symlink:
rm -f %{buildroot}%{_libdir}/libdts.a
ln -s libdca.so %{buildroot}%{_libdir}/libdts.so

