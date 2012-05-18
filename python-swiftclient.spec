%define name python-swiftclient
%define version 1.0
%define unmangled_version 1.0
%define unmangled_version 1.0
%define release 1

Summary: Client Library for OpenStack Object Storage API
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: Apache License (2.0)
Group: Development/Libraries
BuildRequires:  python-devel python-setuptools python-sphinx make
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: OpenStack, LLC. <openstack-admins@lists.launchpad.net>
Url: https://github.com/openstack/python-swiftclient

%description
Python bindings to the OpenStack Object Storage API
===================================================

This is a python client for the Swift API. There's a Python API (the
``swiftclient`` module), and a command-line script (``swift``).

Development takes place via the usual OpenStack processes as outlined
in the `OpenStack wiki`__.  The master repository is on GitHub__.

__ http://wiki.openstack.org/HowToContribute
__ http://github.com/openstack/python-swiftclient

This code is based on original the client previously included with
`OpenStack's swift`__ The python-swiftclient is licensed under the
Apache License like the rest of OpenStack.

__ http://github.com/openstack/swift

.. contents:: Contents:
   :local:


%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
