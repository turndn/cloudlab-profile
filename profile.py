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
    ('urn:publicid:IDN+emulab.net+image+DLOCK:migration-kvm.experiment', 'UBUNTU 24.04 (kvm-qemu-libvirt)'),
]

pc.defineParameter("osImage", "Select OS image for clients",
                   portal.ParameterType.IMAGE,
                   imageList[0], imageList)

# Always need this when using parameters
params = pc.bindParameters()

ifaces = []

class Client:
    def __init__(self, **kwargs):
        self.node = kwargs.get("node", "")
        self.hardware_type = kwargs.get("hardware_type", "")
        self.iface_name = kwargs.get("iface_name", "")
        self.ipaddr = kwargs.get("ipaddr", "")

clients = []

nodes = [
    "d710",
    "d820",
]

for i, node in enumerate(nodes):
    c = Client(node=node,
               hardware_type=node,
               iface_name="eth1",
               ipaddr="192.168.6.{}".format(i + 3))
    clients.append(c)

for client_config in clients:
    client = request.RawPC(client_config.node)
    client.disk_image = params.osImage
    client.hardware_type = client_config.hardware_type
    client.routable_control_ip = True
    ifaces.append(client.addInterface(client_config.iface_name,
                                      pg.IPv4Address(client_config.ipaddr, '255.255.255.0')))

lan = request.LAN("lan")
lan.bandwidth = 100000

# Attach server to lan.
for iface in ifaces:
    lan.addInterface(iface)

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
