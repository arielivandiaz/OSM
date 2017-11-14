echo "Evaluating the video: ../../videos with CUS"
echo "Epsilon:0.4"
echo "Users:5"
echo "Simple zone"
../../src/build/osm --method cus -e 0.4 -n 5 -f 3591 -r "../../output/v46/reference" -i "../../output/v46/data/" --verbose 
../../src/build/osm --method cus -e 0.4 -n 5 -f 2118 -r "../../output/v22/reference" -i "../../output/v22/data/" --verbose 
../../src/build/osm --method cus -e 0.4 -n 5 -f 3192 -r "../../output/v27/reference" -i "../../output/v27/data/" --verbose 
../../src/build/osm --method cus -e 0.4 -n 5 -f 1740 -r "../../output/v55/reference" -i "../../output/v55/data/" --verbose 
../../src/build/osm --method cus -e 0.4 -n 5 -f 2517 -r "../../output/v31/reference" -i "../../output/v31/data/" --verbose 
