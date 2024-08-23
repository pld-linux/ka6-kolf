#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.08.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kolf
Summary:	kolf
Name:		ka6-%{kaname}
Version:	24.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5012b0c788aac74a8ed34b1bf70946a4
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka6-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kolf is a miniature golf game. The game is played from an overhead
view, with a short bar representing the golf club. Kolf features many
different types of objects, such water hazards, slopes, sand traps,
and black holes (warps), among others.

%description -l pl.UTF-8
Kolf jest miniaturową grą w golfa. Gra jest pokazywana z z góry,
z małą poprzeczką reprezentującą klub golfowy. Kolf zawiera
wiele różnych typów obiektów, takich jak pułapki wodne, zbocza,
pułapki piaskowe i czarne dziury.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolf
%{_desktopdir}/org.kde.kolf.desktop
%{_iconsdir}/hicolor/*x*/apps/kolf.png
%{_iconsdir}/hicolor/scalable/apps/kolf.svgz
%{_datadir}/kolf
%{_datadir}/metainfo/org.kde.kolf.appdata.xml
