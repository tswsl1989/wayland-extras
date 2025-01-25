%global packager Thomas Lake <tom@leftdiodes.co.uk>
%global forgeurl https://github.com/jovanlanik/gtklock

Name:           gtklock
Version:        4.0.0
Release:        %autorelease
Summary:        A lockscreen based on gtkgreet. It uses the ext-session-lock Wayland protocol. Works on sway and other wlroots-based compositors.

%forgemeta

License:        GPL-3.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc, meson, wayland-devel, scdoc, pam-devel, gtk3-devel >= 3.22.0, pkgconfig(gtk-session-lock)
Requires:       gtk3, gtk-session-lock >= 0.2.0, pam

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
%{_bindir}/gtklock
%{_datadir}/locale/cs/LC_MESSAGES/gtklock.mo
%{_datadir}/locale/de/LC_MESSAGES/gtklock.mo
%{_datadir}/locale/sr/LC_MESSAGES/gtklock.mo
%{_datadir}/locale/sr@latin/LC_MESSAGES/gtklock.mo
%{_mandir}/man1/gtklock.1.gz
%{_sysconfdir}/pam.d/gtklock

%changelog
%autochangelog 
