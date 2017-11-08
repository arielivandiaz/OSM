echo "Evaluating Dataset : VSUMM1 with CUS"
echo "Epsilon:0.5"
echo "Users:5"
echo "Simple zone"





../../build/osm --method cus -e 0.5 -n 5 -f 2091 -r "../UserSummary/v25" -i "../VSUMM2Summary/v25" --verbose 
../../build/osm --method cus -e 0.5 -n 5 -f 2091 -r "../UserSummary/v25" -i "../VSUMM2Summary/v25" --verbose 


echo "Done!"
