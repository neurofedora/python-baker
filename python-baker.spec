%global modname baker

%global commit 408295259ae5bfd36d639e104ed344c61d05e3c6
%global shortcommit %(c=%{commit}; echo ${c:0:12})

Name:           python-%{modname}
Version:        1.3
Release:        1.git%{shortcommit}%{?dist}
Summary:        Easy, powerful access to Python functions from the command line

# https://bitbucket.org/mchaput/baker/issues/36/include-license-file
License:        ASL 2.0
URL:            https://pypi.python.org/pypi/Baker
Source0:        https://bitbucket.org/mchaput/baker/get/%{commit}.tar.gz#/%{modname}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
Baker lets you easily add a command line interface to your Python functions
using a simple decorator, to create scripts with "sub-commands", similar to
Django's 'manage.py', 'svn', 'hg', etc.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-nose

%description -n python2-%{modname}
Baker lets you easily add a command line interface to your Python functions
using a simple decorator, to create scripts with "sub-commands", similar to
Django's 'manage.py', 'svn', 'hg', etc.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-nose

%description -n python3-%{modname}
Baker lets you easily add a command line interface to your Python functions
using a simple decorator, to create scripts with "sub-commands", similar to
Django's 'manage.py', 'svn', 'hg', etc.

Python 3 version.

%prep
%autosetup -n mchaput-%{modname}-%{shortcommit}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
pushd tests/
  PYTHONPATH=%{buildroot}%{python2_sitelib} nosetests-%{python2_version}
  # https://bitbucket.org/mchaput/baker/issues/35/test-bakerwriteconfig-fails-on-python3-35
  PYTHONPATH=%{buildroot}%{python3_sitelib} nosetests-%{python3_version} || :
popd

%files -n python2-%{modname}
%doc README.txt
%{python2_sitelib}/Baker*.egg-info/
%{python2_sitelib}/%{modname}.py*

%files -n python3-%{modname}
%doc README.txt
%{python3_sitelib}/Baker*.egg-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Tue Nov 24 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.3-1.git408295259ae5
- Initial package
