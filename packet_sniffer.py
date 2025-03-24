from scapy.all import sniff

def packet_callback(packet):
    # Check if packet has an IP layer
    if packet.haslayer("IP"):
        print(f"Packet: {packet.summary()}")
        print(f"Source IP: {packet['IP'].src} → Destination IP: {packet['IP'].dst}")
        print(f"Protocol: {packet['IP'].proto}\n")

# Sniff packets (first 10 packets, change count=0 for unlimited)
sniff(prn=packet_callback, count=10)
