#! /bin/bash

echo "Wait"
read a
/local/repository/migrate_libvirt.sh m510

echo "Wait"
read a
/local/repository/migrate_libvirt.sh xl170
