import socket
import os

#IP address of host to listen on
host = "172.16.242.196"

#create a socket connection and connect to interface

if os.name == "nt":
	socket_protocol = socket.IPPROTO_IP
else:
	socket_protocol = socket.IPPROTO_ICMP

packet_sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

packet_sniffer.bind((host,0))

#to include IP addresses in the capture
packet_sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

#if using Windows send IOCTL to set up promiscuous mode
if os.name == "nt":
	packet_sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

#read single packet
print packet_sniffer.recvfrom(65565)

#if using windows turn off promiscuous mode
if os.name == "nt":
	packet_sniffer.setsockopt(socket.SIO_RCVALL, socket.RCVALL_OFF)
