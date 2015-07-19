# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/perception
# catalog-date 2007-02-24 15:09:57 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-perception
Version:	20070224
Release:	10
Summary:	BibTeX style for the journal Perception
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/perception
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/perception.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/perception.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A product of custom-bib, provided simply to save others' time.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/perception/perception.bst
%doc %{_texmfdistdir}/doc/latex/perception/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070224-2
+ Revision: 754808
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070224-1
+ Revision: 719233
- texlive-perception
- texlive-perception
- texlive-perception
- texlive-perception

