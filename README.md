# penguinsay
## The talking penguin
Penguin talkback written in Linux for Linux

## Create the simple Linux install package for `penguinsay`
This is a guide to create an installer package for the `penguinsay` command on:
1. Arch (Manjaro, Black Arch, et al)
2. Debian (Ubuntu, Kali, Mint, et al)
3. RPM (OpenSUSE, RedHat/CentOS, Fedora, et al)

Working examples for each already resides in this repository

### Create and install the `penguinsay` package directly from this repo

| **Arch** :$ (& Manjaro, Black Arch)

```console
git clone https://github.com/JesseSteele/penguinsay.git
cd penguinsay/arch
makepkg -si
```

| **Debian** :$ (& Ubuntu, Kali, Mint)

```console
git clone https://github.com/JesseSteele/penguinsay.git
cd penguinsay/deb
dpkg-deb --build penguinsay
sudo dpkg -i penguinsay.deb
```

| **RedHat/CentOS** :$ (& Fedora)

```console
git clone https://github.com/JesseSteele/penguinsay.git
sudo dnf update
sudo dnf install rpm-build rpmdevtools
cp -rf penguinsay/rpm/rpmbuild ~/
rpmbuild -ba ~/rpmbuild/SPECS/penguinsay.spec
ls ~/rpmbuild/RPMS/noarch/
sudo rpm -i ~/rpmbuild/RPMS/noarch/penguinsay-1.0.0-1.noarch.rpm  # Change filename if needed
rm -rf ~/rpmbuild
```

| **OpenSUSE** :$ (& Tumbleweed)

```console
git clone https://github.com/JesseSteele/penguinsay.git
cd penguinsay/rpm
sudo zypper update
sudo zypper install rpm-build rpmdevtools
cp -r rpmbuild ~/
rpmbuild -ba ~/rpmbuild/SPECS/penguinsay.spec
ls ~/rpmbuild/RPMS/noarch/
sudo rpm -i ~/rpmbuild/RPMS/noarch/penguinsay-1.0.0-1.noarch.rpm  # Change filename if needed
rm -rf ~/rpmbuild
```

## Detailed instructions per architecture
Instructions explain each in detail to create these packages from scratch...

