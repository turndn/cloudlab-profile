#! /bin/bash

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c4130

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c6320

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c6420
