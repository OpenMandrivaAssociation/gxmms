%define name	gxmms
%define version 0.3.0
%define release %mkrel 9

Name: 	 	%{name}
Summary: 	Controls XMMS through the GNOME2 panel
Version: 	%{version}
Release: 	%{release}

Source:		http://savannah.nongnu.org/download/gxmms/%{name}-%{version}.tar.bz2
Patch1: gxmms-0.3.0-gcc4.1.patch
URL:		http://www.nongnu.org/gxmms/
License:	GPL
Group:		Sound
BuildRequires:	libpanel-applet-2-devel
BuildRequires:	xmms-devel
BuildRequires:  perl-XML-Parser
BuildRequires: intltool

%description
gXMMS is a simple GNOME panel applet that lets you control the basic functions
of the X MultiMedia System (XMMS).

This is the list of current features:

Scrollable track time progress bar
Buttons: Previous track - Play / Pause - Stop - Next track - Eject
Real-time tooltips with track title and time
Show/Hide main window, playlist editor and graphical eq
Internazionalization (i18n) 

%prep
%setup -q
%patch1 -p1 -b .gcc

%build
export LDFLAGS=`gtk-config --libs`
%configure2_5x --with-xmms
%make
									
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%_libexecdir/gxmms_applet
%{_libdir}/bonobo/servers/GNOME_gxmmsApplet.server
%{_datadir}/%name
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/pixmaps/*
