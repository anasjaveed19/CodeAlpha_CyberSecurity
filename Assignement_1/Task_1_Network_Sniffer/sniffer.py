from scapy.all import sniff, IP

def process_packet(packet):
    # Check if the packet has an IP layer [cite: 26]
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"Source: {src_ip} | Destination: {dst_ip} | Protocol: {protocol}")

print("Starting Sniffer... (Press Ctrl+C to stop)")
# This captures traffic and uses the function above to show it [cite: 23]
sniff(prn=process_packet, store=False)