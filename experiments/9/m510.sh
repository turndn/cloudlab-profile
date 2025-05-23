#! /bin/bash

/local/repository/base.sh

echo "Wait"
read hello
/local/repository/migrate_libvirt.sh c220g1

echo "Wait"
read hello
/local/repository/migrate_libvirt.sh c220g2
