#!/usr/bin/python

import rrdtool

freq = 120

f = open('list_of_nodes')
lines = f.readlines()
f.close()

for l in lines:
	ip_addr = l.split(' ')[1].rstrip('\n')
	for m in lines:
		ip_addr_2 = m.split(' ')[1].rstrip('\n')	
		ret = rrdtool.create(ip_addr+"_"+ip_addr_2+".rdd", "--step", "120", "--start", 'N', 
			"DS:src:GAUGE:240:U:U",
			"DS:dst:GAUGE:240:U:U",
			"RRA:AVERAGE:0.5:1:72000",
			"RRA:AVERAGE:0.5:5:72000")
