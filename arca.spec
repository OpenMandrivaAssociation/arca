#define snapshot 20220107

Name:		arca
Version:	0.5.2
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Maui Archiver for compressed files
URL:    	https://mauikit.org
Source0:	https://invent.kde.org/maui/arca/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/%{name}-%{snapshot}.tar.bz2}
License:	GPLv3
Group:		Development/Tools/Maui
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:  cmake(KF5Archive)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(MauiKit3)
BuildRequires:  cmake(MauiKitFileBrowsing3)
BuildRequires:	gettext
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	cmake(Qt5QuickCompiler)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5QmlModels)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Widgets)

%description
Maui Archiver for compressed files

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/arca
%{_datadir}/applications/org.kde.arca.desktop
%{_datadir}/metainfo/org.kde.arca.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/arca.svg
