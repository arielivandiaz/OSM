#!/usr/bin/env python
import h5py

import pandas as panda

import tables

import cv2
import os
import csv 
import numpy as np
import argparse

FORMAT = '.jpg'
JPEG_QUALITY = 75


#/*********************************************************************************************    
def get_args():


	parser = argparse.ArgumentParser(description='Process some integers.')

	parser.add_argument('video',   type=str, help='video name with extension')
	parser.add_argument('users_csv',   type=str, help='csv with users sumarization')
	parser.add_argument('vsum_csv',   type=str, help='csv with video sumarization results to evaluate ')
	parser.add_argument('-cus', '--cus', action='store_true', help='run cus metric')
	#parser.add_argument('-bhi', '--bhi', action='store_true', help='run bhi metric')
	
	args = vars(parser.parse_args())


	
	
	return args['video'],args['users_csv'],args['vsum_csv'],args['cus']


#/*********************************************************************************************    

def csv_to_matrix(file):

	file= file + '.csv'
   
	output = np.array(list(csv.reader(open(file, "rb"), delimiter=",")))

	return output
	

#/*********************************************************************************************    

def matrix_to_csv(file, matrix):

	file = file +'.csv'

	df=panda.DataFrame(matrix)

	df.to_csv(file, sep='\t', encoding='utf-8', index=False,header=False)


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


#Array to Frame without  Frame ID
#A: Arreglo de 0 y 1
# NOT FINISHED
def array_to_frame_without_ID(video_name,file_csv,folder_output):


	cap = cv2.VideoCapture(video_name)

	length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

	frame_id=0

	file_csv=folder_output + '/' + file_csv 

	frames=np.array(csv_to_matrix(file_csv)) 
	folder_output=folder_output+'_'+video_name
	if os.path.exists(folder_output) == 0:
		print 'Folder Created :', folder_output
		os.mkdir(folder_output)

	print frames 
	print '*' * 80
	print
	while (cap.isOpened()):
			

		display_loadging(length,frame_id,0)

		if frames[frame_id]=='1':

			
			ret, frame = cap.read()
			frame_name = folder_output + '/' + 'Frame%d' % (frame_id)	  + FORMAT		
			cv2.imwrite(frame_name, frame, [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY])			
			cv2.imwrite(frame_name, frame)

		frame_id+=1

		if frame_id==length:   
				print 'END OF VECTOR'      
				break

	cap.release()






