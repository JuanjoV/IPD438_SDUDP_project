import threading
import socket
import sys
import queue
import dataclasses

class TCPEngine(object):
    def __init__(self):
        pass

    



@dataclasses.dataclass
class ConnectionData:
    clientIP    : str
    clientPort  : int
    serverIP    : str
    serverPort  : int
    sEngineIP   : str
    sEnginePort : int
    cEngineIP   : str
    cEnginePort : int

if __name__ == "__main__":
    from_udpQ = queue.Queue()
    to_udpQ = queue.Queue()
    
    tcpEng = TCPEngine()

