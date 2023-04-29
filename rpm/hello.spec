Name:     hello
Version:  2.10
Release:  2%{?dist}
Summary:  The "Hello World" program from GNU
License:  GPLv3+
URL:      http://ftp.gnu.org/gnu/hello
Source0: https://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz

BuildRequires: gettext
BuildRequires: automake

Requires(post): info
Requires(preun): info

%description
The "Hello World" program, done with all bells and whistles of a proper FOSS
project, including configuration, build, internationalization, help files, etc.

%prep
%autosetup

%build
echo OOOOOOOOOOOOOOOOOOOOOOOOOOO
pwd
ls -la
%configure
%make_build

%install
%make_install
%find_lang %{name}
rm -f %{buildroot}/%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files -f %{name}.lang
%{_mandir}/man1/hello.1.*
%{_infodir}/hello.info.*
%{_bindir}/hello

%doc AUTHORS ChangeLog NEWS README THANKS TODO
%license COPYING

%changelog
* Tue Sep 06 2011 The Coon of Ty <Ty@coon.org> - 2.8-1
- Initial version of the package

