Summary:	The Unix version of the old classic game Digger
Summary(pl):	Uniksowa wersja klasycznej gry Digger
Name:		digger
Version:	20020314
Release:	1
License:	(C) Windmill Software 1983
Group:		Applications/Games/Arcade
Source0:	http://www.digger.org/%{name}-%{version}.tar.gz
NoSource:	0
Patch0:		%{name}-optflags.patch
Patch1:		%{name}-fix_gcc_3.patch
URL:		http://www.digger.org/
BuildRequires:	SDL-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Unix version of the old classic game Digger. It has many
new features including:
- Exit button
- Optional VGA graphics
- Recording and playback
- Real time speed control
- Keyboard redefinition
- Gauntlet mode
- Two player simultaneous mode

%description -l pl
Uniksowa wersja starej klasycznej gry Digger. Posiada wiele nowych
mo¿liwo¶ci takich jak:
- Przycisk wyj¶cia
- Opcjonalna grafika VGA
- Nagrywanie i odtwarzanie sesji
- Kontrola prêdko¶ci w czasie rzeczywistym
- Przedefiniowanie klawiatury
- Tryb Próby
- Tryb dwóch graczy

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%{__make} -f Makefile.sdl \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}.txt
%attr(755,root,root) %{_bindir}/%{name}
