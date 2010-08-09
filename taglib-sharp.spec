Name: taglib-sharp
License:        LGPLv2
Group:          Development/Other
Summary:        Metadata library for most common movie and music formats 
Url:            http://download.banshee-project.org/taglib-sharp/
Version:        2.0.3.7
Release:        %mkrel 3
Source0:        http://download.banshee-project.org/%name/%version/%name-%{version}.tar.bz2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  mono-devel

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

%build
./configure --prefix=/usr --disable-docs
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS NEWS README
%_prefix/lib/mono/taglib-sharp
%_prefix/lib/mono/gac/taglib-sharp
%_prefix/lib/mono/gac/policy.2.0.taglib-sharp

%files devel
%defattr(-, root, root)
%_prefix/share/pkgconfig/taglib-sharp.pc
