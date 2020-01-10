%define debug_package %{nil}

Name:           qt4urpm
Version:        2.0
Release:        2
Summary:        A Qt based frontend for the urpm* package management tools
License:        GPLv3
Group:          System/Configuration/Packaging
URL:            http://www.sf.net/projects/qt4urpm
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  qt4-devel
Requires:       urpmi
Requires:       kdebase4-runtime
Requires:       gurpmi
Requires:       xterm
Requires:       qt4-common

%description
qt4urpm is a Qt4 based frontend for the urpm* package management tools,
which provides an intuitive interface to manage orphaned packages and
search for packages that contain a specific file.

%prep
%setup -q
%autopatch -p1

%build
make lrelease
qmake -spec /usr/lib/qt4/mkspecs/linux-g++ -o Makefile qt4urpm.pro
make LOCALEPATH="%{_datadir}/%{name}/qm/"

%install
mkdir -p %{buildroot}%{_bindir}/
cp %{name} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{_vendor}-%{name}.desktop << EOF
[Desktop Entry]
Name=Qt4urpm
Comment=%{summary}
Comment[ru]=Поиск файлов по пакетам и управление осиротевшими пакетами
Exec=%{_bindir}/%{name}
Icon=/usr/share/icons/oxygen/256x256/categories/preferences-system.png
Type=Application
Categories=System;Settings;PackageManager;
EOF

mkdir -p %{buildroot}%{_datadir}/%{name}/qm
cp *.qm %{buildroot}%{_datadir}/%{name}/qm/

%files
%{_datadir}/applications/%{_vendor}-%{name}.desktop
%{_datadir}/%{name}/qm/*.qm
%defattr(755,root,root,755)
%{_bindir}/%{name}

