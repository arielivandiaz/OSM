#!/usr/bin/env python




import os
import csv 
import numpy as np
import argparse


#/*********************************************************************************************    
def get_args():


	parser = argparse.ArgumentParser(description='Process some integers.')


	parser.add_argument('input_file',   type=str, help='input csv file')
	
	args = vars(parser.parse_args())


		
	return args['input_file']



#/*********************************************************************************************    

def csv_to_matrix(file):

	
   
	output = np.array(list(csv.reader(open(file, "rb"), delimiter=",")))

	return output
	


#************************************************************************************************************

if __name__ == '__main__':

	
	input_csv = get_args()

	#CSV WITH FRAMES ID's TO CSV WITH 0 & 1

	matrix =  csv_to_matrix(input_csv)

	length_max = len(matrix)

	folder = "Output"

	os.mkdir(folder)

	i=0
	while i<length_max-1:
		if(len(matrix[i][0])>2):
			csv_name =   matrix[i][0] 
			csv_name = csv_name.replace(".", "")
			csv_name = csv_name.replace("/", "")
			csv_name +=  '.csv'
			print  csv_name
			csv_name = folder + "/" + csv_name
		i+=1




		file = open(csv_name,'w')
		frames = str(matrix[i]).replace("'", "" )
		frames = frames.replace(" ", "" )
		frames = frames.replace("[", "" )
		frames = frames.replace("]", "" )
		file.write(frames)

		file.close()

		i+=1


	print "SUCCESS"