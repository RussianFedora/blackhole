%global debug_package %{nil}

Summary:	Attribute-based logger with strong focus on gaining maximum performance
Name:		blackhole
Version:	0.2.4
Release:	1%{?dist}

License:	MIT
URL:		http://github.com/3Hren/blackhole
Source0:	%{name}-%{version}.tar.xz

BuildRequires:	cmake

%description
Blackhole is an attribute-based logger with strong focus on gaining maximum
performance as possible for such kind of loggers.


%package devel
Summary: Development files for %{name}


%description devel
This package contains libraries, header files and developer documentation
needed for developing software which uses the Blackhole logging library.

%prep
%autosetup

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
* Thu Jan 12 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 0.2.4-1
- initial build
