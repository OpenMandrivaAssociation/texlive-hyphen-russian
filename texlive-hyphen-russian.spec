%global tl_name hyphen-russian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Russian hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-russian
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-russian.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive(ruhyphen)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Russian in T2A and UTF-8 encodings. For 8-bit
engines, the 'ruhyphen' package provides a number of different pattern
sets, as well as different (8-bit) encodings, that can be chosen at
format-generation time. The UTF-8 version only provides the default
pattern set. A mechanism similar to the one used for 8-bit patterns may
be implemented in the future.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-russian:
russian loadhyph-ru.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-russian:
\addlanguage{russian}{loadhyph-ru.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-russian:
['russian'] = {
	loader = 'loadhyph-ru.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-ru.pat.txt',
	hyphenation = 'hyph-ru.hyp.txt',
},
TL_HYPHEN_EOF
