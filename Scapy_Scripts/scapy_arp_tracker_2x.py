from scapy.all import *

#creating a function that accepts a packet from the sniff command
#this will examine the packet for ARP and return the Source MAC address
#as well as the Source IP address

def arp_monitor(pkt):
	if ARP in pkt and pkt[ARP].op in (1,2):
		return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

#This allows us to sniff packets formt he network and return them in
#a packet list.  prn = ? is used to apply a function to the 
#packets as they are returned from the network (arp_monitor)
#store = 0 means we will not store any packets in memory
#filter is looking for key words in the packets (arp in this case)

sniff(prn=arp_monitor, filter = "arp", store = 0)
