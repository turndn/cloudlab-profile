#! /bin/bash

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c6320

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c6420

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c8220
