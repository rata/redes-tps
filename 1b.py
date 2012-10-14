#! /usr/bin/env python

import sys
from myping import estimate_rtt


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Usage:", sys.argv[0], "<destination> [count]"
        sys.exit(1)

    dst = sys.argv[1]

    count = 10
    if len(sys.argv) >= 3:
        count = int(sys.argv[2])

    rtt = estimate_rtt(dst, count)

    print "El rtt es:", rtt
