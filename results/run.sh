echo "Evaluating the video: ../videos/VSUMM/v27.mpg with BHI"
echo "Distance:120"
echo "Epsilon:0.5"
echo "Users:5"
echo "Simple zone"
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3192 -r "../output/v27/reference" -i "../output/v27/data/" --verbose 
