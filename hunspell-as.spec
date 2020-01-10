Name: hunspell-as
Summary: Assamese hunspell dictionaries
Version: 1.0.3
Release: 9%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/files/2318/4/as_IN.oxt
URL: http://extensions.services.openoffice.org/project/AssameseDict
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Assamese hunspell dictionaries.

%prep
%setup -q -c -n hunspell-as

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p as_IN.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%files
%doc README_as_IN.txt COPYING COPYING.MPL COPYING.GPL COPYING.LGPL

%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.3-9
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Parag <pnemade@redhat.com> - 1.0.3-6
- spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 29 2009 Parag <pnemade@redhat.com> - 1.0.3-2
- Fix source issue in cvs

* Tue Apr 28 2009 Caolan McNamara <caolanm@redhat.com> - 1.0.3-1
- initial version
