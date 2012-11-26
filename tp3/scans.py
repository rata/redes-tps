#! /usr/bin/env python

import sys
import socket
from scapy.all import sr1, IP, TCP


def _syn_scan(host, port, timeout):

    pkt = IP(dst=host) / TCP(dport=port,flags="S")
    pkt = sr1(pkt, timeout=timeout)

    if pkt is None:
        return None

    return pkt.getlayer(TCP).flags


def syn_scan(host, port, timeout=10):

    # XXX: no se cierra la conexion ni acepta la conexion, solo se recibe el
    # "SYN/ACK" y no se hace mas nada
    flags = _syn_scan(dst, port, timeout)

    if flags is None:
        return "Got no answer, possibly closed/filtered"
    elif flags == 0x12:
        # 0x12 es un "SYN/ACK"
        return "abierto"
    elif flags == 0x14:
        # 0x14 es un "RST/ACK"
        return "cerrado"
    else:
        # No es nada de lo esperado, pero seguro como no es un "SYN/ACK" no es
        # que esta abierto, asique decimos que esta cerrado/filtrado
        return "cerrado/filtrado"


def connect_scan(host, port, timeout=10):

    try:
        s = socket.create_connection((host, port), timeout)
        s.close()
        return "abierto"
    except:
        # Could not open socket
        return "cerrado/filtrado"


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print "Usage", sys.argv[0], "<dst> <port>"
        sys.exit(1)

    dst = sys.argv[1]
    port = int(sys.argv[2])

    print "Starting SYN scan..."
    port_state = syn_scan(dst, port)
    print "SYN scan result:", port_state

    print "Starting connect scan"
    port_state = connect_scan(dst, port)
    print "Connect scan result:", port_state

