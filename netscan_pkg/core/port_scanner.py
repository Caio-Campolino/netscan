import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_port(ip, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            return sock.connect_ex((ip, port)) == 0
    except Exception:
        return False


def scan_ports(ip, ports, threads=50, timeout=1):
    open_ports = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {
            executor.submit(scan_port, ip, port, timeout): port
            for port in ports
        }

        for future in as_completed(futures):
            port = futures[future]
            if future.result():
                open_ports.append(port)

    return sorted(open_ports)
