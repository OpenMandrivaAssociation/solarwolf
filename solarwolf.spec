%define	name	solarwolf
%define	version	1.5
%define	release	2mdk
%define	Summary	2D frantic arcade game of collecting boxes and dodging bullets

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.pygame.org/shredwheat/solarwolf/
Source0:	%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
License:	LGPL
Group:		Games/Arcade
Summary:	%{Summary}
BuildArch:	noarch
Requires:	pygame
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SolarWolf is an action/arcade game written entirely in Python.

Advance through 48 levels levels. Collect the boxes on each stage,
while enemies shoot at you from all sides. The game is originally based
of one of the author's childhood favorites, SolarFox on the Atari 2600. 

%prep
%setup -q
rm -rf `find -type d -name .xvpics`

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__install} -d $RPM_BUILD_ROOT{%{_gamesdatadir}/%{name},%{_gamesbindir}}
%{__cp} -a data code %{name}.py $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/

%{__cat} <<EOF > $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
#!/bin/sh
cd %{_gamesdatadir}/%{name}
./%{name}.py $@
EOF

%{__install} -d $RPM_BUILD_ROOT%{_menudir}
%{__cat} <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		icon=%{name}.png \
		needs="x11" \
		section="More Applications/Games/Arcade" \
		title="SolarWolf"\
		longtitle="%{Summary}"
EOF

%{__install} %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%{__install} %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
%{__install} %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/data
%{_gamesdatadir}/%{name}/code
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_menudir}/%{name}
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}/%{name}.py