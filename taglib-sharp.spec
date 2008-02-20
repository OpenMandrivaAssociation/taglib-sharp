Name: taglib-sharp
License:        LGPLv2
Group:          Development/Other
Summary:        Metadata library for most common movie and music formats 
Url:            http://taglib-sharp.com/
Version:        2.0.3.0
Release:        %mkrel 1
Source0:        http://www.taglib-sharp.com/Download/%name-%{version}.tar.gz
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


%prep
%setup -q

%build
./configure --prefix=/usr --disable-docs
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT/usr/share/pkgconfig
mv $RPM_BUILD_ROOT/usr/lib/pkgconfig/* $RPM_BUILD_ROOT/usr/share/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS NEWS README
%_prefix/lib/mono/taglib-sharp
%_prefix/lib/mono/gac/taglib-sharp
%_prefix/lib/mono/gac/policy.2.0.taglib-sharp
%_prefix/share/pkgconfig/taglib-sharp.pc
