echo "Evaluating the video: ../videos/VSUMM/v21.mpg with CUS"
echo "Epsilon:0.5"
echo "Users:5"
echo "Simple zone"
../src/build/osm --method cus -e 0.5 -n 5 -f 3290 -r "../output/v21/reference" -i "../output/v21/data/" --verbose 
../src/build/osm --method cus -e 0.5 -n 5 -f 2118 -r "../output/v22/reference" -i "../output/v22/data/" --verbose 
../src/build/osm --method cus -e 0.5 -n 5 -f 1759 -r "../output/v23/reference" -i "../output/v23/data/" --verbose 
