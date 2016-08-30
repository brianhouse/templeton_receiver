#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, sys
from pymetawear.client import MetaWearClient
from housepy import config, log
from rater import rater
from monitor import monitor

try:
    adapter = sys.argv[1]
    device_key = sys.argv[2]
    address = config['devices'][device_key]
except Exception as e:
    print(e)
    print("[ADAPTER#] [DEVICE#] --via config.yaml")
    exit()

log.info("Using %s to connect to %s..." % (adapter, address))

while True:
    try:
        c = MetaWearClient(address, 'pygatt', debug=False, adapter=adapter)        
        log.info("--> MetaWear initialized: {0}".format(c))
        log.info(c.accelerometer)
        ## setup
        # c.accelerometer.set_settings(data_rate=100.0, data_range=2.0)        
        # c.soft_reset()
        # c.disconnect()
        # time.sleep(4)
        # exit()        
    except Exception as e:
        log.error(log.exc(e))
        log.warning("Retrying...")
    else:
        break

log.info("Blinking 10 times...")
pattern = c.led.load_preset_pattern('blink', repeat_count=10)
c.led.write_pattern(pattern, 'g')
c.led.play()
time.sleep(5)
log.info("--> ready")
rater.start()
monitor.start()

def on_data(data):
    if config['debug']:
        log.debug("Epoch time: [{0}] - X: {1}, Y: {2}, Z: {3}".format(data[0], *data[1]))
    rater.queue.put(1)
    monitor.queue.put(data)
c.accelerometer.notifications(on_data)


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:    
    c.accelerometer.notifications(None)
    time.sleep(5.0)
    log.info("Shutting down...")
    c.disconnect()
    log.info("--> bye")

