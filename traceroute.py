#! /usr/bin/env python

import sys
from myping import traceroute


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Usage:", sys.argv[0], "<destination> [maxhops]"
        sys.exit(1)

    dst = sys.argv[1]

    maxhops = 30
    if len(sys.argv) >= 3:
        maxhops = int(sys.argv[2])

    hops = traceroute(dst, maxhops)

    for index, hop in enumerate(hops, 1):

        print "Hop", index, ":", hop
