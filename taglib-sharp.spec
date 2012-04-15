Name: taglib-sharp
License:        LGPLv2
Group:          Development/Other
Summary:        Metadata library for most common movie and music formats 
Url:            http://download.banshee-project.org/taglib-sharp/
Version:        2.0.4.0
Release:        %mkrel 2
Source0:        http://download.banshee-project.org/%name/%version/%name-%{version}.tar.bz2
#gw missing from the tarball
Source1: extractKey.cpp
Source2: listData.cpp
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  mono-devel
BuildRequires:  libexiv-devel

%description
TagLib# is a metadata or "tag" reader and writer library that supports
the most common movie and music formats, abstracting away
format specificity. TagLib# offers either a common API for all
formats or access to specific APIs for a given format.

Authors:
Brian Nickel <brian.nickel@gmail.com>
Aaron Bockover <abockover@novell.com>

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
TagLib# is a metadata or "tag" reader and writer library that supports
the most common movie and music formats, abstracting away
format specificity. TagLib# offers either a common API for all
formats or access to specific APIs for a given format.

Authors:
Brian Nickel <brian.nickel@gmail.com>
Aaron Bockover <abockover@novell.com>

%prep
%setup -q
cp %SOURCE1 %SOURCE2 examples/

%build
./configure --prefix=/usr --disable-docs
make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS NEWS README
%_prefix/lib/mono/taglib-sharp
%_prefix/lib/mono/gac/taglib-sharp
%_prefix/lib/mono/gac/policy.2.0.taglib-sharp

%files devel
%defattr(-, root, root)
%_prefix/share/pkgconfig/taglib-sharp.pc
