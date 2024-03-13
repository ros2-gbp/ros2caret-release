%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-ros2caret
Version:        0.5.0
Release:        7%{?dist}%{?release_suffix}
Summary:        ROS ros2caret package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python3-tabulate
Requires:       ros-humble-ament-index-python
Requires:       ros-humble-caret-analyze
Requires:       ros-humble-caret-msgs
Requires:       ros-humble-ros2cli
Requires:       ros-humble-tracetools-trace
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-caret-analyze
BuildRequires:  ros-humble-caret-msgs
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-ros2cli
BuildRequires:  ros-humble-tracetools-trace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-mock
BuildRequires:  ros-humble-ament-copyright
BuildRequires:  ros-humble-ament-flake8
BuildRequires:  ros-humble-ament-mypy
BuildRequires:  ros-humble-ament-pep257
%endif

%description
ROS 2 CLI package for caret

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Wed Mar 13 2024 ymski <yamasaki@isp.co.jp> - 0.5.0-7
- Autogenerated by Bloom

* Tue Feb 27 2024 ymski <yamasaki@isp.co.jp> - 0.5.0-6
- Autogenerated by Bloom

* Tue Feb 27 2024 ymski <yamasaki@isp.co.jp> - 0.5.0-5
- Autogenerated by Bloom

* Tue Feb 27 2024 ymski <yamasaki@isp.co.jp> - 0.5.0-4
- Autogenerated by Bloom

* Tue Feb 27 2024 ymski <yamasaki@isp.co.jp> - 0.5.0-3
- Autogenerated by Bloom

