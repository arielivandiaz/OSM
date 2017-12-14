#!/usr/bin/env python


import commands
import os
import csv 
import numpy as np
import copy
import datetime
import argparse
from os import walk

run_osm = """
../src/build/osm --method cus -e 0.5 -d 120 -n 5 -f 2618 -r ../output/v62/reference -i ../output/v62/data/ 
"""

run_lfovs= """
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v62.mpg -o=../output/v62/data -s=%f -n=%f -d=%f -t=%d -e=%d 
"""

clean_data= """
rm output.csv
rm output.txt
rm -r -f ../output/v62/data
"""

print_frames="""
ls ../output/v62/data
"""

#./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v62.mpg -o=../output/v62/data -s=0.45 -n=0.98 -d=0.25 -t=30.0 -e=18 
#../src/build/osm --method cus -e 0.5 -d 120 -n 5 -f 3591 -r "../output/v62/reference" -i "../output/v62/data/" --enable-double-zone

class metric:

	def __init__(self, sensibility,noise,distance,t,e):

		self.s =sensibility
		self.n =noise
		self.d = distance
		self.t = t
		self.e = e

	def __str__(self):


		return "\n S = % f \n N = % f \n D = % f \n T = % d \n E = % d \n" % ( self.s,self.n,self.d, self.t, self.e)


class measure:

	cus_a = None
	cus_e = None
	precision = None
	recall = None
	f_meter = None
	kappa = None

	def __init__(self, array):

		self.cus_a=float(array[0][0])
		self.cus_e=float(array[0][1])
		self.precision=float(array[0][2])
		self.recall=float(array[0][3])
		self.f_meter=float(array[0][4])
		self.kappa=float(array[0][5])


	def __str__(self):


		
		return "\n Cus a = % f \n Cus e = % f \n Precision = % f \n Recall = % f \n F-meter = % f \n Kappa = % f \n  " % ( self.cus_a,self.cus_e,self.precision, self.recall, self.f_meter, self.kappa)


def csv_to_matrix(file):

	file= file + '.csv'
   
	output = np.array(list(csv.reader(open(file, "rb"), delimiter="\t")))

	return output

def sh(script):
    os.system("bash -c '%s'" % script)




if __name__ == '__main__':


		params_best = metric(0.1,0.98,0.25,30,9)
		params = metric(0.1,0.98,0.25,30,9)

		best_f_meter=0 

		

		#Sensibility
		running=1
		while(running):

			print
			sh(clean_data)
			sh(run_lfovs % (params.s,params.n,params.d,params.t,params.e))
			sh(print_frames)
			print params
			print	
			sh("sh run_osm.sh")	
			output=csv_to_matrix('output')
			print 
			actual = measure(output)
			if actual.f_meter > best_f_meter:
				print "BEST F METER" + '!'*20
				best_f_meter =  actual.f_meter
				params_best = copy.copy(params)
				params_best = copy.deepcopy(params)			
			
			print
		
			params.s+=0.1
			if float(params.s) >= 1:
				running = 0
				break
		print '*'*40
		print params
		print '*'*40

		file = open('sensibilidad.txt','w')
		file.write('Paraetros para tunning de sensibilidad: \n')
		file.write(params.s + '\n')
		file.write(params.n + '\n')
		file.write(params.d + '\n')
		file.write(params.t + '\n')
		file.write(params.e + '\n')
		file.write('SALIDA OSM\n')
		file.write(actual.cus_a + '\n')
		file.write(actual.cus_e + '\n')
		file.write(actual.precision + '\n')
		file.write(actual.recall + '\n')
		file.write(actual.f_meter + '\n')
		file.write(actual.kappa + '\n')
		file.close()

		params = copy.copy(params_best)
		params = copy.deepcopy(params_best)	



