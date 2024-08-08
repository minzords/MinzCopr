Name:			python3-cinemagoer
Version:		2023.05.01
Release:		1%{?dist}
Summary:		Python bindings for the Internet Movie Database (IMDb)
Summary(fr):	Python bindings pour l'Internet Movie Database (IMDb)

License:		GPL-2.0-or-later
URL:			https://cinemagoer.github.io
Source0:		https://github.com/cinemagoer/cinemagoer/archive/refs/tags/%{version}.tar.gz

BuildArch:		noarch
BuildRequires:	python3-setuptools
BuildRequires:	python3-rpm-macros

Requires:		python3-lxml
Requires:		python3-sqlalchemy
Requires:		python3-tqdm
Requires:		python3-setuptools
Requires:		python3-importlib-metadata

%description
Python bindings for the Internet Movie Database (IMDb)

%prep
%setup -q -n cinemagoer-%{version}

%build
python3 setup.py build

%install
# Install the configuration files
python3 setup.py install --optimize=1 --root="%{buildroot}"

# Install the documentation readme
install -Dm644 README.rst %{buildroot}%{_docdir}/%{name}/README.rst

%files
%{_bindir}/get_company.py
%{_bindir}/get_first_company.py
%{_bindir}/get_first_movie.py
%{_bindir}/get_first_person.py
%{_bindir}/get_keyword.py
%{_bindir}/get_movie.py
%{_bindir}/get_movie_list.py
%{_bindir}/get_person.py
%{_bindir}/get_top_bottom_movies.py
%{_bindir}/imdbpy
%{_bindir}/imdbpy2sql.py
%{_bindir}/s32cinemagoer.py
%{_bindir}/search_company.py
%{_bindir}/search_keyword.py
%{_bindir}/search_movie.py
%{_bindir}/search_person.py
%{python3_sitelib}/imdb
%{python3_sitelib}/cinemagoer-2023.5.1-py%{python3_version}.egg-info
%{_docdir}/%{name}/README.rst

%changelog
* Thu Aug 08 2024 - Minzord <contact@minzord.fr> - 2023.05.01-1
- Initial package
- Compatible with Fedora and RHEL
