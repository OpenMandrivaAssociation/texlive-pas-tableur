Name:		texlive-pas-tableur
Version:	2.01
Release:	1
Summary:	Create a spreadsheet layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pas-tableur
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pas-tableur.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pas-tableur.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands for creating a grid of
rectangles, and commands for populating locations in the grid.
PGF/TikZ is used for placement and population of the cells.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pas-tableur
%doc %{_texmfdistdir}/doc/latex/pas-tableur

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
