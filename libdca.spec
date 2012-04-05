%define name libdca
%define version 0.0.5
%define release %mkrel 3
%define distsuffix plf
%define major 0
%define libname %mklibname dca %{major}
%define develname %mklibname -d dca

Summary: DTS Coherent Acoustics decoder
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.videolan.org/pub/videolan/libdca/%version/%{name}-%version.tar.bz2
License: GPLv2+
Group: Sound
Url: http://www.videolan.org/developers/libdca.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes: dtsdec
Provides: dtsdec

%description
This is a free decoder for the DTS Coherent Acoustics format. It
consists of a library and a command line decoder. DTS is a high
quality multi-channel (5.1) digital audio format used in DVDs and
DTS audio CDs.

This package is in restricted as it might violate some patents.

%package tools
Summary: DTS Coherent Acoustics decoder
Group: Sound
Obsoletes: dtsdec
Provides: dtsdec

%description tools
This is a free decoder for the DTS Coherent Acoustics format. It
consists of a library and a command line decoder. DTS is a high
quality multi-channel (5.1) digital audio format used in DVDs and
DTS audio CDs.

This package is in restricted as it might violate some patents.

%package -n %{libname}
Group: System/Libraries
Summary: DTS Coherent Acoustics decoder shared library

%description -n %{libname}
This is a free decoder for the DTS Coherent Acoustics format. It
consists of a library and a command line decoder. DTS is a high
quality multi-channel (5.1) digital audio format used in DVDs and
DTS audio CDs.

This package is in restricted as it might violate some patents.

%package -n %{develname}
Group: Development/C
Summary: Library for decoding DTS audio - C development files
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: dtsdec-devel
Provides: dtsdec-devel

%description -n %{develname}
This is a free decoder for the DTS Coherent Acoustics format.DTS is a
high quality multi-channel (5.1) digital audio format used in DVDs and
DTS audio CDs.

This package contains a library and the required header files to
develop with libdts.

This is in restricted as it might violate some patents.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# libdca installs broken libdts.a compatibility symlink;
# replace it with shared devel symlink:
rm %{buildroot}%{_libdir}/libdts.a
ln -s libdca.so %{buildroot}%{_libdir}/libdts.so

%clean
rm -rf %{buildroot}

%if %mdvver < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%files tools
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/dtsdec
%{_bindir}/dcadec
%{_bindir}/extract_dca
%{_bindir}/extract_dts
%{_mandir}/man1/dcadec.1*
%{_mandir}/man1/extract_dca.1*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libdca.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc TODO
%{_includedir}/dts.h
%{_includedir}/dca.h
%{_libdir}/*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/libdca.pc
%{_libdir}/pkgconfig/libdts.pc

%changelog
* Fri Aug 19 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.0.5-3plf2011.0
- Port from PLF to restricted
- Little spec clean up

* Mon Jul 20 2009 Anssi Hannula <anssi@zarb.org> 0.0.5-2plf2010.0
- remove broken static library compatibility symlink and replace it with
  a shared library compatibility symlink

* Thu Jul 24 2008 Götz Waschk <goetz@zarb.org> 0.0.5-1plf2009.0
- rename to libdca

* Thu Jan 17 2008 Götz Waschk <goetz@zarb.org> 0.0.2-6plf2008.1
- rebuild

* Sun Dec  3 2006 Götz Waschk <goetz@zarb.org> 0.0.2-5plf2007.1
- fix description
- add dts_internal header for avidemux

* Mon Aug 28 2006 Götz Waschk <goetz@zarb.org> 0.0.2-4plf2007.0
- rebuild

* Sun Aug 07 2005 trem <trem@zarb.org> 0.0.2-3plf
- add distsuffix

* Mon May 23 2005 Götz Waschk <goetz@zarb.org> 0.0.2-2plf
- mkrel

* Wed Nov  3 2004 Götz Waschk <goetz@zarb.org> 0.0.2-1plf
- initial plf package

* Tue Mar  2 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.2-1mdk
- the header has moved to %_includedir
- new version

* Wed Feb 11 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.1-1mdk
- initial package
