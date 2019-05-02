Name:		texlive-hyphen-russian
Version:	20190406
Release:	1
Summary:	Russian hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-russian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8
Requires:	texlive-ruhyphen

%description
Hyphenation patterns for Russian in T2A and UTF-8 encodings.
For 8-bit engines, the 'ruhyphen' package provides a number of
different pattern sets, as well as different (8-bit) encodings,
that can be chosen at format-generation time.  The UTF-8
version only provides the default pattern set.  A mechanism
similar to the one used for 8-bit patterns may be implemented
in the future.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-russian
%_texmf_language_def_d/hyphen-russian
%_texmf_language_lua_d/hyphen-russian

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-russian <<EOF
\%% from hyphen-russian:
russian loadhyph-ru.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-russian
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-russian <<EOF
\%% from hyphen-russian:
\addlanguage{russian}{loadhyph-ru.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-russian
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
