echo "Evaluating Dataset : VSUMM1Summary/v21 with BHI"
echo "Distance:120"
echo "Epsilon:0.5"
echo "Users:5"
echo "Simple zone"

../../build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3290 -r "../UserSummary/v21" -i "../VSUMM1Summary/v21" --verbose 


echo "Done!"
