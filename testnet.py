
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import Ryu, OVSSwitch

RYU_CTRL_NAME = '~/l2.py'


class testTopo(Topo):
    
    def build(self, n=1):
        nodes = []
        leftHost = self.addHost('h1')
        rightHost = self.addHost('h2')
        nodes.append(leftHost)

        for sw in range(n):
            switch = self.addSwitch('s%s' % (sw + 1), cls=OVSSwitch, protocols='OpenFlow13' )
            nodes.append(switch)
            self.addLink(nodes[sw], switch)
        
        self.addLink(nodes[n], rightHost)

def simpleTest():

    topo = testTopo(n=9)
    #ryuCtrl = Ryu('c0', ryuArgs=RYU_CTRL_NAME, command='ryu run')
    ryuCtrl = RemoteController('c0', ip='127.0.0.1', port=6653)
    net = Mininet(topo, controller=ryuCtrl)
    #net.addController(ryuCtrl)
    net.start()
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    net.pingAll()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    simpleTest()
