from rrdtool import fetch as rrd_fetch
import time

class FlowInstance ():
	def __init__(self):
		self.machine_a = ""
		self.machine_b = ""
		self.current_load_src = 0
		self.current_load_dst = 0
		self.current_time = 0

ip_file = '/opt/openstack_extra.aman/horizon/dashboards/nova/netmon/list_of_machines'
f = open(ip_file)
list_of_ips = f.readlines()
f.close()
i=0
for ip in list_of_ips:
	list_of_ips[i].rstrip('\n')
	i+=1

def get_instance_data(request):
	list_to_ret = []
#	for ip_a in list_of_ips:
#		for ip_b in list_of_ips:
	ip_a = '10.248.127.233'
	ip_b = '10.240.53.200'
	current_time = time.time()
	print 'cur_time' + str(int(current_time))
	flow_instance = get_rrd(ip_a, ip_b, str(int(current_time)))		
	list_to_ret.append(flow_instance)
	return list_to_ret

def get_rrd(ip_a, ip_b, current_time):
	ip_a = ip_a.rstrip('\n')
	ip_b = ip_b.rstrip('\n')
	db_name = ip_a.rstrip('\n')+"_"+ip_b.rstrip('\n')+".rdd"
	db_full_name = '/opt/openstack_extra.aman/rrdb/'+db_name
	print db_name
	print str(int(current_time) - 5*120)
	print str(current_time)
	data = rrd_fetch(db_full_name, "AVERAGE", "--start", str(int(current_time) - 5*120), "--end", str(current_time))
	print data
	speed_vals = data[2]
	print speed_vals
	data_src_sum = 0
	data_dst_sum = 0
	for tuple in speed_vals:
		if tuple[0] is not None:
			data_src_sum += tuple[0]
		if tuple[1] is not None:
			data_dst_sum += tuple[1]
	data_src_sum = int(data_src_sum)
	data_dst_sum = int(data_dst_sum) 
	data_src_avg = data_src_sum/len(speed_vals)*120
	data_dst_avg = data_dst_sum/len(speed_vals)*120
	
	to_ret = FlowInstance()
	to_ret.machine_a = ip_a
	to_ret.machine_b = ip_b
	to_ret.current_load_src = data_src_avg
	to_ret.current_load_dst = data_dst_avg
	to_ret.current_time = int(current_time)

	return to_ret

