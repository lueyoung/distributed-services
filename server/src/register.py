#!/usr/bin/env python3

from kazoo.client import KazooClient as zkclient
import sys
from socket import *

ip = gethostbyname(gethostname())
#port = int(sys.argv[1])
port = sys.argv[1]
zk_hosts = ",".join(sys.argv[2:])
print(zk_hosts)
zk = zkclient(hosts=zk_hosts)
zk.start()

zk.ensure_path("/rpc_service")

zk.set("/rpc_service", bytes("{}:{}".format(ip, port),encoding = "utf-8"))

zk.stop()
zk.close()
