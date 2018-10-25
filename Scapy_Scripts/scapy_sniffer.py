from scapy.all import *

packet_sniffer = sniff(count = 10)
packet_sniffer.nsummary()