- These instructions presume you can access [penguinsay.sh](https://github.com/JesseSteele/penguinsay/blob/main/penguinsay.sh)

### I. Arch Linux Package (`penguinsay-1.0.0-1-any.pkg.tar.zst`)
*Arch package directory structure:*

| **`arch/`** :

```
arch/
├─ penguinsay.sh
└─ PKGBUILD
```

- Create directory: `arch`
- In `arch/` create file: `PKGBUILD`

| **`arch/PKGBUILD`** :

```
# Maintainer: Jesse Steele <codes@jessesteele.com>
pkgname=penguinsay
pkgver=1.0.0
pkgrel=1
pkgdesc="Penguin talkback written in Linux for Linux"
url="https://github.com/JesseSteele/penguinsay"
#arch=('x86_64')
arch=('any')
license=('GPL')
depends=('bash')  # Dependency on bash package
#source=("$pkgname-$pkgver.sh")
source=("$pkgname.sh")
sha256sums=('SKIP')

package() {
  cd "$srcdir"
  install -Dm755 "$srcdir/$source" "$pkgdir/usr/bin/$pkgname"
}
```

- Place file `penguinsay.sh` in the same directory as `PKGBUILD`
- Build package:
  - Navigate to directory `arch/`
  - Run this, then the package will be built, then installed with `pacman`:

| **Build & install Arch package** :$ (in one command)

```console
makepkg -si
```

- Use this to build and install in two steps:

| **Build, *then* install Arch package** :$ (first line produces the `.pkg.tar.zst` file for repos or manual install)

```console
makepkg
sudo pacman -U penguinsay-1.0.0-1-any.pkg.tar.zst
```

- Special notes about Arch:
  - We don't need to resolve any dependencies, we can omit the `-s` flag with `makepkg`
    - This package only needs `bash` as a dependency, which should already be installed merely to execute the script
      - `depends=('bash')` is redundant and only serves as an example in `PKGBUILD`
  - The name of the directory containing the package files does not matter
  - `PKGBUILD` is the instruction file, not a directory as might be expected with other package builders
  - `makepkg` must be run from the same directory containing `PKGBUILD`
  - The `.pkg.tar.zst` file will appear inside the containing directory

| **Remove Arch package** :$ (optional)

```console
sudo pacman -R penguinsay
```

### II. Debian Package (`penguinsay.deb`)
*Debian package directory structure:*

| **`deb/`** :

```
deb/
└─ penguinsay/
   ├─ DEBIAN/
   │  └─ control
   └─ usr/
      └─ local/
         └─ bin/
            └─ penguinsay
```

- Create directories: `deb/penguinsay/DEBIAN`
- In `DEBIAN/` create file: `control`

| **`deb/penguinsay/DEBIAN/control`** :

```
Package: penguinsay
Version: 1.0.0
Section: base
Priority: optional
#Architecture: amd64
Architecture: all
Maintainer: Jesse Steele <codes@jessesteele.com>
Depends: bash (>= 4.0)
Description: Penguin talkback written in Linux for Linux

```

- Create directories: `deb/penguinsay/usr/local/bin/`
- Rename and place file `penguinsay.sh` at `deb/penguinsay/usr/local/bin/penguinsay`
  - Make it executable with :$ `chmod +x deb/penguinsay/usr/local/bin/penguinsay`
- Build package:
  - Navigate to directory `deb/`
  - Run this, then the package will be built, then installed:

| **Build, *then* install Debian package** :$

```console
dpkg-deb --build penguinsay  # Create the .deb package
sudo dpkg -i penguinsay.deb  # Install the package
```

- Special notes about Debian
  - The script file at `usr/local/bin/penguinsay` must be pre-named and already executable
    - This is because this installer does not use a `postinst` script like some `.deb` packages may
    - This package simply places the files as they appear in the `DEBIAN/` directory
  - Debian packages require files to be named and at locations like `usr/local/bin/penguinsay`
    - This defines where they will be installed to relative to `/` on the machine
  - The directory of the package files (`penguinsay/`) will be the same as the package installer's `.deb` basename
  - The package installer will appear at `penguinsay.deb` in the same directory as (`penguinsay/`) regardless of the PWD from where the `dpkg-deb --build` command was run
    - For `deb/penguinsay` it will be at `deb/penguinsay.deb`

| **Remove Debian package** :$ (optional)

```console
sudo apt-get remove penguinsay
```

### III. RPM Package (`penguinsay-1.0.0-1.noarch.rpm`)
*RPM package directory structure:*

| **`rpm/`** :

```
rpm/
└─ rpmbuild/
   ├─ SPECS/
   │  └─ penguinsay.spec
   └─ SOURCES/
      └─ penguinsay.sh
```

- Create directories: `rpm/rpmbuild/SPECS`
- In `SPECS/` create file: `penguinsay.spec`

| **`rpm/rpmbuild/SPECS/penguinsay.spec`** :

```
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
mkdir -p %{buildroot}/usr/local/bin
install -m 755 %{_sourcedir}/penguinsay.sh %{buildroot}/usr/local/bin/penguinsay

%files
/usr/local/bin/penguinsay

%changelog
-------------------------------------------------------------------
Thu Jan 01 00:00:00 UTC 1970 codes@jessesteele.com
- Something started, probably with v1.0.0-1
```

- Create directory: `rpm/rpmbuild/SOURCES/`
- Place file `penguinsay.sh` in directory `rpm/rpmbuild/SOURCES/`
- Install the `rpm-build` and `rpmdevtools` packages

| **RedHat/CentOS** :$

```console
sudo dnf update
sudo dnf install rpm-build rpmdevtools
```

| **OpenSUSE** :$

```console
sudo zypper update
sudo zypper install rpm-build rpmdevtools
```

- Build package:
  - Navigate to directory `rpm/`
  - Run the following commands:

| **Build, *then* install RPM package** :$

```console
cp -r rpmbuild ~/
rpmbuild -ba ~/rpmbuild/SPECS/penguinsay.spec                     # Create the .rpm package
ls ~/rpmbuild/RPMS/noarch/                                        # Check the .rpm filename
sudo rpm -i ~/rpmbuild/RPMS/noarch/penguinsay-1.0.0-1.noarch.rpm  # Install the package (filename may be different)
```

- Special notes about RPM:
  - RPM requires the build be done from `~/rpmbuild/`
  - The resulting `.rpm` fill will be at: `~/rpmbuild/RPMS/noarch/penguinsay-1.0.0-1.noarch.rpm`
    - This file might actually have a different name, but should be in the same directory (`~/rpmbuild/RPMS/noarch/`)
  - `noarch` means it works on any architecture
    - This part of the filename was set in the `.spec` file with `BuildArch: noarch`
  - The `%changelog` is for OpenSUSE's `zypper`
    - RedHat/CentOS may want the date line like this:
      - `* Thu Jan 01 1970 Jesse Steele <codes@jessesteele.com> - 1.0.0-1`

| **Remove RedHat/CentOS package** :$ (optional)

```console
sudo dnf remove penguinsay
```

| **Remove OpenSUSE package** :$ (optional)

```console
sudo zypper remove penguinsay
```