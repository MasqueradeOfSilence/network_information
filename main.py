import netifaces
import dns.resolver
from requests import get

print("Hello network information!")
interface_list = netifaces.interfaces()
print("Interface list: " + str(interface_list) + "\n")

# Display IP addresses and subnets for each interface
print("IP addresses and subnets: ")

for i in range(0, len(interface_list)):
    current_interface = netifaces.ifaddresses(interface_list[i])
    if 2 in current_interface.keys():
        print("IP Address:" + current_interface[2][0]["addr"])
        print("Subnet: " + current_interface[2][0]["netmask"] + "\n")

# Display gateways
print("Gateways: ")
print(netifaces.gateways())

# DNS Servers:
dns_resolver = dns.resolver.Resolver()
print("DNS Servers: " + str(dns_resolver.nameservers))

# Public IP for NATed host:
ip = get("https://api.ipify.org").text
print("Here is my public IP: {}".format(ip))
