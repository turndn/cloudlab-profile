#! /bin/bash

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c6525-100g

echo "Wait"
read a
/local/repository/migrate_libvirt.sh d6515

echo "Wait"
read a
/local/repository/migrate_libvirt.sh m510

echo "Wait"
read a
/local/repository/migrate_libvirt.sh xl170
