Name:		texlive-seealso
Version:	1.2
Release:	1
Summary:	Improve the performance of \see macros with makeindex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/seealso
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seealso.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seealso.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seealso.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package amends the \see and \seealso macros that are used
in building indexes with makeindex, to deal with repetitions,
and to ensure page numbers are present in the actual index
entries. on these indirecty.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/seealso
%doc %{_texmfdistdir}/doc/latex/seealso
#- source
%doc %{_texmfdistdir}/source/latex/seealso

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
