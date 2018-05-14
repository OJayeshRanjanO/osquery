import time
import os
import subprocess
import datetime

def parseFile():
	subprocess.call("osqueryctl start",shell=True)
	CPU = 0
	Mem = 0
	count = 0
	fd2 = open("osqueryResults","w")
	try:
		while True:
			subprocess.call("ps -aux | grep /usr/bin/osqueryd > osqueryTestFile",shell=True)
			fd = open('osqueryTestFile')
			print("Time:" + str(count) +"s")
			for line in fd:#Read all instances of the process
				if 'osqueryTestFile' not in line and 'grep' not in line:
					line = line.split()

					CPU += float(line[2])
					Mem += float(line[3])
					# if count % 5 == 0:#Print every 5 seconds
					utc = datetime.datetime.utcnow()
					writeToFile(fd2,"["+(str(utc)[0:str(utc).index(".")])+"] Process "+ str(" ".join(line[10:])) +"\tCPU " + str(line[2]) +"\tMeM " + str(line[3])+"\n")
			count+=1 
			time.sleep(1)
			writeToFile(fd2,"\n\n")
			if count == 300:
				break
	except KeyboardInterrupt:
		writeToFile(fd2,"CPU\tMeM\n")
		writeToFile(fd2,str(CPU/count) + "\t" + str(Mem/count))
		fd.close()
		fd2.close()
		subprocess.call("osqueryctl stop",shell=True)
		subprocess.call("rm osqueryTestFile",shell=True)
		exit(0)
	except:
		fd.close()
		fd2.close()
		subprocess.call("osqueryctl stop",shell=True)
		subprocess.call("rm osqueryTestFile",shell=True)
		exit(0)
	writeToFile(fd2,"CPU\tMeM\n")
	writeToFile(fd2,str(CPU/count) + "\t" + str(Mem/count))
	fd.close()
	fd2.close()
	subprocess.call("osqueryctl stop",shell=True)
	subprocess.call("rm osqueryTestFile",shell=True)


def writeToFile(fd,text):
	print(text)
	fd.write(text)


if __name__ == "__main__":
	parseFile()

 

	# count = 0
	# PID = 0
	# totalCPU = 0
	# ProcessName = ""
	# totalMemoryUsage = 0
	# process = '/usr/sbin/ModemManager'
	# data = {}
	# try: 
	# 	while True:
	# 		fd = open("htop.html")
	# 		for line in fd.readlines():
	# 			if process in line:
	# 				line = line.replace("</span>","").replace("<span"," ").replace('style="font-weight:bold;">'," ").split()
	# 				PID = line[0]
	# 				data.setdefault(PID,{"Memory Usage":0,"CPU":0})
	# 				for fileLine in open("/proc/"+str(PID)+"/status"):
	# 					if "VmSize" in fileLine:
	# 						fileLine = fileLine.split()
	# 						memoryUsage = int(fileLine[1])

	# 				CPU = float(line[8])

	# 				if count < 1:
	# 					totalMemoryUsage += memoryUsage
	# 					totalCPU += CPU
	# 					count +=1

	# 				if CPU > 0.0:
	# 					totalMemoryUsage += memoryUsage
	# 					totalCPU += CPU
	# 					count +=1
	# 					data[PID]["Memory Usage"]+=memoryUsage
	# 					data[PID]["CPU"]+=CPU

	# 				ProcessName = line[11]
	# 				print(ProcessName,PID,CPU,memoryUsage)
	# 		fd.close()
	# 		subprocess.call("echo q | htop --no-color | aha --black --line-fix > htop.html",shell=True)
	# 		time.sleep(1)
	# except KeyboardInterrupt:
	# 	print("Stats for Individual PID \n" + str(data))
	# 	print()
	# 	print("Stats for All Processes of :"+ProcessName +"\n"+str(totalCPU/count),str(totalMemoryUsage/count))
		# subprocess.call("rm htop.html",shell=True)
