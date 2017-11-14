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

	parser.add_argument('video',   type=str, help='video name with extension')
	parser.add_argument('input_file',   type=str, help='input csv file')
	parser.add_argument('output_file',   type=str, help='output csv file')
	
	args = vars(parser.parse_args())


	
	
	return args['video'],args['input_file'],args['output_file']



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


#/*********************************************************************************************    

def create_random_csv(rows,cols,file,folder,binary_flag,length):
	
	size=cols*rows

	if binary_flag:
	
		data_frame =  panda.DataFrame(np.random.randint(0,2, size=(rows,cols)))
	else:
	
		summ_lenght =  np.random.randint(0,length*0.05)
		print 'SUM LEGHT:', summ_lenght
		data_frame =  panda.DataFrame(np.sort(np.random.randint(0,length, size=(rows,summ_lenght))))
		

	if os.path.exists(folder) == 0:
		print 'Folder Created :', folder
		os.mkdir(folder)
	file = folder+ '/' + file + '.csv'
	print "file route: ", file
	

	data_frame.to_csv(file, sep='\t', encoding='utf-8', index=False, header=False)


#/*********************************************************************************************    
def get_video_info(video_name):


	cap = cv2.VideoCapture(video_name)

	length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	print('FRAMES IN VIDEO:', length )

	ret, frame = cap.read()

	if frame is None: 
		print 'ERROR: VIDEO NOT FOUND'
		return
	elif length == 0:
		print 'ERROR: VIDEO NOT FOUND'
		return
	   

	cap.release()

	return length
#/*********************************************************************************************    


def IDs_to_bin_csv(lenght,file_input_csv,file_output_csv):



	frames_input=np.array(csv_to_matrix(file_input_csv)) 


	print frames_input
	#main_folder_output=video_name
	rows = len(frames_input)
	print rows

	frames_output=np.zeros(shape=(rows,lenght),dtype=int)
	
	
	if rows>1:
		for j in range ( 0, rows):
			for i in range (0, len(frames_input[j])):
				index= int(frames_input[j][i])
				frames_output[j][index]=1
				#print frames_output[j][index]

	print frames_output


 	matrix_to_csv(file_output_csv, frames_output)





#************************************************************************************************************

if __name__ == '__main__':

	
	video_file, input_csv,output_csv = get_args()

	

	#CSV WITH FRAMES ID's TO CSV WITH 0 & 1

	length =  get_video_info(video_file)

	IDs_to_bin_csv(length,input_csv,output_csv)

	print "SUCCESS"