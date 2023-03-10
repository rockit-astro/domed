Name:      clasp-dome-data
Version:   20230310
Release:   0
Url:       https://github.com/warwick-one-metre/domed
Summary:   Dome configuration for the CLASP telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/domed

%{__install} %{_sourcedir}/10-clasp-dome.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/clasp.json %{buildroot}%{_sysconfdir}/domed

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/domed/clasp.json
%{_udevrulesdir}/10-clasp-dome.rules

%changelog
