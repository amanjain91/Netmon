#!/bin/bash

#Exit on first error
set -e

ips_dst=$(sed -n 1p ~/dev/collector/list_of_ip_addresses)
ips_src=$(sed -n 2p ~/dev/collector/list_of_ip_addresses)
sudo tcpdump -n $ips_dst >> ~/dev/collector/current_dump_file_dst &
sudo tcpdump -n $ips_src >> ~/dev/collector/current_dump_file_src &
