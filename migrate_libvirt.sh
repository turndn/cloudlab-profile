#! /bin/bash

sudo virsh start domain1
sudo virsh migrate --live domain1 qemu+ssh://"$1"/system 2>&1 | tee ~/results/migration_"$1".txt || sudo virsh destroy domain1
