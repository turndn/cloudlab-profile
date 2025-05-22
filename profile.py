"""This profile sets up a simple environment for migration experiment with KVM.
Two servers can share a VM image through NFS. To do so, one server acts as NFS
server and the other one acts as NFS client. The NFS server uses *temporary*
storage on one of your nodes, the contents will be lost when you terminate your
experiment. We have a different profile available if you need your NFS server
data to persist after your experiment is terminated. 

Instructions:
Click on any node in the topology and choose the `shell` menu item. Your shared
NFS directory is mounted at `/nfs` on all nodes."""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Image list
imageList = [
    ('urn:publicid:IDN+emulab.net+image+DLOCK:migration-kvm', 'UBUNTU 24.04 (kvm-qemu-libvirt)'),
]

# Do not change these unless you change the setup scripts too.
nfsServerName = "nfs"
nfsLanName    = "nfsLan"
nfsDirectory  = "/nfs"

pc.defineParameter("firstServerType", "First server type",
                   portal.ParameterType.STRING, 'd710')

pc.defineParameter("secondServerType", "Second server type",
                   portal.ParameterType.STRING, 'd710')

pc.defineParameter("osImage", "Select OS image for clients",
                   portal.ParameterType.IMAGE,
                   imageList[0], imageList)

pc.defineParameter("nfsSize", "Size of NFS Storage",
                   portal.ParameterType.STRING, "10GB",
                   longDescription="Size of disk partition to allocate on NFS server")

# Always need this when using parameters
params = pc.bindParameters()

# The NFS network. All these options are required.
nfsLan = request.LAN(nfsLanName)
nfsLan.bandwidth = 100000
nfsLan.best_effort       = True
nfsLan.vlan_tagging      = True
nfsLan.link_multiplexing = True

# The NFS server. (first server)
nfsServer = request.RawPC(nfsServerName)
nfsServer.disk_image = params.osImage
nfsServer.hardware_type = params.firstServerType
nfsServer.routable_control_ip = True
iface0 = nfsServer.addInterface('interface-0', pg.IPv4Address('192.168.6.2', '255.255.255.0'))
# Storage file system goes into a local (ephemeral) blockstore.
nfsBS = nfsServer.Blockstore("nfsBS", nfsDirectory)
nfsBS.size = params.nfsSize
# Initialization script for the server
nfsServer.addService(pg.Execute(shell="sh", command="sudo /bin/bash /local/repository/nfs-server.sh"))

# The NFS client. (second server)
nfsClient = request.RawPC("client")
nfsClient.disk_image = params.osImage
nfsClient.hardware_type = params.secondServerType
nfsClient.routable_control_ip = True
iface1 = nfsClient.addInterface('interface-1', pg.IPv4Address('192.168.6.3', '255.255.255.0'))
nfsClient.addService(pg.Execute(shell="sh", command="sudo /bin/bash /local/repository/nfs-client.sh"))

# Attach server to lan.
nfsLan.addInterface(iface0)
nfsLan.addInterface(iface1)

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
