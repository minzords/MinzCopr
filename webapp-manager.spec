Name:			webapp-manager
Version:		1.3.7
Release:		1%{?dist}
Summary:		Run websites as if they were apps
Summary(fr):	Exécutez des sites web comme des applications

License:		MIT
URL:			https://github.com/linuxmint/%{name}
Source0:		https://github.com/linuxmint/%{name}/archive/refs/tags/%{version}.tar.gz

BuildArch:		noarch
BuildRequires:	make
BuildRequires:	gettext

Requires:		python3-gobject
Requires:		python-beautifulsoup4
Requires:		python3-configobj
Requires:		python3-pillow
Requires:		python3-setproctitle
Requires:		python3-tldextract
Requires:		xapps

%description
Run websites as if they were apps

%prep
%setup -q -n %{name}-%{version}

%build
# Set the version number in the about dialog
sed -i "s/__DEB_VERSION__/%{version}/g" usr/lib/%{name}/%{name}.py

make

%install
# Install the configuration files
cp -r etc usr %{buildroot}

%files
/etc/xdg/menus/applications-merged/webapps.menu
/usr/bin/%{name}
/usr/lib/%{name}/common.py
/usr/lib/%{name}/%{name}.py
 %{_datadir}/applications/kde4/%{name}.desktop
 %{_datadir}/applications/%{name}.desktop
 %{_datadir}/desktop-directories/webapps-webapps.directory
 %{_datadir}/glib-2.0/schemas/org.x.%{name}.gschema.xml
 %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
 %{_datadir}/icons/hicolor/scalable/categories/applications-webapps.svg
 %{_datadir}/locale/am/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/ar/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/be/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/bg/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/bn/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/br/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/ca/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/cs/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/cy/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/da/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/de/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/el/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/en_CA/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/en_GB/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/eo/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/es/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/et/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/eu/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/fa/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/fi/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/fr_CA/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/he/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/hi/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/hr/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/hu/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/ia/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/id/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/ie/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/is/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/it/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/ja/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/kab/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/kn/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/ko/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/la/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/lt/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/nb/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/nl/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/oc/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/pl/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/pt/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/pt_BR/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/ro/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/ru/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/sk/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/sl/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/sr/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/sr@latin/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/sv/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/tr/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/uk/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/uz/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/vi/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/zgh/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/zh_CN/LC_MESSAGES/%{name}.mo
 %{_datadir}/locale/zh_TW/LC_MESSAGES/%{name}.mo
 %{_datadir}/%{name}/firefox/profile/chrome/userChrome.css
 %{_datadir}/%{name}/firefox/profile/places.sqlite
 %{_datadir}/%{name}/firefox/profile/search.json.mozlz4
 %{_datadir}/%{name}/firefox/profile/user.js
 %{_datadir}/%{name}/firefox/userChrome-with-navbar.css
 %{_datadir}/%{name}/shortcuts.ui
 %{_datadir}/%{name}/%{name}.ui

%changelog
* Thu Aug 08 2024 - Minzord <contact@minzord.fr> - 1.3.7-1
- Initial package
- Compatible with Fedora and RHEL
