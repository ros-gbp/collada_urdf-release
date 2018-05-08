Name:           ros-lunar-collada-urdf
Version:        1.12.12
Release:        0%{?dist}
Summary:        ROS collada_urdf package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/collada_urdf
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp
Requires:       collada-dom-devel
Requires:       ros-lunar-collada-parser
Requires:       ros-lunar-geometric-shapes
Requires:       ros-lunar-resource-retriever
Requires:       ros-lunar-rosconsole
Requires:       ros-lunar-urdf
Requires:       urdfdom-devel
Requires:       urdfdom-headers-devel
BuildRequires:  assimp-devel
BuildRequires:  collada-dom-devel
BuildRequires:  eigen3-devel
BuildRequires:  ros-lunar-angles
BuildRequires:  ros-lunar-catkin >= 0.5.68
BuildRequires:  ros-lunar-cmake-modules
BuildRequires:  ros-lunar-collada-parser
BuildRequires:  ros-lunar-geometric-shapes
BuildRequires:  ros-lunar-resource-retriever
BuildRequires:  ros-lunar-rosconsole
BuildRequires:  ros-lunar-urdf
BuildRequires:  urdfdom-devel
BuildRequires:  urdfdom-headers-devel

%description
This package contains a tool to convert Unified Robot Description Format (URDF)
documents into COLLAborative Design Activity (COLLADA) documents. Implements
robot-specific COLLADA extensions as defined by
http://openrave.programmingvision.com/index.php/Started:COLLADA

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

