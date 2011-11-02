Name:		texlive-hyphen-russian
Version:	20111102
Release:	1
Summary:	Russian hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-russian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-hyphen-base
Requires:	texlive-hyph-utf8
Requires:	texlive-ruhyphen
Conflicts:	texlive-texmf <= 20110705-3
Requires(post):	texlive-hyphen-base

%description
Hyphenation patterns for Russian in T2A and UTF-8 encodings.
For 8-bit engines, the 'ruhyphen' package provides a number of
different pattern sets, as well as different (8-bit) encodings,
that can be chosen at format-generation time.  The UTF-8
version only provides the default pattern set.  A mechanism
similar to the one used for 8-bit patterns may be implemented
in the future.

%pre
    %_texmf_language_dat_pre
    %_texmf_language_def_pre
    %_texmf_language_lua_pre

%post
    %_texmf_language_dat_post
    %_texmf_language_def_post
    %_texmf_language_lua_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_pre
	%_texmf_language_def_pre
	%_texmf_language_lua_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_post
	%_texmf_language_def_post
	%_texmf_language_lua_post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-russian
%_texmf_language_def_d/hyphen-russian
%_texmf_language_lua_d/hyphen-russian

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-russian <<EOF
%% from hyphen-russian:
russian loadhyph-ru.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-russian <<EOF
%% from hyphen-russian:
\addlanguage{russian}{loadhyph-ru.tex}{}{2}{2}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-russian <<EOF
-- from hyphen-russian:
	['russian'] = {
		loader = 'loadhyph-ru.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-ru.pat.txt',
		hyphenation = 'hyph-ru.hyp.txt',
	},
EOF
