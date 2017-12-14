#!/usr/bin/env python



import os
import csv 
import numpy as np

import datetime
import argparse
from os import walk

run_osm = """
../src/build/osm --method cus -e 0.5 -d 120 -n 5 -f 2674 -r "/v42/reference" -i "/v42/data/ " 
"""

run_lfovs= """
./../LFOVS/build/opencv_binary -i=../v42.mpg -o=../v42/data -s=%f -n=%f -d=%f -t=%d -e=%d 
"""

#./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v42.mpg -o=../output/v42/data -s=0.45 -n=0.98 -d=0.25 -t=30.0 -e=18 
#../src/build/osm --method cus -e 0.5 -d 120 -n 5 -f 3591 -r "../output/v42/reference" -i "../output/v42/data/" --enable-double-zone

class measure:

	cus_a = None
	cus_e = None
	precision = None
	recall = None
	f_meter = None
	kappa = None

	def __init__(self, array):

		self.cus_a=float(array[1][0])
		self.cus_e=float(array[1][1])
		self.precision=float(array[1][2])
		self.recall=float(array[1][3])
		self.f_meter=float(array[1][4])
		self.kappa=float(array[1][5])


	def __str__(self):


		print "File Lecture: "
		return "\n Cus a = % f \n Cus e = % f \n Precision = % f \n Recall = % f \n F-meter = % f \n Kappa = % f \n  " % ( self.cus_a,self.cus_e,self.precision, self.recall, self.f_meter, self.kappa)


def csv_to_matrix(file):

	file= file + '.txt'
   
	output = np.array(list(csv.reader(open(file, "rb"), delimiter=",")))

	return output

def sh(script):
    os.system("bash -c '%s'" % script)



if __name__ == '__main__':

		output=csv_to_matrix('averange')

		actual = measure(output)
	

		#print actual

		sh(run_osm)

