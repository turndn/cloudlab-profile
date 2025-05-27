#! /bin/bash

echo "Wait"
read a
/local/repository/migrate_libvirt.sh r320

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c6220

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c220g1
