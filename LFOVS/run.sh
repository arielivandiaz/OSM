mkdir build
cd build
cmake ..
make
./opencv_binary -i=../../videos/VSUMM/v21.mpg -o=../../output/v21/data -s=0.4 -n=0.96 -d=0.2 -t=30 
