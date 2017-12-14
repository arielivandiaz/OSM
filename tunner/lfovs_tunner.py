#!/usr/bin/env python


import commands
import os
import csv 
import numpy as np

import datetime
import argparse
from os import walk

run_osm = """
../src/build/osm --method cus -e 0.5 -d 120 -n 5 -f 3591 -r ../output/v42/reference -i ../output/v42/data/ --enable-double-zone 
"""

run_lfovs= """
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v42.mpg -o=../output/v42/data -s=%f -n=%f -d=%f -t=%d -e=%d 
"""

clean_data= """
rm output.txt
rm output.csv
rm -r -f ../output/v42/data
"""

#./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v42.mpg -o=../output/v42/data -s=0.45 -n=0.98 -d=0.25 -t=30.0 -e=18 
#../src/build/osm --method cus -e 0.5 -d 120 -n 5 -f 3591 -r "../output/v42/reference" -i "../output/v42/data/" --enable-double-zone

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

	file= file + '.txt'
   
	output = np.array(list(csv.reader(open(file, "rb"), delimiter=",")))

	return output

def sh(script):
    os.system("bash -c '%s'" % script)



if __name__ == '__main__':


		#output=csv_to_matrix('output')

		#actual = measure(output)

		params = metric(0.5,0.98,0.25,30,18)

		print
		sh(clean_data)
		sh(run_lfovs % (0.5,0.98,0.25,30,18))
		print params
		print	
		sh("sudo sh run_osm.sh")	
		output=csv_to_matrix('output')
		actual = measure(output)
		print actual
		print
		sh(clean_data)
		params.e=5
		sh(run_lfovs % (0.5,0.98,0.25,30,5))
		print params
		print
		sh("sh run_osm.sh")
		print

