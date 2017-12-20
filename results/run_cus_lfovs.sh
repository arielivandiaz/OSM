
sh clean.sh

python ../tools/osm_utility/osm_utiity_out.py ../videos/VSUMM ../user_summaries/VSUMM ../auto_summaries/VSUMM1 -cus -g -lfovs -lfovs_s 0.4 -lfovs_n 0.96 -lfovs_d 0.25 -lfovs_t 30 -lfovs_e 9

sh run.sh

python ../tools/get_average/get_average.py output.csv averange.txt LFOVS_CUS      


cp output.txt DATA/output-"$(date +%d-%m-%H-%M-%S).txt"
cp output.csv DATA/output-"$(date +%d-%m-%H-%M-%S).csv"
cp averange.txt DATA/output-averange-"$(date +%d-%m-%H-%M-%S).csv"
rm output.txt
rm output.csv
rm averange.txt