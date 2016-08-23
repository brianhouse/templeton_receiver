#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, division, print_function, unicode_literals, absolute_import, sys
from pymetawear.client import MetaWearClient
from housepy import config, log

try:
    adapter_index = int(sys.argv[0])
    device_index = int(sys.argv[1])
    adapter = config['adapters'][adapter_index]
    address = config['devices'][device_index]
except Exception:
    print("[ADAPTER#] [DEVICE#] --via config.yaml")
    exit()

log.info("Using %s to connect to %s..." % (adapter, address))

while True:
    try:
        c = MetaWearClient(, 'pygatt', debug=False, adapter=adapter)        
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

def on_data(data):
    log.info("Epoch time: [{0}] - X: {1}, Y: {2}, Z: {3}".format(data[0], *data[1]))
c.accelerometer.notifications(on_data)

try:
    time.sleep(20.0)
except KeyboardInterrupt:
    log.info("Shutting down...")
    c.accelerometer.notifications(None)
    time.sleep(5.0)
    c.disconnect()
    log.info("--> bye")

