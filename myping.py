#! /usr/bin/env python

import sys
import time
from scapy.all import sr1,IP,ICMP, RandShort


def ping(dst, payload, seq=1, ttl=64, timeout=5):
    """Makes 1 ICMP echo request to dst.
    @returns: the response in an object that accepts method show(), None on
    timeout
    """

    pkt = IP(dst=dst, ttl=ttl) / ICMP(seq=seq, id=RandShort()) / payload
    pkt = sr1(pkt, timeout=timeout)

    return pkt


def estimate_rtt(dst, pkts = 10):
    """Estimates RTT sending pkts pings to dst.
    @returns rtt (ms)
    """

    t1 = time.time()

    for i in range(0, pkts):

        # Use the loop iteration as payload, just to put something
        ping(dst, payload=str(i), seq=i)

    t2 = time.time()

    # RTT is the time elapsed in average
    rtt = (t2 - t1) / float(pkts) * 1000

    return rtt


def traceroute(dst, maxhops=30):

    hops=[]
    last_hop = None

    # We don't want to use 0 as TTL, so we start at 1 and go to maxhops
    # inclusive
    for ttl in range(1, maxhops + 1):

        pkt = ping(dst, payload='test', ttl=ttl)

        # check if a response arrive. If not, use "*" as hop
        hop = "*"
        if pkt:
            hop = pkt.src

        # If we know which hop is this, and is the same as the last one, there
        # is no point to keep sending ICMPs with more TTL. No other hop will be
        # added
        # We check against last_hop IP and not if "hop == dst", because dst
        # could be a FQDN
        if hop != "*" and hop == last_hop:
            break

        hops.append(hop)
        last_hop = hop
        #time.sleep(1)

    return hops
