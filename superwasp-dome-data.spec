Name:      superwasp-dome-data
Version:   20221119
Release:   0
Url:       https://github.com/warwick-one-metre/domed
Summary:   Dome configuration for SuperWASP telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/domed

%{__install} %{_sourcedir}/10-superwasp-dome.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/superwasp.json %{buildroot}%{_sysconfdir}/domed

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/domed/superwasp.json
%{_udevrulesdir}/10-superwasp-dome.rules

%changelog
