Name:      rockit-dome
Version:   %{_version}
Release:   1%{dist}
Summary:   Astrohaven dome server
Url:       https://github.com/rockit-astro/domed
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/domed/
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/dome %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/domed %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/domed@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/dome %{buildroot}/etc/bash_completion.d

%{__install} %{_sourcedir}/config/10-clasp-dome.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/config/10-onemetre-dome.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/config/10-sting-dome.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/config/clasp.json %{buildroot}%{_sysconfdir}/domed/
%{__install} %{_sourcedir}/config/onemetre.json %{buildroot}%{_sysconfdir}/domed/
%{__install} %{_sourcedir}/config/sting.json %{buildroot}%{_sysconfdir}/domed/

%package server
Summary:  Astrohaven dome server
Group:    Unspecified
Requires: python3-rockit-dome python3-pyserial
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/domed
%defattr(0644,root,root,-)
%{_unitdir}/domed@.service

%package client
Summary:  Astrohaven dome client
Group:    Unspecified
Requires: python3-rockit-dome
%description client

%files client
%defattr(0755,root,root,-)
%{_bindir}/dome
/etc/bash_completion.d/dome

%package data-clasp
Summary: Dome configuration for the CLASP telescope
Group:   Unspecified
%description data-clasp

%files data-clasp
%defattr(0644,root,root,-)
%{_sysconfdir}/domed/clasp.json
%{_udevrulesdir}/10-clasp-dome.rules

%package data-onemetre
Summary: Dome configuration for the W1m metre telescope
Group:   Unspecified
%description data-onemetre

%files data-onemetre
%defattr(0644,root,root,-)
%{_sysconfdir}/domed/onemetre.json
%{_udevrulesdir}/10-onemetre-dome.rules

%package data-sting
Summary: Dome configuration for the STING telescope
Group:   Unspecified
%description data-sting

%files data-sting
%defattr(0644,root,root,-)
%{_sysconfdir}/domed/sting.json
%{_udevrulesdir}/10-sting-dome.rules

%changelog
