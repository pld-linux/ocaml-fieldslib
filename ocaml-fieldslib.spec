#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Syntax extension to define first class values representing record fields
Summary(pl.UTF-8):	Rozszerzenie składni do definiowania pierwszoklasowych wartości reprezentujących pola rekordów
Name:		ocaml-fieldslib
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/fieldslib/tags
Source0:	https://github.com/janestreet/fieldslib/archive/v%{version}/fieldslib-%{version}.tar.gz
# Source0-md5:	bda1a5ab1175366f77d6bcf43680c547
URL:		https://github.com/janestreet/fieldslib
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Syntax extension to define first class values representing record
fields, to get and set record fields, iterate and fold over all fields
of a record and create new record values.

This package contains files needed to run bytecode executables using
fieldslib library.

%description -l pl.UTF-8
Rozszerzenie składni do definiowania pierwszoklasowych wartości
reprezentujących pola rekordów, do pobierania i ustawiania pól
rekordów, iterowania i składania wszystkich pól rekordów oraz
tworzenia nowych wartości rekordów.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki fieldslib.

%package devel
Summary:	Generation of comparison functions from types - development part
Summary(pl.UTF-8):	Generowanie funkcji porównujących z typów - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
fieldslib library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki fieldslib.

%prep
%setup -q -n fieldslib-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/fieldslib/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/fieldslib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md
%dir %{_libdir}/ocaml/fieldslib
%{_libdir}/ocaml/fieldslib/META
%{_libdir}/ocaml/fieldslib/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/fieldslib/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/fieldslib/*.cmi
%{_libdir}/ocaml/fieldslib/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/fieldslib/fieldslib.a
%{_libdir}/ocaml/fieldslib/*.cmx
%{_libdir}/ocaml/fieldslib/*.cmxa
%endif
%{_libdir}/ocaml/fieldslib/dune-package
%{_libdir}/ocaml/fieldslib/opam
