Netmon
======

Instructions to setup and run Netmon:

Step 1
Clone this repository onto the master VM as well as each of the VMs to be monitored

Step 2 
- Run ./setup_links.sh on master VM to add monitoring code to the openstack dashboard
- Then run sudo /etc/init.d/apache2 reload
- Install the following cronjon (to receive data and put it in RRDtool):
  */2 * * * * sudo sh ~/Netmon/rrdb/update_tables.sh 1>~/Netmon/rrdb/error.log 2>&1

Step 3
On each of the VMs to be monitored install the following cronjob:
*/2 * * * * sudo sh ~/Netmon/collector/statistics_sender_src.sh 1>~/Netmon/collector/error.log 2>&1

Step 4
To be able to connect to the openstack dashboard first create a socks connection to jedi001.cc.gatech.edu
Next, in your browser connect to this socks proxy server.
After this you should be able to go to website jedi001.cc.gatech.edu and login as admin

