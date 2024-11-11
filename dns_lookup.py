import socket

def dns_lookup():
    """Perform DNS lookup for a given IP address or domain name."""
    choice = input("Do you want to look up a (1) domain name or (2) IP address? (Enter 1 or 2): ")

    if choice == '1':
        # Lookup IP address for a given domain name
        domain_name = input("Enter the domain name (e.g., example.com): ")
        try:
            ip_address = socket.gethostbyname(domain_name)
            print(f"The IP address for {domain_name} is: {ip_address}")
        except socket.gaierror:
            print("Error: Unable to resolve the domain name.")
    
    elif choice == '2':
        # Lookup domain name for a given IP address
        ip_address = input("Enter the IP address (e.g., 93.184.216.34): ")
        try:
            domain_name = socket.gethostbyaddr(ip_address)[0]
            print(f"The domain name for {ip_address} is: {domain_name}")
        except socket.herror:
            print("Error: Unable to resolve the IP address.")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    dns_lookup()