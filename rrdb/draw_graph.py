import sys
import rrdtool
import time
db_name = '10.248.127.233_10.240.53.200.rdd'


ret = rrdtool.graph( "net.png", "--start", str(int(time.time()) - 20), "--vertical-label=Bytes/s",
 "DEF:inoctets="+db_name+":src:AVERAGE",
 "DEF:outoctets="+db_name+":dst:AVERAGE",
 "AREA:inoctets#00FF00:In traffic",
 "LINE1:outoctets#0000FF:Out traffic\\r",
 "CDEF:inbits=inoctets,8,*",
 "CDEF:outbits=outoctets,8,*",
 "COMMENT:\\n",
 "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
 "COMMENT:  ",
 "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps")
