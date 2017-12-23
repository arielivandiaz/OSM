from os import walk
import numpy as np

file = open("files.csv","w") 

int_files=[]
for (path, ficheros, archivos) in walk("."):
	print "PATH:", path 

	file.write("%s\n" % path)
	
	for i in range (0,len(archivos)):
		
		archivos[i]=''.join(j for j in archivos[i] if j.isdigit())

		if len(archivos[i])>1:
			result=(int(archivos[i]))			
			int_files.append(result)


	file.write("%s\n" % ", ".join(map(str, sorted(int_files))))

	int_files=[]

file.close() 
