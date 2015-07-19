# revision 33483
# category Package
# catalog-ctan /macros/latex/contrib/pas-tableur
# catalog-date 2014-04-17 19:41:18 +0200
# catalog-license lppl
# catalog-version 1.06
Name:		texlive-pas-tableur
Version:	1.06
Release:	4
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
%{_texmfdistdir}/tex/latex/pas-tableur/pas-tableur.sty
%doc %{_texmfdistdir}/doc/latex/pas-tableur/README
%doc %{_texmfdistdir}/doc/latex/pas-tableur/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/pas-tableur/pas-tableur.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
