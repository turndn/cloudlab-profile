#! /bin/bash

echo "Wait"
read a
/local/repository/migrate_libvirt.sh d710

echo "Wait"
read a
/local/repository/migrate_libvirt.sh r320
