#!/bin/sh

NAME=$(rpm -q --specfile *.spec --qf "%{name}\n" | head -n1)
VERSION=$(rpm -q --specfile *.spec --qf "%{version}\n" | head -n1)

rm -rf $NAME-$VERSION
git clone -b v0.2 https://github.com/3Hren/$NAME.git $NAME-$VERSION --depth 1

tar -ca --exclude-vcs --exclude-vcs-ignores -f $NAME-$VERSION.tar.xz $NAME-$VERSION
rm -rf $NAME-$VERSION
