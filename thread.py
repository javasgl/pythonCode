#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

from datetime import *
import time


def hello(index, *args):
    time.sleep(2)
    print str(index) + "::::" + str(datetime.now()) + "\n"
    return


tasks = list()

index = 0

while index < 10:
    index += 1
    tasks.append(threading.Thread(name="thread-name", target=hello, args=(index, 'world', 'songgl')))

for thread in tasks:
    thread.setDaemon(True)
    thread.start()

for thread in tasks:
    thread.join()
