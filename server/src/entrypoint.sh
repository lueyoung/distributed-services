#!/bin/bash

/workspace/register.py $PORT $ZK_SERVERS
/workspace/main.py $PORT
