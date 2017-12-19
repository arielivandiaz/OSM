



sh clean.sh 

python osm_utiity.py ../../videos/VSUMM/v21.mpg ../../user_summaries/VSUMM/v21 ../../auto_summaries/VSUMM1/v21 -cus
 
sh run.sh	


cp output.txt output-"$(date +%d-%m-%H:%M:%S).txt"
cp output.csv output-"$(date +%d-%m-%H:%M:%S).csv"



