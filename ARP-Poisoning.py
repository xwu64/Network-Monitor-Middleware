"""Custom topology example
One switche plus 3 host :


Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.

This topo used to test ARP poisoning
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        maliciousHost = self.addHost( 'h1',ip='10.0.0.2' )
        leftHost = self.addHost( 'h2',ip='10.0.0.3' )
        rightHost = self.addHost( 'h3',ip='10.0.0.4' )
        switch = self.addSwitch( 's1')



        # Add links
        self.addLink( leftHost,  switch)
        self.addLink( rightHost,  switch)
        self.addLink( maliciousHost,  switch)


topos = { 'mytopo': ( lambda: MyTopo() ) }
