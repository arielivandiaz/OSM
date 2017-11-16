echo "Evaluating the video: ../../videos/VSUMM/v21.mpg with CUS"
echo "Epsilon:0.4"
echo "Users:5"
echo "Simple zone"
../../src/build/osm --method cus -e 0.4 -n 5 -f 3290 -r "../../output/VSUMM/reference" -i "../../output/VSUMM/data/" --verbose 
