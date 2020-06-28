#!/bin/bash

RPC_SRV=$(/workspace/discovery.py $ZK_SERVERS)
/workspace/main.py $RPC_SRV
