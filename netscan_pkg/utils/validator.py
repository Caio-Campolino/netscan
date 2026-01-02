import ipaddress

def validate_target(target):
    try:
        ipaddress.ip_network(target, strict=False)
        return True
    except ValueError:
        return False
