%define	name	solarwolf
%define	version	1.5
%define	release	10
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
%{__install} -d %{buildroot}{%{_gamesdatadir}/%{name},%{_gamesbindir}}
cp -pr data code %{name}.py %{buildroot}%{_gamesdatadir}/%{name}/

%{__cat} <<EOF > %{buildroot}%{_gamesbindir}/%{name}
#!/bin/sh
cd %{_gamesdatadir}/%{name}
./%{name}.py $@
EOF

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%name.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Categories=Game;ArcadeGame;
Name=SolarWolf
Comment=%{Summary}
EOF

%{__install} %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
%{__install} %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
%{__install} %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png


%files
%defattr(644,root,root,755)
%doc readme.txt
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/data
%{_gamesdatadir}/%{name}/code
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}/%{name}.py


%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 1.5-9mdv2011.0
+ Revision: 664871
- mass rebuild

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.5-8mdv2010.0
+ Revision: 433987
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.5-7mdv2009.0
+ Revision: 260877
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.5-6mdv2009.0
+ Revision: 252728
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 25 2008 Funda Wang <fwang@mandriva.org> 1.5-4mdv2008.1
+ Revision: 157784
- fix desktop entry

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Tue Aug 28 2007 Thierry Vignaud <tv@mandriva.org> 1.5-3mdv2008.0
+ Revision: 72276
- convert menu to XDG
- use %%mkrel

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - Import solarwolf



* Fri Aug 27 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.5-2mdk
- rebuild for new menu

* Wed Feb 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.5-1mdk
- 1.5

* Wed Jan 14 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.4-1mdk
- 1.4

* Sat Sep 27 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.3-1mdk
- 1.3

* Mon Aug 04 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2-1mdk
- initial mdk release
