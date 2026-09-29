# nfs-simple
Demonstration of a simple NFS server on Cloudlab

# on both servers

```
/local/repository/base.sh
eval "$(ssh-agent -s)"
sudo ssh-add /local/migration_experiment/id_ed25519
```

test connection

```
ssh root@server-[0/1]
```

modify boot command line

```
console=ttyS0,115200n8
```

perform migration

```
sudo virsh migrate --live domain1 qemu+ssh://"$1"/system
```

usage of virsh

```
sudo virsh start domain1
sudo virsh console domain1
sudo virsh destroy domain1
```
