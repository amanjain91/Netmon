#!/bin/bash

#Exit on first error
#set -e

cd ~/dev/collector

for pid in $(ps aux | grep tcpdump | awk '{print $2}')
do
	kill $pid
done

mv ~/dev/collector/current_dump_file_src ~/dev/collector/old_dump_file_src
mv ~/dev/collector/current_dump_file_dst ~/dev/collector/old_dump_file_dst

sh ~/dev/collector/run_tcpdump_src.sh

my_ip='10.248.127.233'
timestamp=$(date +%s)
filename_src=$my_ip"_"$timestamp"_src"
filename_dst=$my_ip"_"$timestamp"_dst"
touch ~/dev/collector/$filename_src
touch ~/dev/collector/$filename_dst

for ip in $(cat ~/dev/collector/list_of_ip_addresses_v2)
do
	num_packets_src=$(cat ~/dev/collector/old_dump_file_src | grep $ip | wc -l)
	num_packets_dst=$(cat ~/dev/collector/old_dump_file_dst | grep $ip | wc -l)
	echo $ip" "$num_packets_src >> $filename_src
	echo $ip" "$num_packets_dst >> $filename_dst
done

dst_addr='jedi001.cc.gatech.edu'
#dst_path='/net/hu21/ajain68/netmon_data'
dst_path='/opt/openstack_extra.aman/netmon_data/'
scp -i ~/.ssh/netmon ~/dev/collector/$filename_src ajain68@$dst_addr:$dst_path
scp -i ~/.ssh/netmon ~/dev/collector/$filename_dst ajain68@$dst_addr:$dst_path
