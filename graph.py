from turtle import *

class resource:
	def __init__(self,CPU,MEM):
		self.CPU = CPU
		self.MEM = MEM

	def __str__(self):
		return "CPU: " + str(self.CPU) + " MEM:" +str(self.MEM) + "\n\n"

dataArray = []

def parseFile():
	fd = open("vuln-management-pack")
	# fd.readline()
	count = 0
	while True:
		line1 = fd.readline()
		line2 = fd.readline()
		# if line2 == "\n":
		# 	continue 
		if not line2: 
			break  # EOF
		line1 = line1.split()
		line2 = line2.split()
		# print(line1[10],line2[12])
		if len(line1) == 8:
			# print(line1)
			# print(line1[5])
			# print(line1[7])
			data = dataArray[-1]
			data.CPU += float(line1[5])
			data.MEM += float(line1[7])
		if len(line2) == 14:
			# print(line2)
			# print(line2[11])
			# print(line2[13])
			dataArray.append(resource(float(line2[11]),float(line2[13])))
		# print("DATA ARRAY: "+str(dataArray))
import matplotlib.pyplot as plt

if __name__ == "__main__":
	parseFile()
	# array = []
	# for i in dataArray:
	# 	if i.MEM > 2.6:
	# 		print(i)
	plt.plot([i for i in range(0,299)],[data.CPU for data in dataArray],'r')
	plt.ylabel('CPU %')
	plt.xlabel('Time')
	plt.show()

	plt.plot([i for i in range(0,299)],[data.MEM for data in dataArray],'g')
	plt.ylabel('MEM %')
	plt.xlabel('Time')
	plt.show()

	# plt.plot([i for i in range(0,299)],[data.MEM for data in dataArray],'g',[i for i in range(0,299)],[data.CPU for data in dataArray],'r')
	# plt.ylabel('MEM and CPU %')
	# plt.xlabel('Time')
	# plt.show()