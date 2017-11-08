echo "Evaluating the video: ../Example_v21/v21.mpg with CUS"
echo "Epsilon:0.4"
echo "Users:5"
echo "Simple zone"
../../build/osm --method cus -e 0.4 -n 5 -f 3290 -r "../Example_v21/v21/reference" -i "../Example_v21/v21/data/" --verbose 

echo "Done!"
