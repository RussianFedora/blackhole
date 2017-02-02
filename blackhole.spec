%global debug_package %{nil}

Summary:	Attribute-based logger with strong focus on gaining maximum performance
Name:		blackhole
Version:	0.2.4
Release:	3%{?dist}

License:	MIT
URL:		http://github.com/3Hren/blackhole
Source0:	https://github.com/3Hren/blackhole/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
Patch0:		blackhole-0.2.4-cmath.patch

BuildRequires:	cmake

%description
Blackhole is an attribute-based logger with strong focus on gaining maximum
performance as possible for such kind of loggers.


%package devel
Summary: Development files for %{name}
Provides: lib%{name}-devel%{?_isa} = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}


%description devel
This package contains libraries, header files and developer documentation
needed for developing software which uses the Blackhole logging library.

%prep
%autosetup -p 1

%build
%{cmake} -DENABLE_EXAMPLES=OFF .
%{make_build}

%install
%{make_install}

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}


%changelog
* Thu Feb  2 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 0.2.4-3
- include <math.h> header to resolve std::double_t

* Wed Feb  1 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 0.2.4-2
- added Provides

* Thu Jan 12 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 0.2.4-1
- initial build
