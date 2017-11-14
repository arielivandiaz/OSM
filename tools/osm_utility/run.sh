echo "Evaluating the video: ../../videos/v21.mpg with CUS"
echo "Epsilon:0.4"
echo "Users:5"
echo "Simple zone"
../../src/build/osm --method cus -e 0.4 -n 5 -f 3290 -r "../../output/v21/reference" -i "../../output/v21/data/" --verbose 