#Array to Frame with Frame ID
#Arreglos de numeros de ID de keyframes
def get_frame_with_ID(video_name,users_csv,vsum_csv):

	cap = cv2.VideoCapture(video_name)

	if cap:
		print "VIDEO OPENED"
	else:
		print "VIDEO NOT FOUND"

	length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) #Videl Lenght
	fps =  int(cap.get(cv2.CAP_PROP_FPS)) #Videl Lenght
	time_length = float(length/fps)

	print "lenght" , length
	print "fps" , fps
	print "time_lenght" , time_length



	frames=np.array(csv_to_matrix(users_csv)) 

	#main_folder_output=video_name

	main_folder_output=os.path.splitext(video_name)[0] #Elminate the file extension
	
	if os.path.exists(main_folder_output) == 0:		
		os.mkdir(main_folder_output)
	else:
		print 'DIRECTORY', main_folder_output , 'EXISTS'

	references_folder = main_folder_output + '/' + 'reference'
	if os.path.exists(references_folder) == 0:		
		os.mkdir(references_folder)
	else:
		print 'DIRECTORY', references_folder , 'EXISTS'

	data_folder = main_folder_output + '/' + 'data'
	if os.path.exists(data_folder) == 0:		
		os.mkdir(data_folder)
	else:
		print 'DIRECTORY', data_folder , 'EXISTS'

	
	
	n_users = frames.shape[0]
	
	

	for user in range(0,n_users):

		frame_id=0
		length_array=len(frames[user])
		frame_detection=0;

		folder_output=references_folder +'/' + "user" + "%d" % (user+1 )

		if os.path.exists(folder_output) == 0:			
			os.mkdir(folder_output)
		else:
			print 'DIRECTORY', folder_output , 'EXISTS'

		while (cap.isOpened()):
			
			ret, frame = cap.read()
			#print 'id',frame_id,'  detect',frame_detection 
			if frame_detection==length_array:
				break

			if int(frames[user][frame_detection])==frame_id:
				#print 'frame detected' , frame_id

				#frame_no = float(length-1) /(time_length*fps)
				print frame_id
				#The first argument of cap.set(), number 2 defines that parameter for setting the frame selection.
				#Number 2 defines flag CV_CAP_PROP_POS_FRAMES which is a 0-based index of the frame to be decoded/captured next.
				#The second argument defines the frame number in range 0.0-1.0
				cap.set(1,frame_id);

				#Read the next frame from the video. If you set frame 749 above then the code will return the last frame.
				ret, frame = cap.read()
				
				frame_name = folder_output + '/' + 'Frame%d' % (frame_id)	 + FORMAT
				cv2.imwrite(frame_name, frame, [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY])		
				#cv2.imwrite(frame_name, frame)
				frame_detection+=1

			frame_id+=1

			if frame_id==length:   
					#print 'END OF VECTOR'      
					break
		
		print 'USER',user+1 ,'FRAMES DETECTED:',frame_detection

	#vsum



	frame_id=0

	frame_detection=0;

	folder_output=data_folder
	frames_VSUM=np.array(csv_to_matrix(vsum_csv)) 

	length_array=len(frames_VSUM[0])

		
	if os.path.exists(folder_output) == 0:
		os.mkdir(folder_output)
	else:
		print 'DIRECTORY', folder_output, 'EXISTS'

		
	while (cap.isOpened()):
			

		#print 'id',frame_id,'  detect',frame_detection 
		if frame_detection==length_array:
			break
		if int(frames_VSUM[0][frame_detection])==frame_id:
			#print 'frame detected' , frame_id
			
			#The first argument of cap.set(), number 2 defines that parameter for setting the frame selection.
			#Number 2 defines flag CV_CAP_PROP_POS_FRAMES which is a 0-based index of the frame to be decoded/captured next.
			#The second argument defines the frame number in range 0.0-1.0
			cap.set(1,frame_id);
			#Read the next frame from the video. If you set frame 749 above then the code will return the last frame.
			ret, frame = cap.read()
			
			frame_name = folder_output + '/' + 'Frame%d' % (frame_id)	  + FORMAT		
			cv2.imwrite(frame_name, frame, [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY])		
			#cv2.imwrite(frame_name, frame)
			frame_detection+=1
		
		frame_id+=1

		if frame_id==length:   
			#print 'END OF VECTOR'      
			break
	
	print 'FRAMES DETECTED:',frame_detection

	cap.release()
	return length


#************************************************************************************************************

def create_sh(epsilon,distance,users,length,video_name,method):

	file = open('run.sh','w')
	if method==False:
		print "Generating RUN.SH for BHI"
		file.write('echo "Evaluating the video: ' +video_name+ ' with BHI"\n')
		file.write('echo "Distance:'+str(distance)+ '"\n')
	else:
		print "Generating RUN.SH for CUS"
		file.write('echo "Evaluating the video: ' +video_name+ ' with CUS"\n')
		
	file.write('echo "Epsilon:'+str(epsilon)+ '"\n')	
	file.write('echo "Users:'+str(users)+ '"\n')
	file.write('echo "Simple zone"\n')

	if method==False:
		command='../../build/osm --method bhi -e {0} -d {1} -n {2} -f {3} -r "{4}/reference" -i "{4}/data/" --verbose \n'
		file.write(command.format(epsilon,distance,users,length,os.path.splitext(video_name)[0]))
	else:
		command='../../build/osm --method cus -e {0} -n {1} -f {2} -r "{3}/reference" -i "{3}/data/" --verbose \n'
		file.write(command.format(epsilon,users,length,os.path.splitext(video_name)[0]))

	file.write('\necho "Done!"\n')
	file.close()

if __name__ == '__main__':

	#osm settings
	Epsilon = 0.4
	Distance = 120
	Users = 5

	video_file, csv_users, csv_sum ,flag_method = get_args()
	
	video_length = get_frame_with_ID(video_file,csv_users,csv_sum)


	create_sh(Epsilon,Distance,Users,video_length,video_file,flag_method)

	print "FINISHED"