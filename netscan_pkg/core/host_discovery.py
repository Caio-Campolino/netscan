import subprocess
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed
from netscan_pkg.utils.logger import info, debug


def is_host_alive(ip, timeout):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", str(timeout), str(ip)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False


def discover_hosts(network, threads=50, timeout=1, skip_icmp=False):
    alive_hosts = []

    net = ipaddress.ip_network(network, strict=False)

    if skip_icmp:
        return [str(ip) for ip in net.hosts()]

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {
            executor.submit(is_host_alive, ip, timeout): ip
            for ip in net.hosts()
        }

        for future in as_completed(futures):
            ip = futures[future]
            if future.result():
                debug(f"Host alive: {ip}")
                alive_hosts.append(str(ip))

    return alive_hosts
