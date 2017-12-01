mkdir build
cd build
cmake ..
make
./opencv_binary -i=../../data/v21.mpg -o=../../output/v21 -s=0.4 -n=0.96 -d=0.25 -t=30 -e=3
