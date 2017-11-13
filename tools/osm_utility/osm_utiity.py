#!/usr/bin/env python
import h5py

import pandas as panda

import tables

import cv2
import os
import csv 
import numpy as np
import argparse
import datetime
import argparse





class get_parameters(object): 
	pass

"""
Parameters:
	
	parameters.debug
	parameters.group
	parameters.video
	parameters.users_csv
	parameters.vsum_csv
	parameters.label
	parameters.method
	parameters.format
	parameters.quality
	parameters.offset
	parameters.epsilon
	parameters.distance
	parameters.users
	parameters.video_length

"""


#/*********************************************************************************************    
def get_args():


	parser = argparse.ArgumentParser(description='OSM  UTN FRBB')

	parser.add_argument('-dbg', '--debug', action='store_true', help='Mode debug On')
	parser.add_argument('-g', '--group', action='store_true', help='A multiple output')
	parser.add_argument('video',   type=str, help='video name with extension')
	parser.add_argument('users_csv',   type=str, help='csv with users sumarization')
	parser.add_argument('vsum_csv',   type=str, help='csv with video sumarization results to evaluate ')
	parser.add_argument('-l', '--label', nargs='?',   help='The label of this execution for the file output.txt')
	parser.add_argument('-cus', '--cus', action='store_true', help='run cus metric')
	parser.add_argument('-bhi', '--bhi', action='store_true', help='run bhi metric')
	parser.add_argument('-f', '--format', nargs='?',   help='File format of the output frames')
	parser.add_argument('-q', nargs='?',  choices=range(0, 100), type=int, help='The JPG quality rate')
	parser.add_argument('-offset', nargs='?',  type=int, help='The frame selection offset ')
	parser.add_argument('-e', nargs='?',   type=float, help='Epsilon')
	parser.add_argument('-d', nargs='?',   type=int, help='Distance parameter for bhi method')
	parser.add_argument('-u', nargs='?',   type=int, help='Number of users')


	
	return vars(parser.parse_args())
	



#/*********************************************************************************************    

def process_args():

	args = get_args()

	"""
	print args['bhi']
	print args['cus']
	print args['u']
	print args['users_csv']
	print args['d']
	print args['format']
	print args['vsum_csv']
	print args['label']
	print args['q']
	print args['video']
	print args['offset']
	print args['debug']
	print args['group']
	print args['e']
	"""



	parameters = get_parameters()

	if(args['debug']):
		setattr(parameters, 'debug', 1)		
	else:
		setattr(parameters, 'debug', 0)	

	if(args['group']):
		setattr(parameters, 'group', 1)		
	else:
		setattr(parameters, 'group', 0)	


	setattr(parameters, 'video', args['video'])		
	setattr(parameters, 'users_csv', args['users_csv'])		
	setattr(parameters, 'vsum_csv', args['vsum_csv'])		


	if(args['label']):
		setattr(parameters, 'label', args['label'])		
	else:
		setattr(parameters, 'label', 0)	

	if(args['bhi'] and args['cus']):
		print "DUAL EVALUATION INPUT"


	if(args['cus']):
		setattr(parameters, 'method', 1)	
	if(args['bhi']):
		setattr(parameters, 'method', 0)	

	if(args['format']):
		setattr(parameters, 'format', args['format'])
	else:
		setattr(parameters, 'format', ".jpg")

	if(args['q']):
		setattr(parameters, 'quality', args['q'])
	else:
		setattr(parameters, 'quality', 0)

	if(args['offset']):
		setattr(parameters, 'offset', args['offset'])
	else:
		setattr(parameters, 'offset', 0)

	if(args['e']):
		setattr(parameters, 'epsilon', args['e'])
	else:
		setattr(parameters, 'epsilon', 0.4)

	if(args['d']):
		setattr(parameters, 'distance', args['d'])
	else:
		setattr(parameters, 'distance', 120)

	if(args['u']):
		setattr(parameters, 'users', args['u'])
	else:
		setattr(parameters, 'users', 5)




	return parameters


#/*********************************************************************************************    

def prin_objet(obj):

	format_obj= vars(obj)
	for i in format_obj:
		print i, " = " , format_obj[i]


#/*********************************************************************************************    


def prin_objet_in_file(obj,file):

	format_obj= vars(obj)
	for i in format_obj:
		if (format_obj[i]!= 0):
			#command='\t- {0} = {1}\n'
			#file.write(command.format(i, format_obj[i]))
			file.write("\t-" + i + "\t=\t" +  str(format_obj[i]) + '\n')
	


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
def get_frame_with_ID(parameters):

	VIDEO_NAME=	parameters.video
	USERS_CSV=	parameters.users_csv
	VSUM_CSV=	parameters.vsum_csv
	FORMAT =  	parameters.format
	FRAME_ID_OFFSET =  	parameters.offset
	JPEG_QUALITY = parameters.quality
	"""
	parameters.debug
	parameters.group
	parameters.video
	parameters.users_csv
	parameters.vsum_csv
	parameters.label
	parameters.method
	parameters.format
	parameters.quality
	parameters.offset
	parameters.epsilon
	parameters.distance
	parameters.users
	parameters.video_length
	"""

	cap = cv2.VideoCapture(VIDEO_NAME)

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



	frames=np.array(csv_to_matrix(USERS_CSV)) 

	#main_folder_output=VIDEO_NAME

	main_folder_output=os.path.splitext(VIDEO_NAME)[0] #Elminate the file extension
	
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
				cap.set(1,frame_id+FRAME_ID_OFFSET);

				#Read the next frame from the video. If you set frame 749 above then the code will return the last frame.
				ret, frame = cap.read()
				
				frame_name = folder_output + '/' + 'Frame%d' % (frame_id)	 + FORMAT
				if(JPEG_QUALITY!=0)	:
					cv2.imwrite(frame_name, frame, [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY])		
				else:
					cv2.imwrite(frame_name, frame)
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
	frames_VSUM=np.array(csv_to_matrix(VSUM_CSV)) 

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
			cap.set(1,frame_id+FRAME_ID_OFFSET);
			#Read the next frame from the video. If you set frame 749 above then the code will return the last frame.
			ret, frame = cap.read()
			
			frame_name = folder_output + '/' + 'Frame%d' % (frame_id)	  + FORMAT
			if(JPEG_QUALITY!=0)	:
				cv2.imwrite(frame_name, frame, [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY])	
			else:
				cv2.imwrite(frame_name, frame)	
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

def create_sh(parameters):

	epsilon=parameters.epsilon
	distance=parameters.distance
	users=parameters.users
	length=parameters.video_length
	video_name=	parameters.video
	method=parameters.method



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

	
	file.close()

#************************************************************************************************************


def addline_sh(parameters):

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

	
	file.close()


def output_label (parameters):

		file = open('output.txt','a')
		time=datetime.datetime.now().strftime("%H-%M-%S_%d-%m-%Y")
		file.write('\n' +"*"*140 + '\n')
		if(parameters.label):
			file.write(parameters.label + "\t\tEvaluation date: " + time + '\n')
		else:
			file.write("Evaluation date: " + time + '\n')
		prin_objet_in_file(parameters,file)
		file.write("*"*140 + '\n')
		file.write("\t\t\tusers path\t\t\t\t\tdata path\t\t\t\tCUSa\t\tCUSe\t\tprecision\trecall\t\tF-meter\t\tCohen's Kappaaa\n")

		file.close()


if __name__ == '__main__':



	param = process_args() 

	#prin_objet(param)

	video_length = get_frame_with_ID(param)

	setattr(param, 'video_length', video_length)	

	output_label(param)

	create_sh(param)
	

	print "FINISHED"