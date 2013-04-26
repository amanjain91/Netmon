#!/usr/bin/python
from rrdtool import update as rrd_update
from os import listdir
from os.path import isfile, join
import os
from random import randint
import time
data_path = '/opt/openstack_extra.aman/netmon_data'
data_path_parsed = '/opt/openstack_extra.aman/netmon_data_parsed'
db_path = '/opt/openstack_extra.aman/rrdb'
data_files = [ f for f in listdir(data_path) if isfile(join(data_path, f)) and f.find('src') > -1 ]
data_files.sort()

n = 10000
t = time.time()
ip_addr = '10.248.127.233'
for i in range(0, n):
	#ip_addr = src_file.split('_')[0]
	#timestamp = src_file.split('_')[1]
	timestamp = t + i*120
	src_or_dst = 'src_dst'.split('_')[i%2]
#	f = open(join(data_path,src_file))
#	src_datas = f.readlines()
#	f.close()

#	dst_file = ip_addr+"_"+timestamp+"_"+"dst"
#	f = open(join(data_path,dst_file))
#	dst_datas = f.readlines()
#	f.close()

#	i = 0
#	for dst in dst_datas:
#		cur_ip = dst.split(' ')[0]
	cur_ip = '10.240.53.200'
		#dst_val = dst.split(' ')[1].rstrip('\n')
		#src_val = src_datas[i].split(' ')[1].rstrip('\n')
	dst_val = str(randint(0,1024))
	src_val = str(randint(0,2048))
	i+=1
	print ip_addr + ", " + cur_ip + ", " + src_val + ", " + dst_val
	db_name = ip_addr+"_"+cur_ip+".rdd"
	ret = rrd_update(join(db_path,db_name), '%s:%d:%d' % (timestamp, int(src_val), int(dst_val))) 
	#os.system("mv " + join(data_path, src_file) + " " + join(data_path_parsed, src_file))	
	#os.system("mv " + join(data_path, dst_file) + " " + join(data_path_parsed, dst_file))
