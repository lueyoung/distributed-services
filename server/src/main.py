#!/usr/bin/env python3

from server import newRPCServer
from stub import *
import sys

def main():
    
    # server is instantiated
    port = int(sys.argv[1])
    serv = newRPCServer(port=port)
    
    # functions are then registerd with the RPCHandler class. Note this is delegated
    serv.register_function(HelloWorld)
    serv.register_function(add)
    serv.register_function(test)
    serv.register_function(ping)
    
    # server is then set to listen
    serv.run()

if __name__ == "__main__":
    main()
