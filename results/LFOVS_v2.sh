sh clean.sh
rm run.sh
#VSUMM1
python ../tools/osm_utility/osm_utiity_out.py ../videos/VSUMM ../user_summaries/VSUMM ../auto_summaries/VSUMM1 -cus -g -lfovs -lfovs_s 0.39 -lfovs_n 0.95 -lfovs_d 0.19 -lfovs_t 30 -lfovs_e 3

sh run.sh

python ../tools/get_average/get_average.py output.csv averange.txt LFOVS      

