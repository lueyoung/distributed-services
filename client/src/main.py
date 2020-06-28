#!/usr/bin/env python3

from client import newRPCProxy
import sys

def main():

    ipport = sys.argv[1].split(":")
    ip = ipport[0]
    port = int(ipport[1])
    
    proxy = newRPCProxy(ip=ip, port=port)

    # all functions registered with the RPCHandler class can then be called

    ret = proxy.ping()
    print(ret)

    a = proxy.add(2,5)
    print(a)

    res = proxy.ha()
    print(res)

if __name__ == "__main__":
    main()
