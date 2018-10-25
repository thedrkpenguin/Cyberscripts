import sys
from scapy.all import *

#checking to ensure that the command has the appropriate parameters
#program will exit if the parameters are not correct

if len(sys.argv) != 2:
	print "Usage: python scapy_arping.py <network/subnet>\n"
	print "eg: python scapy_arping.py 10.1.1.0/24\n"
	sys.exit(1)

#set the verbosity level to 0 (low) or 3(high)
conf.verb = 0

#creating answered and unanswered ARP responses for the destination 
#designated when the command is launched (sys.argv[1])
ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst = sys.argv[1]), timeout = 2)

#this will iterate through the answered packets for all sent and received packets
#will print the MAC address to IP address mappings
#%MAC.src% = Source MAC Field
#%ARP.psrc% = source IP Field
for snd,rcv in ans:
	print rcv.sprintf("MAC:%Ether.src% IP:%ARP.psrc%")
