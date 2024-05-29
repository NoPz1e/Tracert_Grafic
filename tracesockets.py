import datetime
import socket
import sys, os


def traceroute(hostname_or_address, max_hops=30, timeout=2):
    dest_addr = socket.gethostbyname(hostname_or_address)
    proto_icmp = socket.getprotobyname("icmp")
    proto_udp = socket.getprotobyname("udp")
    port = 33434

    for ttl in range(1, max_hops + 1):
        rx = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto_icmp)
        rx.settimeout(timeout)
        rx.bind(("", port))
        tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto_udp)
        tx.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        start = datetime.datetime.now()
        tx.sendto("".encode(), (dest_addr, port))

        try:
            _, curr_addr = rx.recvfrom(512)
            curr_addr = curr_addr[0]
        except socket.error:
            curr_addr = "*"
        finally:
            end = datetime.datetime.now()
            rx.close()
            tx.close()

        yield curr_addr, (end - start).microseconds

        if curr_addr == dest_addr:
            break


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python traceroute.py <hostname_or_address>")
        sys.exit(1)

    dest_name = sys.argv[1]

    filename = f"{dest_name}.txt"
    if os.path.exists(filename):
        os.remove(filename)

    try:
        with open(filename, "x") as file:
            for i, v in enumerate(traceroute(dest_name)):
                reg = f"{(i+1)}\t{v[0]}\t{v[1]}\n"
                file.write(reg)
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(1)