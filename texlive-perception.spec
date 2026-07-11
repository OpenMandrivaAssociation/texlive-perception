%global tl_name perception
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	BibTeX style for the journal Perception
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/perception
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/perception.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/perception.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A product of custom-bib, provided simply to save others' time.

