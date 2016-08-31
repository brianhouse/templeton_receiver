#!/usr/bin/env python3

import threading, queue, time, socket
from housepy import log, config

class MonitorSender(threading.Thread):

    def __init__(self, adapter, device_key):
        super(MonitorSender, self).__init__()
        self.daemon = True
        self.queue = queue.Queue()
        self.adapter = adapter
        self.device_key = device_key
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.sendto("/init,%s,%s" & (self.adapter, self.device_key), config['monitor'], 23232)
        self.start()

    def run(self):        
        while True:
            data = self.queue.get()
            if len(data) == 1:
                self.socket.sendto("/hz,%s,%s,%s" % (self.adapter, self.device_key, data), config['monitor'], 23232)
            elif config['monitor'] is not None:
                self.socket.send("/a,%s,%s,%s,%f,%f,%f", [self.adapter, self.device_key, data[0], data[1][0], data[1][1], data[1][2]])


class MonitorReceiver(threading.Thread):

    def __init__(self):
        super(MonitorReceiver, self).__init__()
        self.daemon = True
        self.queue = queue.Queue()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        self.socket.bind(('', 23232))      
        self.start()

    def run(self):
        while True:
            try:
                message, address = self.socket.recvfrom(1024)
                data = message.decode('utf-8').split(',')
                if data[0] == "/a":
                    self.queue.put(data[1:])    
                else:
                    log.info(data)
            except Exception as e:
                log.error(log.exc(e))


if __name__ == "__main__":
    monitor = MonitorReceiver()
    while True:
        time.sleep(0.1)
