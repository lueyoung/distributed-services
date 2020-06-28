#!/usr/bin/env python3

from kazoo.client import KazooClient as zkclient
import sys

zk_hosts = ",".join(sys.argv[1:])
zk = zkclient(hosts=zk_hosts, read_only=True, timeout=10)
zk.start()

data, _ = zk.get("/rpc_service")

print("{}".format(data.decode("utf-8")))
