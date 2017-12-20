#!/usr/bin/env python




import os
import csv 
import numpy as np
import argparse




#/*********************************************************************************************    
def get_args():


	parser = argparse.ArgumentParser(description='Process some integers.')


	parser.add_argument('input_file',   type=str, help='input csv file')
	parser.add_argument('output_file',   type=str, help='output file')
	parser.add_argument('label',   type=str, help='label for file')
	
	args = vars(parser.parse_args())


		
	return args['input_file'], args['output_file'],args['label']



#/*********************************************************************************************    

def csv_to_matrix(file):

	
   
	output = np.array(list(csv.reader(open(file, "rb"), delimiter="\t")))

	return output
	


#************************************************************************************************************

if __name__ == '__main__':

	
	input_csv, output_file ,label = get_args()

	#CSV WITH FRAMES ID's TO CSV WITH 0 & 1

	matrix =  csv_to_matrix(input_csv)

	length_max = len(matrix)

	
	output = open (output_file , "a")

	value=[0,0,0,0,0,0]


	print matrix[1][1]
	print matrix[1][2]
	print matrix[1][3]
	print matrix[1][4]
	for i in range (0, len (matrix)):
		for j in range(0,6):
			value[j]+=float(matrix[i][j+1])

	print value

	for j in range(0,6):
			value[j]/=len (matrix)

	print value

	output.write(label)
	output.write("\n")
	output_str= str(value)
	output_str = output_str.replace("[", "")
	output_str = output_str.replace("]", "")
	output.write(output_str)
	output.write("\n")

	print "SUCCESS"