Name:          ambience-outrun
Version:       1.0
Release:       3
Summary:       A magical sound ambience
Group:         System/Tools
Vendor:        247
Distribution:  SailfishOS
Packager:      247 <>
URL:           www.jollacommunity.it

License:       GPL

%description
An ambience for all the OutRun fans.

%files

%defattr(-,root,root,-)
/usr/share/ambience/*

%post
chmod 755 /usr/share/ambience/{name}
chmod 755 /usr/share/ambience/{name}/images
chmod 644 /usr/share/ambience/{name}/*.*
chmod 644 /usr/share/ambience/{name}/images/*.*
systemctl-user restart ambienced.service

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/ambience/{name}
systemctl-user restart ambienced.service
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "It's just upgrade"
systemctl-user restart ambienced.service
fi
fi

%changelog
* Thu Oct 18 2018 1.0
* Alarm changed to a more louder sound
