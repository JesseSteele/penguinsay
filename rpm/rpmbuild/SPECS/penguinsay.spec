Name:           penguinsay
Version:        1.0.0
Release:        1%{?dist}
Summary:        The talking penguin

License:        GPL
URL:            https://github.com/JesseSteele/penguinsay

BuildArch:      noarch
Requires:       bash

%description
Penguin talkback written in Linux for Linux

%prep
echo "####################################################
We are creating the talking penguin RPM installer...
Other commands could go here...
####################################################"

%build
# We could put some commands here if we needed to build from source

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{_sourcedir}/penguinsay.sh %{buildroot}/usr/bin/penguinsay

%files
/usr/bin/penguinsay

%changelog
* Thu Jan 01 1970 Jesse Steele <codes@jessesteele.com> - 1.0.0-1
- Something started, probably with v1.0.0-1