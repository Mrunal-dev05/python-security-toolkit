import ipaddress
import re


MAC_RE = re.compile(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}")


def test_valid_mac():
    assert MAC_RE.fullmatch("AA:BB:CC:DD:EE:FF")


def test_invalid_mac():
    assert not MAC_RE.fullmatch("AA:BB:CC:DD:EE")


def test_valid_network():
    assert str(ipaddress.ip_network("192.168.1.0/24")) == "192.168.1.0/24"


def test_invalid_network():
    try:
        ipaddress.ip_network("not-a-network")
    except ValueError:
        assert True
    else:
        assert False


def test_valid_ports():
    ports = [22, 80, 443]
    assert all(1 <= port <= 65535 for port in ports)
