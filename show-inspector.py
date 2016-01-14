import json
import math
import sys

def convertSize(size):
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size,1024)))
   p = math.pow(1024,i)
   s = round(size/p,2)
   if (s > 0):
       return '%s %s' % (s,size_name[i])
   else:
       return '0B'


fname = sys.argv[1]

f = open(fname)
data = json.load(f)
f.close()

ram_total = 0
disks = []
cpus = {} 


for i in data:
	if i[0] == 'memory' and i[2] == 'size':
#		print "\t{bank}: {size}".format(bank=i[1], size=convertSize(int(i[3])))
		ram_total += int(i[3])

	if i[0] == 'disk' and i[2] == 'size':
		disks.append([i[1], i[3]])

	if i[0] == 'cpu' and i[2] == 'number':
		cpus[i[1]] = i[3]

	if i[0] == 'ipmi' and i[2] == 'mac-address':
		ipmi_mac = i[3]
	if i[0] == 'ipmi' and i[2] == 'ip-address':
		ipmi_ip = i[3]




print "Node "+fname.replace('extra_hardware-', '')+" ({ipmi_ip} / {ipmi_mac}): ".format(ipmi_mac=ipmi_mac, ipmi_ip=ipmi_ip)

print "\tRAM: {size}".format(size=convertSize(ram_total))
print "\tDisks:"
for disk in disks:
	print "\t - /dev/{drive}: {disk_size}".format(drive=disk[0], disk_size=disk[1])

print "\tCPU: physical: {physical} / logical: {logical}".format(physical=cpus['physical'], logical=cpus['logical'])

print "\n"



