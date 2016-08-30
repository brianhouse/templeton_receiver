#!/usr/bin/env python3

import threading, queue, time
from housepy import log, osc, config

osc.verbose = False

class MonitorSender(threading.Thread):

    def __init__(self):
        super(MonitorSender, self).__init__()
        self.daemon = True
        self.queue = queue.Queue()
        self.socket = osc.Sender(config['monitor'], 23232)
        self.socket.send("/init", "hello world")
        self.start()

    def run(self):        
        while True:
            data = self.queue.get()
            if config['monitor'] is not None:
                self.socket.send("/a", "%s, %s, %s, %s" % (data[0], data[1][0], data[1][1], data[1][2]))


class MonitorReceiver(threading.Thread):

    def __init__(self):
        super(MonitorReceiver, self).__init__()
        self.daemon = True
        self.queue = queue.Queue()
        self.start()

    def run(self):
        def on_message(location, address, data):
            print(location)
            print(address)
            print(data)
            self.queue.put(data)
        self.socket = osc.Receiver(23232, on_message, blocking=True)


if __name__ == "__main__":
    monitor = MonitorReceiver()
    while True:
        time.sleep(0.1)
else:
    monitor = MonitorSender()
