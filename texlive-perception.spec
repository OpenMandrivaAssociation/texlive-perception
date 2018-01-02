Name:		texlive-perception
Version:	20170414
Release:	1
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
%{_texmfdistdir}/bibtex/bst/perception
%doc %{_texmfdistdir}/doc/bibtex/perception

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
