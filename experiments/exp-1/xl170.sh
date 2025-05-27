#! /bin/bash

echo "Wait"
read a
/local/repository/migrate_libvirt.sh m510

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c220g1

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c220g2

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c220g5
