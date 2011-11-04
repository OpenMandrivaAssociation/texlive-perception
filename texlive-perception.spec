# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/perception
# catalog-date 2007-02-24 15:09:57 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-perception
Version:	20070224
Release:	1
Summary:	BibTeX style for the journal Perception
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/perception
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/perception.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/perception.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
A product of custom-bib, provided simply to save others' time.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/perception/perception.bst
%doc %{_texmfdistdir}/doc/latex/perception/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
