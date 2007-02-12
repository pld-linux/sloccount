Summary:	Measures source lines of code (SLOC) in programs
Summary(pl.UTF-8):	Mierzenie liczby linii kodu (SLOC) źródłowego programów
Name:		sloccount
Version:	2.26
Release:	2
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.dwheeler.com/sloccount/%{name}-%{version}.tar.gz
# Source0-md5:	09abd6e2a016ebaf7552068a1dba1249
Patch0:		%{name}-nemerle.patch
URL:		http://www.dwheeler.com/sloccount/
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SLOCCount (pronounced "sloc-count") is a suite of programs for
counting physical source lines of code (SLOC) in potentially large
software systems (thus, SLOCCount is a "software metrics tool" or
"software measurement tool"). SLOCCount can count physical SLOC for a
wide number of languages; listed alphabetically, they are: Ada,
Assembly, awk, Bourne shell, C, C++, C shell, COBOL, Expect, Fortran,
Java, lex/flex, LISP (including Scheme), ML (including OCaml),
Modula-3, Objective-C, Pascal, Perl, PHP, Python, sed, Tcl, and Yacc.
SLOCCount can automatically determine if a file is a source code file
or not, and if so, which language it's written in. As a result, you
can analyze large systems completely automatically; it's been used to
examine entire GNU/Linux distributions, for example. SLOCCount also
includes some report-generating tools to collect the data generated
and present it in several different formats. Normally you can just run
"sloccount DIRECTORY" and all the source code in the directory and its
descendants will be counted.

%description -l pl.UTF-8
SLOCCount (wymawiane tak jak "sloc-count") to zestaw programów do
liczenia fizycznych linii kodu (SLOC) źródłowego w potencjalnie dużych
systemach oprogramowania (w ten sposób SLOCCount jest "narzędziem
miary oprogramowania" lub "narzędziem mierzącym oprogramowanie").
SLOCCount może liczyć fizyczne linie kodu dla wielu języków;
alfabetycznie są to: Ada, asembler, awk, powłoka Bourne'a, C, C++,
powłoka C, COBOL, Expect, Fortran, Java, lex/flex, LISP (wraz ze
Scheme), ML (włączając OCamla), Modula-3, Objective-C, Pascal, perl,
PHP, Python, sed, Tcl oraz Yacc. SLOCCount potrafi automatycznie
określić, czy plik jest kodem źródłowym, a jeśli tak, to w jakim
języku jest napisany. W efekcie może całkowicie automatycznie
analizować duże systemy; bywa używany do określenia wielkości całych
dystrybucji GNU/Linuksa. SLOCCount zawiera także trochę narzędzi do
generowania raportów - zbierających wygenerowane dane i prezentujących
je w różnych innych formatach. Zwykle wystarczy uruchomić "sloccount
KATALOG", a cały kod źródłowy w katalogu i jego katalogach zostanie
podliczony.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install_programs install_man \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc sloccount.html README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
