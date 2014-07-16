%define major 5
%define libname %mklibname KF5Html %{major}
%define devname %mklibname KF5Html -d
%define debug_package %{nil}

Name: khtml
Version: 5.0.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/portingAids/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 HTML library (for compatibility with 4.x)
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: cmake
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: cmake(KF5JS)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5GlobalAccel)
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
%setup -q
%apply_patches
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5
%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_sysconfdir}/xdg/khtmlrc
%{_datadir}/kf%{major}/khtml
%{_datadir}/kf%{major}/kjava
%{_datadir}/khtml
%{_datadir}/kservices%{major}/*.desktop
%{_libdir}/plugins/kf%{major}/parts/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*
