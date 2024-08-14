# Content-Distribution-Network
A content distribution network using socket programming in Python.

### Aim of the project:

Design and Simulation of a Content Distribution Network (CDN) using Iterative queries in
DNS(Domain Name System).

### Implememtation:

A content distribution network was simulated using multiple systems and a Raspberry Pi 3B.
Python socket programming was used for UDP transmission. The systems were classified as
Requesting Host, Local DNS server, Root DNS server, TLD DNS server, and two
Authoritative DNS servers. The network was based on the Iterative queries in DNS.

The information transmitted using this method was a .mp4 file and was successfully retrieved
from the servers when requested by the host. The .mp4 file was sent through a UDP socket.

The communication between the servers was a binary encoded message following the DNS
message format that was encoded and decoded at each stage of the information
retrieval process.

The systems used for this implementation use socket programming as the mode of
communication and all systems were programmed according to their assigned role in the
network.


### Outcomes of the project:
The simulation of a Content Distribution Network was implemented and the requested .mp4
file was successfully retrieved from the respective server.

The network can be further improved by the addition of multiple authoritative DNS servers
for the classification of multiple content distributors in the network(CDN).

All the queries and responses were recorded via Wireshark capture and observed. All the
transmitted messages were verified if the content transmitted was coded and decoded
accurately at each stage of transmission.
