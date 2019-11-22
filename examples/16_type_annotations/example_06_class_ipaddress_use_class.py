from __future__ import annotations
import ipaddress


class IPAddress:
    def __init__(self, ip: str) -> None:
        self.ip = ip

    def __add__(self, other: int) -> IPAddress:
        ip_int = int(ipaddress.ip_address(self.ip))
        sum_ip_str = str(ipaddress.ip_address(ip_int + other))
        return IPAddress(sum_ip_str)

