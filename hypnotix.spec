Name:			hypnotix
Version:		4.6
Release:		2%{?dist}
Summary:		An IPTV streaming application with support for live TV, movies and series.
Summary(fr):	Application de streaming IPTV avec support pour la TV en direct, les films et les séries.

License:		MIT
URL:			https://github.com/linuxmint/%{name}
Source0:		https://github.com/linuxmint/%{name}/archive/refs/tags/%{version}.tar.gz

BuildArch:		noarch
BuildRequires:	make
BuildRequires:	gettext

Requires:		circle-flags
Requires:		python3-cairo
Requires:		python3-gobject
Requires:		python3-requests
Requires:		python3-setproctitle
Requires:		python3-unidecode
Requires:       python3-cinemagoer
Requires:		mpv-libs
Requires:		xapps
Requires:		yt-dlp

%description
An IPTV streaming application with support for live TV, movies and series.

%prep
%setup -q -n %{name}-%{version}

%build
# Set the version number in the about dialog
sed -i "s/__DEB_VERSION__/%{version}/g" usr/lib/%{name}/%{name}.py

make

%install
# Install the configuration files
cp -r usr %{buildroot}

%files
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/common.py
%{_prefix}/lib/%{name}/%{name}.py
%{_prefix}/lib/%{name}/mpv.py
%{_prefix}/lib/%{name}/xtream.py
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.x.%{name}.gschema.xml
%{_datadir}/%{name}/countries.list
%{_datadir}/%{name}/generic_tv_logo.png
%{_datadir}/%{name}/%{name}.css
%{_datadir}/%{name}/%{name}.ui
%{_datadir}/%{name}/pictures/badges/de.svg
%{_datadir}/%{name}/pictures/badges/en.svg
%{_datadir}/%{name}/pictures/badges/es.svg
%{_datadir}/%{name}/pictures/badges/fr.svg
%{_datadir}/%{name}/pictures/badges/it.svg
%{_datadir}/%{name}/pictures/badges/movies.svg
%{_datadir}/%{name}/pictures/badges/music.svg
%{_datadir}/%{name}/pictures/badges/news.svg
%{_datadir}/%{name}/pictures/movies.svg
%{_datadir}/%{name}/pictures/series.svg
%{_datadir}/%{name}/pictures/tv.svg
%{_datadir}/%{name}/shortcuts.ui
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/locale/am/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/ar/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/be/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/bg/LC_MESSAGES/%{name}.mo
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
%{_datadir}/locale/rue/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/sk/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/sl/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/sq/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/sr/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/sr@latin/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/sv/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/th/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/tr/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/uk/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/uz/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/vi/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/zh_TW/LC_MESSAGES/%{name}.mo

%changelog
* Thu Aug 08 2024 - Minzord <contact@minzord.fr> - 4.6-1
- Initial package
- Compatible with Fedora and RHEL
