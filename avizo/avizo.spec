%global packager Thomas Lake <tom@leftdiodes.co.uk>
%global forgeurl https://github.com/heyjuvi/avizo

%global tag 1.3
Name:           avizo
Version:        %{tag}
Release:        %autorelease
Summary:        A simple notification daemon, mainly intended to be used for multimedia keys for example with Sway.

%forgemeta

License:        GPL-3.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc, meson, vala, cmake, gtk3-devel, gtk-layer-shell-devel
Requires:       gtk3, gtk-layer-shell, brightnessctl, pamixer >= 1.6

%description


%prep
%forgeautosetup -v

%build
%meson
%meson_build


%install
%meson_install

%files
%license LICENSE
%{_bindir}/avizo-client
%{_bindir}/avizo-service
%{_bindir}/volumectl
%{_bindir}/lightctl
%{_sysconfdir}/xdg/avizo/config.ini

%changelog
%autochangelog 
