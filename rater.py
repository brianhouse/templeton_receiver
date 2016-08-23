import threading, queue, time
from housepy import log

class Rater(threading.Thread):

    def __init__(self):
        super(Rater, self).__init__()
        self.daemon = True
        self.queue = queue.Queue()

    def run(self):        
        start_t = time.time()
        while True:
            t = time.time()
            if t - start_t >= 1:
                events = []
                while not self.queue.empty():
                    events.append(self.queue.get_nowait())                    
                log.info("Running at %shz" % sum(events))
                start_t = t

rater = Rater()