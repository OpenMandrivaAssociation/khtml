%define major 5
%define libname %mklibname KF5Html %{major}
%define devname %mklibname KF5Html -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
# (tpg) 2019-08-20
# fragment is larger than or outside of variable
#  call void @llvm.dbg.value(metadata i64 %439, metadata !155850, metadata !DIExpression(DW_OP_LLVM_fragment, 128, 64)), !dbg !943919
# !155850 = !DILocalVariable(name: "yyval", scope: !155822, file: !155029, line: 1841, type: !155829)
# LLVM ERROR: Broken module found, compilation aborted!
#clang-9: error: linker command failed with exit code 1 (use -v to see invocation)
%define _disable_lto 1

Name: khtml
Version: 5.67.0
Release: 3
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/portingAids/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 HTML library (for compatibility with 4.x)
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(phonon4qt5)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: cmake(KF5JS)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: giflib-devel
BuildRequires: jpeg-devel
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(zlib)
BuildRequires: gperf
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 HTML library.

This is for compatibility with KDE 4.x only. 
New applications should use QtWebKit.

%package -n %{libname}
Summary: The KDE Frameworks 5 HTML library
Group: System/Libraries

%description -n %{libname}
The KDE Frameworks 5 HTML library.

This is for compatibility with KDE 4.x only. 
New applications should use QtWebKit.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_sysconfdir}/xdg/khtmlrc
%{_datadir}/qlogging-categories5/khtml.categories
%{_datadir}/kf%{major}/khtml
%{_datadir}/kf%{major}/kjava
%{_datadir}/kservices%{major}/*.desktop
%{_libdir}/qt5/plugins/kf%{major}/parts/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*
