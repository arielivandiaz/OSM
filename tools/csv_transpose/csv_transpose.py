#!/usr/bin/env python
import h5py

import pandas as panda

import tables

import cv2
import os
import csv 
import numpy as np
import argparse


#/*********************************************************************************************    
def get_args():


	parser = argparse.ArgumentParser(description='Process some integers.')

	parser.add_argument('input_file',   type=str, help='input csv file')
	parser.add_argument('output_file',   type=str, help='output csv file')
	
	args = vars(parser.parse_args())


	
	
	return args['input_file'],args['output_file']



#/*********************************************************************************************    

def csv_to_matrix(file):

	file= file + '.csv'
   
	output = np.array(list(csv.reader(open(file, "rb"), delimiter=",")))

	return output
	

#/*********************************************************************************************    

def matrix_to_csv(file, matrix):

	file = file +'.csv'

	df=panda.DataFrame(matrix)

	df.to_csv(file, sep=',', encoding='utf-8', index=False,header=False)




#************************************************************************************************************

if __name__ == '__main__':



	input_csv,output_csv = get_args()

	matrix = csv_to_matrix(input_csv)

	matrix=matrix.transpose()

	matrix_to_csv(output_csv,matrix)


	print "SUCCESS"