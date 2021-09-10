Name:      observatory-dome-client
Version:   20210910
Release:   0
Url:       https://github.com/warwick-one-metre/domed
Summary:   Astrohaven dome client.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwick-observatory-common, python3-warwick-observatory-dome

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/dome %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/dome %{buildroot}/etc/bash_completion.d/dome

%files
%defattr(0755,root,root,-)
%{_bindir}/dome
/etc/bash_completion.d/dome

%changelog
