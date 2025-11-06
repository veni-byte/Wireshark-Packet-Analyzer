import nest_asyncio
import pyshark
import matplotlib.pyplot as plt

# Load pcap file
nest_asyncio.apply()
cap = pyshark.FileCapture(r"C:\Users\Admin\Documents\capture2.pcapng")
                          
                         

packet_sizes = []
packet_numbers = []

for i, packet in enumerate(cap):
    try:
        size = int(packet.length)  # packet length in bytes
        packet_sizes.append(size)
        packet_numbers.append(i + 1)
    except AttributeError:
        pass  # skip packets without length info

# Plot
plt.figure(figsize=(10,5))
plt.plot(packet_numbers, packet_sizes, marker='o', linestyle='-', markersize=3)
plt.title('Packet Size vs Packet Number')
plt.xlabel('Packet Number')
plt.ylabel('Packet Size (Bytes)')
plt.grid(True)
plt.show()