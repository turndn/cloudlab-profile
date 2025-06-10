#! /bin/bash

echo "Wait"
read a
/local/repository/migrate_libvirt.sh d710

echo "Wait"
read a
/local/repository/migrate_libvirt.sh c6525-100g

echo "Wait"
read a
/local/repository/migrate_libvirt.sh d6515
