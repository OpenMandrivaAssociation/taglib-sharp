Name: taglib-sharp
License:        LGPLv2
Group:          Development/Other
Summary:        Metadata library for most common movie and music formats 
Url:            http://download.banshee-project.org/taglib-sharp/
Version:        2.0.4.0
Release:        5
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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

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


%changelog
* Thu Apr 14 2011 Götz Waschk <waschk@mandriva.org> 2.0.4.0-1mdv2011.0
+ Revision: 652994
- new version
- add missing examples
- update build deps
- remove checks

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 2.0.3.7-3mdv2011.0
+ Revision: 567906
- fix deps
- split out devel package

* Sun Mar 21 2010 Funda Wang <fwang@mandriva.org> 2.0.3.7-1mdv2010.1
+ Revision: 525997
- update to new version 2.0.3.7

* Fri Feb 26 2010 Funda Wang <fwang@mandriva.org> 2.0.3.6-1mdv2010.1
+ Revision: 511427
- new version 2.0.3.6

* Thu Jan 28 2010 Götz Waschk <waschk@mandriva.org> 2.0.3.4-1mdv2010.1
+ Revision: 497524
- update to new version 2.0.3.4

* Thu Oct 15 2009 Götz Waschk <waschk@mandriva.org> 2.0.3.3-1mdv2010.0
+ Revision: 457512
- new version 2.0.3.3

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.0.3.2-2mdv2010.0
+ Revision: 427225
- rebuild

* Sat Feb 28 2009 Götz Waschk <waschk@mandriva.org> 2.0.3.2-1mdv2009.1
+ Revision: 346034
- new version
- reenable checks

* Tue Jan 27 2009 Götz Waschk <waschk@mandriva.org> 2.0.3.1-1mdv2009.1
+ Revision: 334034
- new version
- fix source URL

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.0.3.0-2mdv2009.0
+ Revision: 225608
- rebuild

* Wed Feb 20 2008 Götz Waschk <waschk@mandriva.org> 2.0.3.0-1mdv2008.1
+ Revision: 173330
- import taglib-sharp


