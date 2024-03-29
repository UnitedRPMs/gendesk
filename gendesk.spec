%define debug_package %{nil}

Name:    gendesk
Version: 1.0.9
Release: 1%{?gver}%{dist}
Summary: Utility for generating desktop files
Group:   Development/Tools
License: MIT
URL:     http://gendesk.roboticoverlords.org/
Source0: http://roboticoverlords.org/%{name}/%{name}-%{version}.tar.xz
Source1: http://roboticoverlords.org/images/default.png
#-------------------------------------
BuildRequires: golang
BuildRequires: git
#-------------------------------------

%description
Utility for generating desktop files

%prep
%autosetup -n %{name}-%{version}

#GOPATH=`pwd` go get -d -v

%build
#GOPATH=`pwd` go build
#GOPATH=`pwd` 
go build -mod=vendor -buildmode=pie -gccgoflags="-s -w $LDFLAGS"


%install
  mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/
  install -Dm755 "%{name}" "$RPM_BUILD_ROOT/usr/bin/%{name}"
  install -Dm644 %{S:1} "$RPM_BUILD_ROOT/usr/share/pixmaps/"
  install -Dm644 "%{name}.1.gz" "$RPM_BUILD_ROOT/usr/share/man/man1/%{name}.1.gz"

%files
%license LICENSE
%{_bindir}/gendesk
%{_mandir}/man1/gendesk.1.gz
%{_datadir}/pixmaps/default.png


%changelog

* Thu Dec 23 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.0.9-1
- Updated to 1.0.9

* Sat Mar 20 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.0.8-1
- Updated to 1.0.8

* Sat Aug 08 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.0.6-1
- Updated to 1.0.6

* Sat Jan 25 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.0.5-1
- Updated to 1.0.5

* Wed Sep 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.0.4-1
- Updated to 1.0.4

* Sat Dec 22 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.0.2-1
- Updated to 1.0.2

* Tue Nov 20 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.0.1-1
- Updated to 1.0.1

* Tue Sep 26 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 0.6.5-1
- Initial build
