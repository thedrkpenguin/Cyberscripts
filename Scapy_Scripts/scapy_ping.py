#! /usr/bin/python

import sys
from scapy.all import *

if len(sys.argv) != 2:
	print "Usage: python scapy_ping.py <ip_address>\n"
	print "eg: python scapy_ping.py 127.0.0.1\n"
	sys.exit(1)

icmp_packet = sr1(IP(dst=sys.argv[1]) / ICMP())

if icmp_packet:
	icmp_packet.show()
