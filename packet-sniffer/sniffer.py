import socket
import struct
import textwrap

#TODO: add IPv6
# DHCP???

# to get a certain amount of tabs, use lambda function
tab = lambda num: "\t"*num

HOST = socket.gethostbyname(socket.gethostname())
# loops while packets come in, and displays them
def main():
    connection = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    connection.bind((HOST,0))                                                               # create raw socket and bind it to the interface (might need to use ipconfig & hardcode the values: conn.bind(('IP',0)) )
    connection.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)                          # include IP headers
    connection.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    while True:
        raw_data, addr = connection.recvfrom(65536)
        dest_mac, source_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame:')
        print('destination: {}, source: {}, protocol: {}'.format(dest_mac, source_mac, eth_proto))

        # 8 for IPv4
        if eth_proto == 8:
            (version, header_length, ttl, proto, src, target, data) = ipv4_packet(data)
            print(tab(1) + ' - IPv4 packet:')
            print(tab(2) + ' - version: {}, header length: TTL: {}'.format(version, header_length, ttl))
            print(tab(2) + ' - protocol: {}, source: {}, target: {}'.format(proto, src, target))

            # ICMP
            if proto == 1:
                icmp_type, code, checksum, data = icmp_packet(data)
                print(tab(1) + ' - ICMP packet:')
                print(tab(2) + ' - type: {}, code: {}, checksum: {}, '.format(icmp_type, code, checksum))
                print(tab(2) + ' - data:' + format_multi_line((tab(3) + ' '), data))

            # TCP
            elif proto == 6:
                src_port, dest_port, sequence, ack, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data = tcp_segment(data)
                print(tab(1) + ' - TCP segment:')
                print(tab(2) + ' - source port: {}, destination: {}'.format(src_port, dest_port))
                print(tab(2) + ' - sequence: {}, acknowledgement: {}'.format(sequence, ack))
                print(tab(2) + ' - Flags:')
                print(tab(3) + ' - URG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN: {}'.format(flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin))
                print(tab(2) + ' - Data:' + format_multi_line((tab(3) + ' '), data))

            # UDP
            elif proto == 17:
                src_port, dest_port, length, data = udp_segment(data)
                print(tab(1) + ' - UDP segment:')
                print(tab(2) + ' - source port: {}, destination port: {}, length: {}'.format(src_port, dest_port, length))

            # other
            else:
                print(tab(1) + ' - data:' + format_multi_line((tab(2) + ' '), data))
            
        else:
            print('data:' + format_multi_line((tab(1) + ' '), data))

# unpack ethernet frame
def ethernet_frame(data):
    dest_mac, source_mac, proto = struct.unpack('! 6s 6s H', data[:14])                     # grabs & unpacks the first 14 bytes of packet data (receiver, sender, type)
    return get_mac_address(dest_mac), get_mac_address(source_mac), socket.htons(proto), data[14:] # return the data that comes after that (size of payload differs depending on activity)

# return formatted MAC address (AA:BB:CC:DD:EE:FF)
def get_mac_address(mac_addr_bytes):
    bytes_str = map('{:02x}'.format, mac_addr_bytes)                                        # we only need 2 demical places for each chunk
    return ':'.join(bytes_str).upper()                                                      # join each chuck with a colon to complete the address

# unpack the IP data
def ipv4_packet(data):
    version_header_length = data[0]                                                         # gets version & header length (8 bytes)
    version = version_header_length >> 4                                                    # bit shifts version_header_length to the right by 4, so that only the version is saved (0000 vvvv)
    header_length = (version_header_length & 15) * 4                                        # need header length to figure out where the data starts
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]

# returns formatted IPv4 address (127.0.0.0)
def ipv4(addr):
    return '.'.join(map(str, addr))

# unpack ICMP packet
def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

# unpack UDP segments
def udp_segment(data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])
    return src_port, dest_port, size, data[8:]

# unpack TCP segment
def tcp_segment(data):
    (src_port, dest_port, sequence, ack, offset_reserved_flags) = struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    return src_port, dest_port, sequence, ack, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[offset:]

# makes multi-line print-out more readable
def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])

main()