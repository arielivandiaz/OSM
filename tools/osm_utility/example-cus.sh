echo "Evaluating Dataset : VSUMM2Summary/v21 with CUS"
echo "Epsilon:0.5"
echo "Users:5"
echo "Simple zone"


../../build/osm --method cus -e 0.5 -n 5 -f 3279 -r "../UserSummary/v21" -i "../VSUMM2Summary/v21" --verbose 



echo "Done!"
