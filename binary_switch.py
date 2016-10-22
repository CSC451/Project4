# File based on OpenFlow tutorial written by James McCauley
# Written by Hugo Lucas
# CSC 451: Introduction to Networks
# Fall 2016

# Do not edit

from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.openflow.discovery 
import math

# These are particularly important for this portion of the assignment !
from pox.lib.packet.ipv4 import ipv4
from pox.lib.packet.arp import arp
from pox.lib.addresses import IPAddr, EthAddr

log = core.getLogger()

class Binary_Switch (object):

  def __init__ (self, connection):
    # Done on start-up
    self.connection = connection
    connection.addListeners(self)

  def resend_packet (self, packet_in, out_port):
    msg = of.ofp_packet_out()
    msg.data = packet_in
    
    # Add an action to send to the specified port
    action = of.ofp_action_output(port = out_port)
    msg.actions.append(action)

    # Send message to switch
    self.connection.send(msg)

  def binary_switch(self, packet, packet_in):
    # Fill in method with your own code, feel free to create other methods however

    # Determine which type of packet you're dealing with [Hint: look at the import statements]

    # Once you know which packet you have, extract the information needed to forward packet [Hint: look at the POX wiki]

    # Create an algorithm that determines which port to forward the packet from

    # Forward the packet into the port given by your algorithm

  def _handle_PacketIn (self, event):
    # OpenFlow method that is called automatically by a switch when it encounters a packet it does not
    # know where to forward

    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.

    self.binary_switch(packet, packet_in)


def launch ():
  # Starts the component, there is no reason to edit this portion

  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Binary_Switch(event.connection)
  pox.openflow.discovery.launch()
  core.openflow.addListenerByName("ConnectionUp", start_switch)
