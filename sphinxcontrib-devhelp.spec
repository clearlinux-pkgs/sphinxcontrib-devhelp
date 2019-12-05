#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : sphinxcontrib-devhelp
Version  : 1.0.1
Release  : 5
URL      : https://files.pythonhosted.org/packages/57/5f/bf9a0f7454df68a7a29033a5cf8d53d0797ae2e426b1b419e4622726ec7d/sphinxcontrib-devhelp-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/5f/bf9a0f7454df68a7a29033a5cf8d53d0797ae2e426b1b419e4622726ec7d/sphinxcontrib-devhelp-1.0.1.tar.gz
Source99 : https://files.pythonhosted.org/packages/57/5f/bf9a0f7454df68a7a29033a5cf8d53d0797ae2e426b1b419e4622726ec7d/sphinxcontrib-devhelp-1.0.1.tar.gz.asc
Summary  : No summary provided
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-devhelp-license = %{version}-%{release}
Requires: sphinxcontrib-devhelp-python = %{version}-%{release}
Requires: sphinxcontrib-devhelp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
=====================
sphinxcontrib-devhelp
=====================
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp_ document.

%package license
Summary: license components for the sphinxcontrib-devhelp package.
Group: Default

%description license
license components for the sphinxcontrib-devhelp package.


%package python
Summary: python components for the sphinxcontrib-devhelp package.
Group: Default
Requires: sphinxcontrib-devhelp-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-devhelp package.


%package python3
Summary: python3 components for the sphinxcontrib-devhelp package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sphinxcontrib-devhelp package.


%prep
%setup -q -n sphinxcontrib-devhelp-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554254220
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-devhelp
cp LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-devhelp/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-devhelp/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
