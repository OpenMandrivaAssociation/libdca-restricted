%define distsuffix plf

%define major 0
%define libname %mklibname dca %{major}
%define develname %mklibname -d dca

Name:		libdca
Version:	0.0.5
Release:	4
Summary:	DTS Coherent Acoustics decoder
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

%package tools
Summary:	DTS Coherent Acoustics decoder
Group:		Sound
Obsoletes:	dtsdec < %{version}-%{release}
Provides:	dtsdec = %{version}-%{release}

%description tools
This is a free decoder for the DTS Coherent Acoustics format. It
consists of a library and a command line decoder. DTS is a high
quality multi-channel (5.1) digital audio format used in DVDs and
DTS audio CDs.

This package is in restricted as it might violate some patents.

%package -n %{libname}
Group:		System/Libraries
Summary:	DTS Coherent Acoustics decoder shared library

%description -n %{libname}
This is a free decoder for the DTS Coherent Acoustics format. It
consists of a library and a command line decoder. DTS is a high
quality multi-channel (5.1) digital audio format used in DVDs and
DTS audio CDs.

This package is in restricted as it might violate some patents.

%package -n %{develname}
Group:		Development/C
Summary:	Library for decoding DTS audio - C development files
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	dtsdec-devel = %{version}-%{release}

%description -n %{develname}
This is a free decoder for the DTS Coherent Acoustics format.DTS is a
high quality multi-channel (5.1) digital audio format used in DVDs and
DTS audio CDs.

This package contains a library and the required header files to
develop with libdts.

This is in restricted as it might violate some patents.

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

%files tools
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/dtsdec
%{_bindir}/dcadec
%{_bindir}/extract_dca
%{_bindir}/extract_dts
%{_mandir}/man1/dcadec.1*
%{_mandir}/man1/extract_dca.1*

%files -n %{libname}
%{_libdir}/libdca.so.%{major}*

%files -n %{develname}
%doc TODO
%{_includedir}/dts.h
%{_includedir}/dca.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libdca.pc
%{_libdir}/pkgconfig/libdts.pc

