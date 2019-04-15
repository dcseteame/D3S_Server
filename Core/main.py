#!/usr/bin/python3

from poll import Poll

pollThread = Poll("http://localhost:35673/devices")
pollThread.start()
