%global _hardened_build 1

Name:           libvarlink
Version:        18
Release:        3%{?dist}
Summary:        Varlink C Library
License:        ASL 2.0
URL:            https://github.com/varlink/%{name}
Source0:        https://github.com/varlink/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  gcc

%description
Varlink C Library

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        util
Summary:        Varlink command line tools

%description    util
The %{name}-util package contains varlink command line tools.

%prep
%setup -q

%build
%meson
%meson_build

%check
export LC_CTYPE=C.utf8
%meson_test

%install
%meson_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/libvarlink.so.*

%files util
%{_bindir}/varlink
%{_datadir}/bash-completion/completions/varlink
%{_datadir}/vim/vimfiles/after/*

%files devel
%{_includedir}/varlink.h
%{_libdir}/libvarlink.so
%{_libdir}/pkgconfig/libvarlink.pc

%changelog
* Tue Jun 18 2019 Lokesh Mandvekar <lsm5@redhat.com> - 18-3
- Resolves: #1721229 - add gating.yaml

* Mon Jun 17 2019 Lokesh Mandvekar <lsm5@redhat.com> - 18-2
- Resolves: #1721229 - add tests

* Mon Jun 17 2019 Lokesh Mandvekar <lsm5@redhat.com> - 18-1
- Resolves: #1721229 - bump to v18

* Tue Nov 06 2018 Harald Hoyer <harald@redhat.com> - 16-1
- libvarlink 16
- fixed coverity issues
- Resolves: #1638294 - Interface name validation rule update

* Wed Oct 10 2018 <kay@redhat.com> - 15-1
- libvarlink 15
- Resolves: #1638294 - Interface name validation rule update

* Mon Aug 13 2018 Lokesh Mandvekar <lsm5@redhat.com> - 12-2
- Resolves: #1615546 - BR: python3-devel

* Mon Jul 16 2018 <kay@redhat.com> - 12-1
- libvarlink 12

* Sun Jun 17 2018 <kay@redhat.com>
- libvarlink 11

* Sat May 12 2018  <kay@redhat.com>
- libvarlink 10

* Fri Apr 13 2018 <kay@redhat.com>
- libvarlink 9

* Thu Apr 12 2018 <kay@redhat.com>
- libvarlink 8

* Mon Mar 26 2018 <kay@redhat.com>
- libvarlink 7

* Mon Mar 26 2018 <kay@redhat.com>
- libvarlink 6

* Fri Mar 23 2018 <kay@redhat.com>
- libvarlink 5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Harald Hoyer <harald@redhat.com> - 1-2
- bump release

* Fri Feb  2 2018 <kay@redhat.com>
- libvarlink 1
