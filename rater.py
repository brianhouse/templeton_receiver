import threading, queue, time
from housepy import log

class Rater(threading.Thread):

    def __init__(self, monitor):
        super(Rater, self).__init__()
        self.daemon = True
        self.queue = queue.Queue()
        self.monitor = monitor

    def run(self):        
        start_t = time.time()
        while True:
            t = time.time()
            if t - start_t >= 1:
                events = []
                while not self.queue.empty():
                    events.append(self.queue.get_nowait())                    
                hz = sum(events)
                log.info("Running at %shz" % hz)
                self.monitor.queue.put(hz)
                start_t = t
            time.sleep(0.1)

