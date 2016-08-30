pi@raspberrypi:~/templeton_receiver $ sudo python3 . hci0 bare
2016-08-30 18:20:18,191 |INFO| Using hci0 to connect to DC:21:3A:4D:3A:86... <__main__.py:19>
Timed out connecting to DC:21:3A:4D:3A:86 after 10.0 seconds.
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/pexpect/expect.py", line 99, in expect_loop
    incoming = spawn.read_nonblocking(spawn.maxread, timeout)
  File "/usr/local/lib/python3.4/dist-packages/pexpect/pty_spawn.py", line 462, in read_nonblocking
    raise TIMEOUT('Timeout exceeded.')
pexpect.exceptions.TIMEOUT: Timeout exceeded.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/pi/pymetawear/pymetawear/backends/pygatt/gatttool.py", line 82, in connect
    timeout)
  File "/usr/local/lib/python3.4/dist-packages/pexpect/spawnbase.py", line 321, in expect
    timeout, searchwindowsize, async)
  File "/usr/local/lib/python3.4/dist-packages/pexpect/spawnbase.py", line 345, in expect_list
    return exp.expect_loop(timeout)
  File "/usr/local/lib/python3.4/dist-packages/pexpect/expect.py", line 107, in expect_loop
    return self.timeout(e)
  File "/usr/local/lib/python3.4/dist-packages/pexpect/expect.py", line 70, in timeout
    raise TIMEOUT(msg)
pexpect.exceptions.TIMEOUT: Timeout exceeded.
<pexpect.pty_spawn.spawn object at 0x7578b6b0>
command: /usr/bin/gatttool
args: ['/usr/bin/gatttool', '-i', 'hci0', '-I']
buffer (last 100 chars): b':86][LE]> \r\x1b[K\x1b[0;91mError: \x1b[0mconnect error: Connection timed out (110)\r\n[DC:21:3A:4D:3A:86][LE]> '
before (last 100 chars): b':86][LE]> \r\x1b[K\x1b[0;91mError: \x1b[0mconnect error: Connection timed out (110)\r\n[DC:21:3A:4D:3A:86][LE]> '
after: <class 'pexpect.exceptions.TIMEOUT'>
match: None
match_index: None
exitstatus: None
flag_eof: False
pid: 1535
child_fd: 8
closed: False
timeout: 30
delimiter: <class 'pexpect.exceptions.EOF'>
logfile: None
logfile_read: None
logfile_send: None
maxread: 2000
ignorecase: False
searchwindowsize: None
delaybeforesend: 0.05
delayafterclose: 0.1
delayafterterminate: 0.1
searcher: searcher_re:
    0: re.compile("b'Connection successful.*\\[LE\\]>'")
    1: re.compile("b'\\[CON\\]\\[DC:21:3A:4D:3A:86\\]\\[LE\\]'")

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "./__main__.py", line 23, in <module>
    c = MetaWearClient(address, 'pygatt', debug=False, adapter=adapter)        
  File "/home/pi/pymetawear/pymetawear/client.py", line 117, in __init__
    self._address, timeout=timeout, debug=debug, adapter=adapter)   ## bh
  File "/home/pi/pymetawear/pymetawear/backends/pygatt/__init__.py", line 40, in __init__
    debug)
  File "/home/pi/pymetawear/pymetawear/backends/__init__.py", line 57, in __init__
    METAWEAR_SERVICE_NOTIFY_CHAR[1])
  File "/home/pi/pymetawear/pymetawear/backends/pygatt/__init__.py", line 113, in get_handle
    return self.requester.get_handle(uuid) + int(notify_handle)
  File "/home/pi/pymetawear/pymetawear/backends/pygatt/__init__.py", line 58, in requester
    self._address, timeout=self._timeout, address_type='random')
  File "/home/pi/pymetawear/pymetawear/backends/pygatt/gatttool.py", line 87, in connect
    raise NotConnectedError(message)
pygatt.exceptions.NotConnectedError
During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3.4/runpy.py", line 170, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/lib/python3.4/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "./__main__.py", line 33, in <module>
    log.error(log.exc(e))
  File "./housepy/log.py", line 47, in exc
    return "%s <%s:%s> %s" % (sys.exc_info()[0].__name__, os.path.split(sys.exc_info()[2].tb_frame.f_code.co_filename)[1], sys.exc_info()[2].tb_lineno, e)
  File "/usr/local/lib/python3.4/dist-packages/pygatt/exceptions.py", line 12, in __str__
    return repr(self)
  File "/usr/local/lib/python3.4/dist-packages/pygatt/exceptions.py", line 9, in __repr__
    return "<%s %s>" % (self.__class__.__name__, self.message)
AttributeError: 'NotConnectedError' object has no attribute 'message'
pi@raspberrypi:~/templeton_receiver $ 
