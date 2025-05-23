#! /bin/bash

sudo virsh start domain1
sudo virsh migrate --live domain1 qemu+ssh://"$1"/system | tee ~/results/migration_"$1".txt 2>&1 || sudo virsh destroy domain1
