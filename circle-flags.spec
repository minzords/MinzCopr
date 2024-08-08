Name:			circle-flags
Version:		2.6.2
Release:		1%{?dist}
Summary:		A collection of circular flags in SVG format
Summary(fr):	Une collection de drapeaux circulaires au format SVG
License:		MIT
URL:			http://packages.linuxmint.com/pool/main/c/%{name}
Source0:		%{URL}/%{name}_%{version}.tar.xz

BuildArch:		noarch

%description
A collection of circular flags in SVG format

%prep
%setup -q -n %{name}

%build
# Nothing to do

%install
# Install the configuration files
cp -r usr %{buildroot}

%files
%{_datadir}/%{name}-svg

%changelog
* Thu Aug 08 2024 - Minzord <contact@minzord.fr> - 2.6.2-1
- Initial package
- Compatible with Fedora and RHEL
