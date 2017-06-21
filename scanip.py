#!/usr/bin/python
import commands
import os
print "The computers predent in the network are"
print commands.getoutput("arp | grep 192.168 | cut -c1-15")

