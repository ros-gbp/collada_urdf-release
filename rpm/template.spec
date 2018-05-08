Name:           ros-lunar-collada-parser
Version:        1.12.12
Release:        0%{?dist}
Summary:        ROS collada_parser package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/collada_parser
Source0:        %{name}-%{version}.tar.gz

Requires:       collada-dom-devel
Requires:       ros-lunar-class-loader
Requires:       ros-lunar-rosconsole
Requires:       ros-lunar-urdf
Requires:       ros-lunar-urdf-parser-plugin
BuildRequires:  collada-dom-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-class-loader
BuildRequires:  ros-lunar-rosconsole
BuildRequires:  ros-lunar-urdf
BuildRequires:  ros-lunar-urdf-parser-plugin
BuildRequires:  urdfdom-headers-devel

%description
This package contains a C++ parser for the Collada robot description format. The
parser reads a Collada XML robot description, and creates a C++ URDF model.
Although it is possible to directly use this parser when working with Collada
robot descriptions, the preferred user API is found in the urdf package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Tue May 08 2018 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.12-0
- Autogenerated by Bloom

* Tue Apr 17 2018 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.11-0
- Autogenerated by Bloom

* Tue Jun 27 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.10-2
- Autogenerated by Bloom

* Mon Jun 26 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.10-1
- Autogenerated by Bloom

* Mon Jun 26 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.10-0
- Autogenerated by Bloom

