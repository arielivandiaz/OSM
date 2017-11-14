#!/usr/bin/env python

import cv2
import argparse


#/*********************************************************************************************    
def get_args():


	parser = argparse.ArgumentParser(description='Process some integers.')

	parser.add_argument('video',   type=str, help='video name with extension')	
	
	args = vars(parser.parse_args())


	
	
	return args['video']


#/*********************************************************************************************    

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

if __name__ == '__main__':


	video_file  = get_args()
	
	video_length = get_video_info(video_file)

	print '*'*50
	print "VIDEO FILE:", video_file
	print "VIDEO LENGTH:", video_length
	print '*'*50

	print "FINISHED"