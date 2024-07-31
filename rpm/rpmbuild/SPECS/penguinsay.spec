Name:           penguinsay
Version:        1.0.0
Release:        1%{?dist}
Summary:        The talking penguin

License:        GPL
URL:            https://github.com/JesseSteele/penguinsay

BuildArch:      noarch
BuildRequires:  bash
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
mkdir -p %{buildroot}/usr/local/bin
install -m 755 %{_sourcedir}/penguinsay.sh %{buildroot}/usr/local/bin/penguinsay

%files
/usr/local/bin/penguinsay

%changelog