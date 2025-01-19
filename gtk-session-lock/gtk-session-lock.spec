%global packager Thomas Lake <tom@leftdiodes.co.uk>
%global forgeurl https://github.com/Cu3PO42/gtk-session-lock

Name:           gtk-session-lock
Version:        0.2.0
Release:        %autorelease
Summary:        A library for building screen lockers using GTK3 with the ext-session-lock-v1 Wayland protocol.

%forgemeta

License:        GPL-3.0-or-later AND MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires: meson >= 0.45.1, libwayland-client >= 1.10.0, gtk3-devel >= 3.22.0, gobject-introspection, vala
Requires:       gtk3

%description


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:	pkgconfig(gtk-session-lock)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%forgeautosetup -v


%build
%meson
%meson_build


%install
%meson_install

%files
%license LICENSE_GPL.txt
%license LICENSE_MIT.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/girepository-1.0/GtkSessionLock-0.1.typelib
%{_libdir}/pkgconfig/gtk-session-lock-0.pc
%{_datadir}/gir-1.0/GtkSessionLock-0.1.gir
%{_datadir}/vala/vapi/gtk-session-lock-0.deps
%{_datadir}/vala/vapi/gtk-session-lock-0.vapi


%changelog
%autochangelog
