echo "Evaluating the video: ../videos/VSUMM with BHI"
echo "Distance:120"
echo "Epsilon:0.5"
echo "Users:5"
echo "Simple zone"
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v46.mpg -o=../output/v46/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3591 -r "../output/v46/reference" -i "../output/v46/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v22.mpg -o=../output/v22/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2118 -r "../output/v22/reference" -i "../output/v22/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v27.mpg -o=../output/v27/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3192 -r "../output/v27/reference" -i "../output/v27/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v55.mpg -o=../output/v55/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 1740 -r "../output/v55/reference" -i "../output/v55/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v31.mpg -o=../output/v31/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2517 -r "../output/v31/reference" -i "../output/v31/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v62.mpg -o=../output/v62/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2618 -r "../output/v62/reference" -i "../output/v62/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v29.mpg -o=../output/v29/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 1944 -r "../output/v29/reference" -i "../output/v29/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v23.mpg -o=../output/v23/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 1759 -r "../output/v23/reference" -i "../output/v23/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v49.mpg -o=../output/v49/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3614 -r "../output/v49/reference" -i "../output/v49/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v32.mpg -o=../output/v32/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2689 -r "../output/v32/reference" -i "../output/v32/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v57.mpg -o=../output/v57/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3449 -r "../output/v57/reference" -i "../output/v57/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v24.mpg -o=../output/v24/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 1815 -r "../output/v24/reference" -i "../output/v24/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v56.mpg -o=../output/v56/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2325 -r "../output/v56/reference" -i "../output/v56/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v65.mpg -o=../output/v65/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2739 -r "../output/v65/reference" -i "../output/v65/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v28.mpg -o=../output/v28/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3561 -r "../output/v28/reference" -i "../output/v28/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v37.mpg -o=../output/v37/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3413 -r "../output/v37/reference" -i "../output/v37/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v36.mpg -o=../output/v36/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 4223 -r "../output/v36/reference" -i "../output/v36/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v43.mpg -o=../output/v43/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 4796 -r "../output/v43/reference" -i "../output/v43/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v64.mpg -o=../output/v64/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 5309 -r "../output/v64/reference" -i "../output/v64/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v66.mpg -o=../output/v66/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2187 -r "../output/v66/reference" -i "../output/v66/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v41.mpg -o=../output/v41/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2765 -r "../output/v41/reference" -i "../output/v41/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v42.mpg -o=../output/v42/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2674 -r "../output/v42/reference" -i "../output/v42/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v48.mpg -o=../output/v48/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3705 -r "../output/v48/reference" -i "../output/v48/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v59.mpg -o=../output/v59/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2106 -r "../output/v59/reference" -i "../output/v59/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v25.mpg -o=../output/v25/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 1797 -r "../output/v25/reference" -i "../output/v25/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v21.mpg -o=../output/v21/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3290 -r "../output/v21/reference" -i "../output/v21/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v30.mpg -o=../output/v30/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 1815 -r "../output/v30/reference" -i "../output/v30/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v34.mpg -o=../output/v34/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 4205 -r "../output/v34/reference" -i "../output/v34/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v67.mpg -o=../output/v67/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2722 -r "../output/v67/reference" -i "../output/v67/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v69.mpg -o=../output/v69/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3616 -r "../output/v69/reference" -i "../output/v69/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v58.mpg -o=../output/v58/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3186 -r "../output/v58/reference" -i "../output/v58/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v33.mpg -o=../output/v33/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3261 -r "../output/v33/reference" -i "../output/v33/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v38.mpg -o=../output/v38/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 4570 -r "../output/v38/reference" -i "../output/v38/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v45.mpg -o=../output/v45/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2428 -r "../output/v45/reference" -i "../output/v45/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v61.mpg -o=../output/v61/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2275 -r "../output/v61/reference" -i "../output/v61/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v44.mpg -o=../output/v44/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2429 -r "../output/v44/reference" -i "../output/v44/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v40.mpg -o=../output/v40/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2940 -r "../output/v40/reference" -i "../output/v40/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v35.mpg -o=../output/v35/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2336 -r "../output/v35/reference" -i "../output/v35/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v68.mpg -o=../output/v68/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 1949 -r "../output/v68/reference" -i "../output/v68/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v53.mpg -o=../output/v53/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 1883 -r "../output/v53/reference" -i "../output/v53/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v47.mpg -o=../output/v47/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2166 -r "../output/v47/reference" -i "../output/v47/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v39.mpg -o=../output/v39/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 5254 -r "../output/v39/reference" -i "../output/v39/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v54.mpg -o=../output/v54/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2886 -r "../output/v54/reference" -i "../output/v54/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v70.mpg -o=../output/v70/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 1407 -r "../output/v70/reference" -i "../output/v70/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v52.mpg -o=../output/v52/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 3615 -r "../output/v52/reference" -i "../output/v52/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v63.mpg -o=../output/v63/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2310 -r "../output/v63/reference" -i "../output/v63/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v60.mpg -o=../output/v60/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2093 -r "../output/v60/reference" -i "../output/v60/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v26.mpg -o=../output/v26/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 6269 -r "../output/v26/reference" -i "../output/v26/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v50.mpg -o=../output/v50/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 4829 -r "../output/v50/reference" -i "../output/v50/data/" --verbose 
./../LFOVS/build/opencv_binary -i=../videos/VSUMM/v51.mpg -o=../output/v51/data -s=0.4 -n=0.96 -d=0.25 -t=30.0 -e=9 -v 
../src/build/osm --method bhi -e 0.5 -d 120 -n 5 -f 2934 -r "../output/v51/reference" -i "../output/v51/data/" --verbose 
