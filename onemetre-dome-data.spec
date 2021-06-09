Name:      onemetre-dome-data
Version:   20210612
Release:   0
Url:       https://github.com/warwick-one-metre/domed
Summary:   Dome configuration for W1m telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/domed

%{__install} %{_sourcedir}/10-onemetre-dome.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/onemetre.json %{buildroot}%{_sysconfdir}/domed

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/domed/onemetre.json
%{_udevrulesdir}/10-onemetre-dome.rules

%changelog
