Summary:	Measures source lines of code (SLOC) in programs
Name:		sloccount
Version:	2.21
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.dwheeler.com/sloccount/%{name}-%{version}.tar.gz
URL:		http://www.dwheeler.com/sloccount/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SLOCCount (pronounced "sloc-count") is a suite of programs for
counting physical source lines of code (SLOC) in potentially large
software systems (thus, SLOCCount is a "software metrics tool" or
"software measurement tool"). SLOCCount can count physical SLOC for a
wide number of languages; listed alphabetically, they are: Ada,
Assembly, awk, Bourne shell, C, C++, C shell, COBOL, Expect, Fortran,
Java, lex/flex, LISP (including Scheme), Modula-3, Objective-C,
Pascal, Perl, PHP, Python, sed, TCL, and Yacc. SLOCCount can
automatically determine if a file is a source code file or not, and if
so, which language it's written in. As a result, you can analyze large
systems completely automatically; it's been used to examine entire
GNU/Linux distributions, for example. SLOCCount also includes some
report-generating tools to collect the data generated and present it
in several different formats. Normally you can just run "sloccount
DIRECTORY" and all the source code in the directory and its
descendants will be counted.

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
