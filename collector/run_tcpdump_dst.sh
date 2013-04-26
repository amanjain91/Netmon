#!/bin/bash

#Exit on first error
set -e

ips=$(sed -n 1p list_of_ip_addresses)
sudo tcpdump -n $ips & > current_dump_file_dst
