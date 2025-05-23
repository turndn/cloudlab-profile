#! /bin/bash

/local/repository/base.sh

echo "Wait"
read hello
/local/repository/migrate_libvirt.sh d430

echo "Wait"
read hello
/local/repository/migrate_libvirt.sh d820
