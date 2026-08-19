import os
import re
import time

print("Script is running")

def detect_arp_poisoning():
	print("Scanning Network")
	with os.popen('arp -a') as f:
		arp_data = f.read()
	mac_add = re.findall(r'(([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2})', arp_data)
	clean_macs = [mac[0].lower() for mac in mac_add]

	duplicates = set([x for x in clean_macs if clean_macs.count(x) > 1])
	
	if duplicates:
		print("ALERT: Possible MitM Attack")
		print(f"Duplicated MAC Address: {list(duplicates)[0]}")
	else:
		print("No duplicated MACs found.")

if __name__ == "__main__":
	detect_arp_poisoning()
