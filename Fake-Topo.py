"""Custom topology example
3 switche plus 2 host :

switch linear conneted first swich and last swich connet to 1 host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.

This topo used to test fake topology
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h2',ip='10.0.0.4' )
        rightHost = self.addHost( 'h3',ip='10.0.0.5' )
        switch1 = self.addSwitch( 's1', ip='10.0.0.1')
        switch2 = self.addSwitch( 's2', ip = '10.0.0.2')
        switch3 = self.addSwitch( 's3', ip = '10.0.0.3')



        # Add links
        self.addLink( leftHost,  switch1)
        self.addLink( switch1, switch2 )
        self.addLink( switch2, switch3 )
        self.addLink( switch3, rightHost)


topos = { 'mytopo': ( lambda: MyTopo() ) }
