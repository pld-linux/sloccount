Summary:	Measures source lines of code (SLOC) in programs
Summary(pl):	Mierzenie liczby linii kodu (SLOC) ¼ród³owego programów
Name:		sloccount
Version:	2.23
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.dwheeler.com/sloccount/%{name}-%{version}.tar.gz
# Source0-md5:	991e012b636963f70ff31cadc2541b32
URL:		http://www.dwheeler.com/sloccount/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SLOCCount (pronounced "sloc-count") is a suite of programs for
counting physical source lines of code (SLOC) in potentially large
software systems (thus, SLOCCount is a "software metrics tool" or
"software measurement tool"). SLOCCount can count physical SLOC for a
wide number of languages; listed alphabetically, they are: Ada,
Assembly, awk, Bourne shell, C, C++, C shell, COBOL, Expect, Fortran,
Java, lex/flex, LISP (including Scheme), ML (including OCaml),
Modula-3, Objective-C, Pascal, Perl, PHP, Python, sed, TCL, and Yacc.
SLOCCount can automatically determine if a file is a source code file
or not, and if so, which language it's written in. As a result, you
can analyze large systems completely automatically; it's been used to
examine entire GNU/Linux distributions, for example. SLOCCount also
includes some report-generating tools to collect the data generated
and present it in several different formats. Normally you can just run
"sloccount DIRECTORY" and all the source code in the directory and its
descendants will be counted.

%description -l pl
SLOCCount (wymawiane tak jak "sloc-count") to zestaw programów do
liczenia fizycznych linii kodu (SLOC) ¼ród³owego w potencjalnie du¿ych
systemach oprogramowania (w ten sposób SLOCCount jest "narzêdziem
miary oprogramowania" lub "narzêdziem mierz±cym oprogramowanie").
SLOCCount mo¿e liczbyæ fizyczne linie kodu dla wielu jêzyków;
alfabetycznie s± to: Ada, asembler, awk, pow³oka Bourne'a, C, C++,
pow³oka C, COBOL, Expect, Fortran, Java, lex/flex, LISP (wraz ze
Scheme), ML (w³±czaj±c OCamla), Modula-3, Objective-C, Pascal, perl,
PHP, Python, sed, TCL oraz Yacc. SLOCCount potrafi automatycznie
okre¶liæ, czy plik jest kodem ¼ród³owym, a je¶li tak, to w jakim
jêzyku jest napisany. W efekcie mo¿e ca³kowicie automatycznie
analizowaæ du¿e systemy; bywa u¿ywany do okre¶lenia wielko¶ci ca³ych
dystrybucji GNU/Linuksa. SLOCCount zawiera tak¿e trochê narzêdzi do
generowania raportów - zbieraj±cych wygenerowane dane i prezentuj±cych
je w ró¿nych innych formatach. Zwykle wystarczy uruchomiæ "sloccount
KATALOG", a ca³y kod ¼ród³owy w katalogu i jego katalogach zostanie
podliczony.

%prep
%setup -q

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
