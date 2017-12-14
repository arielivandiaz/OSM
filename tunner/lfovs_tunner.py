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
../src/build/osm --method cus -e 0.5 -d 120 -n 5 -f 2618 -r ../output/v42/reference -i ../output/v42/data/ 
"""

run_lfovs= """
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v42.mpg -o=../output/v42/data -s=%f -n=%f -d=%f -t=%d -e=%d 
"""

clean_data= """
rm output.csv
rm output.txt
rm -r -f ../output/v42/data
"""

print_frames="""
ls ../output/v42/data
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


		return "\t S = % f \t N = % f \t D = % f \t T = % d \t E = % d \n" % ( self.s,self.n,self.d, self.t, self.e)


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

def file_history(params,to_tune,actual):
	
	if to_tune == 's':
		file = open('sensibility_h.txt','a')
	if to_tune == 'n':
		file = open('noise_h.txt','a')
	if to_tune == 'd':
		file = open('distance_h.txt','a')
	if to_tune == 't':
		file = open('t_h.txt','a')
	if to_tune == 'e':
		file = open('e_h.txt','a')

	file.write(str(params.s) + '\t' + str(params.n) + '\t' + str(params.d) + '\t' + str(params.t) + '\t' + str(params.e) + '\t\t' )
	file.write('cusA = ' + str(actual.cus_a) + '\t')
	file.write('cusE = ' + str(actual.cus_e) + '\t')
	file.write('precision = ' + str(actual.precision) + '\t')
	file.write('recall = ' + str(actual.recall) + '\t')
	file.write('f-meter = ' + str(actual.f_meter) + '\t')
	file.write('kappa = ' + str(actual.kappa) + '\n')
	file.close()

def file_bests(params_best,to_tune,actual):

		if to_tune == 's':
			
				file = open('sensibility.txt','w')
				file.write('Paraetros para tunning de s: \n')
	
		if to_tune == 'n':
			
				file = open('noise.txt','w')
				file.write('Paraetros para tunning de n: \n')
				
		if to_tune == 'd':
		
				file = open('distance.txt','w')
				file.write('Paraetros para tunning de d: \n')
				
		if to_tune == 't':
		
				file = open('t.txt','w')
				file.write('Paraetros para tunning de t: \n')
				
		if to_tune == 'e':
		
				file = open('e.txt','w')
				file.write('Paraetros para tunning de e: \n')
			

		
		file.write('s = ' + str(params_best.s) + '\n')
		file.write('n = ' + str(params_best.n) + '\n')
		file.write('d = ' + str(params_best.d) + '\n')
		file.write('t = ' + str(params_best.t) + '\n')
		file.write('e = ' + str(params_best.e) + '\n')
		file.write('SALIDA OSM\n')
		file.write('cusA = ' + str(actual.cus_a) + '\n')
		file.write('cusE = ' + str(actual.cus_e) + '\n')
		file.write('precision = ' + str(actual.precision) + '\n')
		file.write('recall = ' + str(actual.recall) + '\n')
		file.write('f-meter = ' + str(actual.f_meter) + '\n')
		file.write('kappa = ' + str(actual.kappa) + '\n')
		file.close()	

					


def tunning_param(params,to_tune,step,params_best):


	#Sensibility
		running=1
		best_f_meter=-5
		while(running):

			
			sh(clean_data)	
			sh(run_lfovs % (params.s,params.n,params.d,params.t,params.e))			
			
			sh(print_frames)
			print
			print params
			print	
			sh("sh run_osm.sh")	
			output=csv_to_matrix('output')
			print 
			actual = measure(output)
			if actual.f_meter > best_f_meter:
				print "BEST F METER" + '!'*20
				best_f_meter =  actual.f_meter
				if to_tune == 's':
					params_best.s = params.s	
				if to_tune == 'n':
					params_best.n = params.n
				if to_tune == 'd':
					params_best.d = params.d
				if to_tune == 't':
					params_best.t = params.t
				if to_tune == 'e':
					params_best.e = params.e			
			print

			file_history(params,to_tune,actual)
			
			if to_tune == 's':
				params.s += step
				if float(params.s) >= 1:
					running = 0
					break
			if to_tune == 'n':
				params.n += step
				if float(params.n) >= 1:
					running = 0
					break
			if to_tune == 'd':
				params.d += step
				if float(params.d) >= 1:
					running = 0
					break
			if to_tune == 't':
				params.t += step
				if float(params.t) >= 100:
					running = 0
					break
			if to_tune == 'e':
				params.e += step
				if float(params.e) >= 100:
					running = 0
					break
			

			

		print '*'*40
		print params_best
		print '*'*40

		file_bests(params_best,to_tune,actual)

		if to_tune == 's':
			return params_best.s	
		if to_tune == 'n':
			return params_best.n
		if to_tune == 'd':
			return params_best.d
		if to_tune == 't':
			return params_best.t
		if to_tune == 'e':
			return params_best.e

		



if __name__ == '__main__':


		params_best = metric(0.1,0.78,0.25,30,3)
		params = metric(0.1,0.78,0.15,15,0)

		best_f_meter=0 

		#best f-meter for sensis

		#params_best.s = tunning_param(params,'s',0.05,params_best)
		#params.s=params_best.s
		params.e=0
		params_best.e =tunning_param(params,'e',2,params_best)
