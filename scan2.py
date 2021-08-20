#!/usr/bin/python

import nmap
nm = nmap.PortScanner()

host_scan = input('host scan:')
while host_scan=='':
    host_scan = input('host scan:')

nm.scan(hosts=host_scan,arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x,nm[x]['status']['state'])  for x in nm.all_hosts() ]
archivo = open( 'scan.txt','w' )

for host,status in hosts_list:
    print (host,status)
    archivo.write(host+'\n')

archivo.close()