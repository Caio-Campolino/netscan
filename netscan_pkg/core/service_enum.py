import socket
from netscan_pkg.utils.logger import info

def grab_banner(ip, port, timeout=2, limit=200):
    try:
        with socket.socket() as sock:
            sock.settimeout(timeout)
            sock.connect((ip, port))

            if port in (80, 443):
                sock.sendall(
                    b"HEAD / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n"
                )

            banner = sock.recv(1024).decode(errors="ignore")
            return banner.strip()[:limit] if banner else None
    except Exception:
        return None
