#! /bin/bash

mkdir -p ~/work
mkdir -p ~/results

lscpu --json > ~/results/host_cpuid.txt

gcc /local/migration_experiment/kvm_get_supported_cpuid.c -o ~/work/kvm_get_supported_cpuid
sudo ~/work/kvm_get_supported_cpuid > ~/results/kvm_vcpuid.txt 2>&1

python3 /local/migration_experiment/qemu_get_static_model.py > ~/results/qemu_vcpuid.txt 2>&1

sudo virsh domcapabilities > ~/results/libvirt_vcpuid.txt 2>&1

