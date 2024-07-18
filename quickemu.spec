Name:			quickemu
Version:		4.9.6
Release:		1%{?dist}
Summary:		Quickly create and run optimised Windows, macOS and Linux desktop virtual machines.
Summary(fr):	Créez et exécutez rapidement des machines virtuelles de bureau Windows, macOS et Linux optimisées.

License:		MIT
URL:			https://github.com/quickemu-project/quickemu
Source0:		https://github.com/quickemu-project/%{name}/archive/refs/tags/%{version}.tar.gz

BuildArch:		noarch
Requires:		bash
Requires:		coreutils
Requires:		curl
Requires:		edk2-tools
Requires:		genisoimage
Requires:		grep
Requires:		jq
Requires:		mesa-demos
Requires:		pciutils
Requires:		procps
Requires:		python3
Requires:		qemu
Requires:		rsync
Requires:		sed
Requires:		socat
Requires:		spice-gtk-tools
Requires:		swtpm
Requires:		unzip
Requires:		usbutils
Requires:		util-linux
Requires:		xdg-user-dirs
Requires:		xrandr

%description
Quickly create and run optimised Windows, macOS and Linux desktop virtual machines.

%prep
%setup -q -n %{name}-%{version}

%build
#nothing to do here

%install
# Install the configuration files
install -Dm644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

# Install the scripts
install -Dm755 chunkcheck %{buildroot}%{_bindir}/chunkcheck
install -Dm755 quickemu %{buildroot}%{_bindir}/quickemu
install -Dm755 quickget %{buildroot}%{_bindir}/quickget
install -Dm755 quickreport %{buildroot}%{_bindir}/quickreport
install -Dm755 windowskey %{buildroot}%{_bindir}/windowskey

# Install the documentation
install -Dm644 docs/quickget.1 %{buildroot}%{_mandir}/man1/quickget.1
install -Dm644 docs/quickemu.1 %{buildroot}%{_mandir}/man1/quickemu.1
install -Dm644 docs/quickemu_conf.1 %{buildroot}%{_mandir}/man1/quickemu_conf.1

%files
%{_bindir}/chunkcheck
%{_bindir}/quickemu
%{_bindir}/quickget
%{_bindir}/quickreport
%{_bindir}/windowskey
%{_mandir}/man1/quickget.1.gz
%{_mandir}/man1/quickemu.1.gz
%{_mandir}/man1/quickemu_conf.1.gz
%{_datadir}/licenses/%{name}/LICENSE

%changelog
* Wed Jul 17 2024 - Minzord <contact@minzord.fr> - 4.9.6-1
- Initial package
- Compatible with Fedora and RHEL
