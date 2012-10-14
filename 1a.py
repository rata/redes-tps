#! /usr/bin/env python

import sys
from myping import ping


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Usage:", sys.argv[0], "<destination>"
        sys.exit(1)

    dst = sys.argv[1]

    p = ping(dst, "test")

    if p:
        p.show()
    else:
        print "Ping timeout or some other error!"

