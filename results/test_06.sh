


sh clean.sh 
python ../tools/osm_utility/osm_utiity_out.py ../videos/VSUMM ../user_summaries/VSUMM ../auto_summaries/VSUMM1 -cus -g -l test06 -e 0.7
sh run.sh	


python ../tools/get_average/get_average.py output.csv averange.txt test01      


cp output.txt DATA/output-"$(date +%d-%m-%H:%M:%S).txt"
cp output.csv DATA/output-"$(date +%d-%m-%H:%M:%S).csv"
cp averange.txt DATA/output-averange-"$(date +%d-%m-%H:%M:%S).csv"
rm output.txt
rm output.csv
rm averange.txt


