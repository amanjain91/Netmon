#!/bin/bash

#Exit on first error
#set -e

for pid in $(ps aux | grep tcpdump | sed -n 1,2p | awk '{print $2}')
do
	kill $pid
done

mv current_dump_file_dst old_dump_file_dst

sh run_tcpdump_dst.sh

echo "what the heck"
touch ohyes

my_ip='10.248.127.233'
timestamp=$(date +%s)
filename=$my_ip"_"$timestamp
touch $filename

for ip in $(cat list_of_ip_addresses_v2)
do
	num_packets=$(cat old_dump_file_dst | grep $ip | wc -l)
	echo $ip" "$num_packets >> $filename
done

dst_addr='jedi001.cc.gatech.edu'
dst_path='/net/hu21/ajain68/netmon_data'

scp -i ~/.ssh/netmon $filename ajain68@$dst_addr:$dst_path
