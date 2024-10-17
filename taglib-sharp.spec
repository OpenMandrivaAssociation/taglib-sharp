%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Metadata library for most common movie and music formats
Name:		taglib-sharp
Version:	2.0.4.0
Release:	13
License:	LGPLv2+
Group:		Development/Other
Url:		https://download.banshee-project.org/taglib-sharp/
Source0:	http://download.banshee-project.org/%name/%version/%name-%{version}.tar.bz2
#gw missing from the tarball
Source1:	extractKey.cpp
Source2:	listData.cpp
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(mono-nunit)

%description
TagLib# is a metadata or "tag" reader and writer library that supports
the most common movie and music formats, abstracting away
format specificity. TagLib# offers either a common API for all
formats or access to specific APIs for a given format.

%files
%doc AUTHORS NEWS README
%{_prefix}/lib/mono/taglib-sharp
%{_prefix}/lib/mono/gac/taglib-sharp
%{_prefix}/lib/mono/gac/policy.2.0.taglib-sharp

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for taglib-sharp
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
TagLib# is a metadata or "tag" reader and writer library that supports
the most common movie and music formats, abstracting away
format specificity. TagLib# offers either a common API for all
formats or access to specific APIs for a given format.

%files devel
%{_datadir}/pkgconfig/taglib-sharp.pc

#----------------------------------------------------------------------------

%prep
%setup -q
cp %{SOURCE1} %{SOURCE2} examples/

%build
./configure --prefix=/usr --disable-docs
make

%install
%makeinstall_std

