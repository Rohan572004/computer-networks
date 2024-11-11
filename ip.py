import ipaddress

def get_ip_info(ip_str, subnet_mask_str):
    # Convert the IP address and subnet mask to an IPv4Network object
    network = ipaddress.IPv4Network(f"{ip_str}/{subnet_mask_str}", strict=False)

    # Get the class of the IP address
    ip_class = get_ip_class(ip_str)

    # Calculate the network address
    network_address = network.network_address

    # Calculate the broadcast address
    broadcast_address = network.broadcast_address

    # Calculate the first usable address
    first_usable = network.network_address + 1

    # Calculate the last usable address
    last_usable = network.broadcast_address - 1

    return {
        "IP Address": ip_str,
        "Subnet Mask": subnet_mask_str,
        "Class": ip_class,
        "Network Address": str(network_address),
        "Broadcast Address": str(broadcast_address),
        "First Usable Address": str(first_usable),
        "Last Usable Address": str(last_usable)
    }

def get_ip_class(ip_str):
    # Convert the IP address to an integer
    ip_parts = list(map(int, ip_str.split('.')))
    first_octet = ip_parts[0]

    # Determine the class based on the first octet
    if first_octet >= 1 and first_octet <= 126:
        return "Class A"
    elif first_octet >= 128 and first_octet <= 191:
        return "Class B"
    elif first_octet >= 192 and first_octet <= 223:
        return "Class C"
    elif first_octet >= 224 and first_octet <= 239:
        return "Class D (Multicast)"
    elif first_octet >= 240 and first_octet <= 255:
        return "Class E (Experimental)"
    else:
        return "Invalid IP Address"

# Example usage
if __name__ == "__main__":
    ip_address = input("Enter the IP address: ")
    subnet_mask = input("Enter the subnet mask: ")

    ip_info = get_ip_info(ip_address, subnet_mask)

    print("\nIP Address Information:")
    for key, value in ip_info.items():
        print(f"{key}: {value}")

        #ex usage : IP address: 192.168.1.10  ,  subnet mask: 255.255.255.0