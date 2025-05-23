#! /bin/bash

echo "start domain1"
sudo virsh start domain1

echo "Collect vcpuid"
/local/repository/collect_vcpuid.sh

echo "shutdown domain1"
sudo virsh shutdown domain1
