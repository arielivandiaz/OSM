# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ariel/repos-git/OSM/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ariel/repos-git/OSM/src/build

# Include any dependencies generated for this target.
include CMakeFiles/osm.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/osm.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/osm.dir/flags.make

CMakeFiles/osm.dir/commandlinemanager.cpp.o: CMakeFiles/osm.dir/flags.make
CMakeFiles/osm.dir/commandlinemanager.cpp.o: ../commandlinemanager.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ariel/repos-git/OSM/src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/osm.dir/commandlinemanager.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/osm.dir/commandlinemanager.cpp.o -c /home/ariel/repos-git/OSM/src/commandlinemanager.cpp

CMakeFiles/osm.dir/commandlinemanager.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/osm.dir/commandlinemanager.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ariel/repos-git/OSM/src/commandlinemanager.cpp > CMakeFiles/osm.dir/commandlinemanager.cpp.i

CMakeFiles/osm.dir/commandlinemanager.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/osm.dir/commandlinemanager.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ariel/repos-git/OSM/src/commandlinemanager.cpp -o CMakeFiles/osm.dir/commandlinemanager.cpp.s

CMakeFiles/osm.dir/commandlinemanager.cpp.o.requires:

.PHONY : CMakeFiles/osm.dir/commandlinemanager.cpp.o.requires

CMakeFiles/osm.dir/commandlinemanager.cpp.o.provides: CMakeFiles/osm.dir/commandlinemanager.cpp.o.requires
	$(MAKE) -f CMakeFiles/osm.dir/build.make CMakeFiles/osm.dir/commandlinemanager.cpp.o.provides.build
.PHONY : CMakeFiles/osm.dir/commandlinemanager.cpp.o.provides

CMakeFiles/osm.dir/commandlinemanager.cpp.o.provides.build: CMakeFiles/osm.dir/commandlinemanager.cpp.o


CMakeFiles/osm.dir/frame.cpp.o: CMakeFiles/osm.dir/flags.make
CMakeFiles/osm.dir/frame.cpp.o: ../frame.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ariel/repos-git/OSM/src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/osm.dir/frame.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/osm.dir/frame.cpp.o -c /home/ariel/repos-git/OSM/src/frame.cpp

CMakeFiles/osm.dir/frame.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/osm.dir/frame.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ariel/repos-git/OSM/src/frame.cpp > CMakeFiles/osm.dir/frame.cpp.i

CMakeFiles/osm.dir/frame.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/osm.dir/frame.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ariel/repos-git/OSM/src/frame.cpp -o CMakeFiles/osm.dir/frame.cpp.s

CMakeFiles/osm.dir/frame.cpp.o.requires:

.PHONY : CMakeFiles/osm.dir/frame.cpp.o.requires

CMakeFiles/osm.dir/frame.cpp.o.provides: CMakeFiles/osm.dir/frame.cpp.o.requires
	$(MAKE) -f CMakeFiles/osm.dir/build.make CMakeFiles/osm.dir/frame.cpp.o.provides.build
.PHONY : CMakeFiles/osm.dir/frame.cpp.o.provides

CMakeFiles/osm.dir/frame.cpp.o.provides.build: CMakeFiles/osm.dir/frame.cpp.o


CMakeFiles/osm.dir/main.cpp.o: CMakeFiles/osm.dir/flags.make
CMakeFiles/osm.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ariel/repos-git/OSM/src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/osm.dir/main.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/osm.dir/main.cpp.o -c /home/ariel/repos-git/OSM/src/main.cpp

CMakeFiles/osm.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/osm.dir/main.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ariel/repos-git/OSM/src/main.cpp > CMakeFiles/osm.dir/main.cpp.i

CMakeFiles/osm.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/osm.dir/main.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ariel/repos-git/OSM/src/main.cpp -o CMakeFiles/osm.dir/main.cpp.s

CMakeFiles/osm.dir/main.cpp.o.requires:

.PHONY : CMakeFiles/osm.dir/main.cpp.o.requires

CMakeFiles/osm.dir/main.cpp.o.provides: CMakeFiles/osm.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/osm.dir/build.make CMakeFiles/osm.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/osm.dir/main.cpp.o.provides

CMakeFiles/osm.dir/main.cpp.o.provides.build: CMakeFiles/osm.dir/main.cpp.o


CMakeFiles/osm.dir/measurer.cpp.o: CMakeFiles/osm.dir/flags.make
CMakeFiles/osm.dir/measurer.cpp.o: ../measurer.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ariel/repos-git/OSM/src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/osm.dir/measurer.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/osm.dir/measurer.cpp.o -c /home/ariel/repos-git/OSM/src/measurer.cpp

CMakeFiles/osm.dir/measurer.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/osm.dir/measurer.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ariel/repos-git/OSM/src/measurer.cpp > CMakeFiles/osm.dir/measurer.cpp.i

CMakeFiles/osm.dir/measurer.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/osm.dir/measurer.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ariel/repos-git/OSM/src/measurer.cpp -o CMakeFiles/osm.dir/measurer.cpp.s

CMakeFiles/osm.dir/measurer.cpp.o.requires:

.PHONY : CMakeFiles/osm.dir/measurer.cpp.o.requires

CMakeFiles/osm.dir/measurer.cpp.o.provides: CMakeFiles/osm.dir/measurer.cpp.o.requires
	$(MAKE) -f CMakeFiles/osm.dir/build.make CMakeFiles/osm.dir/measurer.cpp.o.provides.build
.PHONY : CMakeFiles/osm.dir/measurer.cpp.o.provides

CMakeFiles/osm.dir/measurer.cpp.o.provides.build: CMakeFiles/osm.dir/measurer.cpp.o


CMakeFiles/osm.dir/pathmanager.cpp.o: CMakeFiles/osm.dir/flags.make
CMakeFiles/osm.dir/pathmanager.cpp.o: ../pathmanager.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ariel/repos-git/OSM/src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/osm.dir/pathmanager.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/osm.dir/pathmanager.cpp.o -c /home/ariel/repos-git/OSM/src/pathmanager.cpp

CMakeFiles/osm.dir/pathmanager.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/osm.dir/pathmanager.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ariel/repos-git/OSM/src/pathmanager.cpp > CMakeFiles/osm.dir/pathmanager.cpp.i

CMakeFiles/osm.dir/pathmanager.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/osm.dir/pathmanager.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ariel/repos-git/OSM/src/pathmanager.cpp -o CMakeFiles/osm.dir/pathmanager.cpp.s

CMakeFiles/osm.dir/pathmanager.cpp.o.requires:

.PHONY : CMakeFiles/osm.dir/pathmanager.cpp.o.requires

CMakeFiles/osm.dir/pathmanager.cpp.o.provides: CMakeFiles/osm.dir/pathmanager.cpp.o.requires
	$(MAKE) -f CMakeFiles/osm.dir/build.make CMakeFiles/osm.dir/pathmanager.cpp.o.provides.build
.PHONY : CMakeFiles/osm.dir/pathmanager.cpp.o.provides

CMakeFiles/osm.dir/pathmanager.cpp.o.provides.build: CMakeFiles/osm.dir/pathmanager.cpp.o


CMakeFiles/osm.dir/methodresolver.cpp.o: CMakeFiles/osm.dir/flags.make
CMakeFiles/osm.dir/methodresolver.cpp.o: ../methodresolver.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ariel/repos-git/OSM/src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object CMakeFiles/osm.dir/methodresolver.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/osm.dir/methodresolver.cpp.o -c /home/ariel/repos-git/OSM/src/methodresolver.cpp

CMakeFiles/osm.dir/methodresolver.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/osm.dir/methodresolver.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ariel/repos-git/OSM/src/methodresolver.cpp > CMakeFiles/osm.dir/methodresolver.cpp.i

CMakeFiles/osm.dir/methodresolver.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/osm.dir/methodresolver.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ariel/repos-git/OSM/src/methodresolver.cpp -o CMakeFiles/osm.dir/methodresolver.cpp.s

CMakeFiles/osm.dir/methodresolver.cpp.o.requires:

.PHONY : CMakeFiles/osm.dir/methodresolver.cpp.o.requires

CMakeFiles/osm.dir/methodresolver.cpp.o.provides: CMakeFiles/osm.dir/methodresolver.cpp.o.requires
	$(MAKE) -f CMakeFiles/osm.dir/build.make CMakeFiles/osm.dir/methodresolver.cpp.o.provides.build
.PHONY : CMakeFiles/osm.dir/methodresolver.cpp.o.provides

CMakeFiles/osm.dir/methodresolver.cpp.o.provides.build: CMakeFiles/osm.dir/methodresolver.cpp.o


# Object files for target osm
osm_OBJECTS = \
"CMakeFiles/osm.dir/commandlinemanager.cpp.o" \
"CMakeFiles/osm.dir/frame.cpp.o" \
"CMakeFiles/osm.dir/main.cpp.o" \
"CMakeFiles/osm.dir/measurer.cpp.o" \
"CMakeFiles/osm.dir/pathmanager.cpp.o" \
"CMakeFiles/osm.dir/methodresolver.cpp.o"

# External object files for target osm
osm_EXTERNAL_OBJECTS =

osm: CMakeFiles/osm.dir/commandlinemanager.cpp.o
osm: CMakeFiles/osm.dir/frame.cpp.o
osm: CMakeFiles/osm.dir/main.cpp.o
osm: CMakeFiles/osm.dir/measurer.cpp.o
osm: CMakeFiles/osm.dir/pathmanager.cpp.o
osm: CMakeFiles/osm.dir/methodresolver.cpp.o
osm: CMakeFiles/osm.dir/build.make
osm: /usr/local/lib/libopencv_cudabgsegm.so.3.2.0
osm: /usr/local/lib/libopencv_cudaobjdetect.so.3.2.0
osm: /usr/local/lib/libopencv_cudastereo.so.3.2.0
osm: /usr/local/lib/libopencv_stitching.so.3.2.0
osm: /usr/local/lib/libopencv_superres.so.3.2.0
osm: /usr/local/lib/libopencv_videostab.so.3.2.0
osm: /usr/local/lib/libopencv_aruco.so.3.2.0
osm: /usr/local/lib/libopencv_bgsegm.so.3.2.0
osm: /usr/local/lib/libopencv_bioinspired.so.3.2.0
osm: /usr/local/lib/libopencv_ccalib.so.3.2.0
osm: /usr/local/lib/libopencv_dnn_modern.so.3.2.0
osm: /usr/local/lib/libopencv_dpm.so.3.2.0
osm: /usr/local/lib/libopencv_face.so.3.2.0
osm: /usr/local/lib/libopencv_freetype.so.3.2.0
osm: /usr/local/lib/libopencv_fuzzy.so.3.2.0
osm: /usr/local/lib/libopencv_hdf.so.3.2.0
osm: /usr/local/lib/libopencv_line_descriptor.so.3.2.0
osm: /usr/local/lib/libopencv_optflow.so.3.2.0
osm: /usr/local/lib/libopencv_reg.so.3.2.0
osm: /usr/local/lib/libopencv_rgbd.so.3.2.0
osm: /usr/local/lib/libopencv_saliency.so.3.2.0
osm: /usr/local/lib/libopencv_stereo.so.3.2.0
osm: /usr/local/lib/libopencv_structured_light.so.3.2.0
osm: /usr/local/lib/libopencv_surface_matching.so.3.2.0
osm: /usr/local/lib/libopencv_tracking.so.3.2.0
osm: /usr/local/lib/libopencv_xfeatures2d.so.3.2.0
osm: /usr/local/lib/libopencv_ximgproc.so.3.2.0
osm: /usr/local/lib/libopencv_xobjdetect.so.3.2.0
osm: /usr/local/lib/libopencv_xphoto.so.3.2.0
osm: /usr/local/lib/libopencv_cudafeatures2d.so.3.2.0
osm: /usr/local/lib/libopencv_shape.so.3.2.0
osm: /usr/local/lib/libopencv_cudacodec.so.3.2.0
osm: /usr/local/lib/libopencv_cudaoptflow.so.3.2.0
osm: /usr/local/lib/libopencv_cudalegacy.so.3.2.0
osm: /usr/local/lib/libopencv_cudawarping.so.3.2.0
osm: /usr/local/lib/libopencv_photo.so.3.2.0
osm: /usr/local/lib/libopencv_cudaimgproc.so.3.2.0
osm: /usr/local/lib/libopencv_cudafilters.so.3.2.0
osm: /usr/local/lib/libopencv_cudaarithm.so.3.2.0
osm: /usr/local/lib/libopencv_calib3d.so.3.2.0
osm: /usr/local/lib/libopencv_phase_unwrapping.so.3.2.0
osm: /usr/local/lib/libopencv_video.so.3.2.0
osm: /usr/local/lib/libopencv_datasets.so.3.2.0
osm: /usr/local/lib/libopencv_dnn.so.3.2.0
osm: /usr/local/lib/libopencv_plot.so.3.2.0
osm: /usr/local/lib/libopencv_text.so.3.2.0
osm: /usr/local/lib/libopencv_features2d.so.3.2.0
osm: /usr/local/lib/libopencv_flann.so.3.2.0
osm: /usr/local/lib/libopencv_highgui.so.3.2.0
osm: /usr/local/lib/libopencv_ml.so.3.2.0
osm: /usr/local/lib/libopencv_videoio.so.3.2.0
osm: /usr/local/lib/libopencv_imgcodecs.so.3.2.0
osm: /usr/local/lib/libopencv_objdetect.so.3.2.0
osm: /usr/local/lib/libopencv_imgproc.so.3.2.0
osm: /usr/local/lib/libopencv_core.so.3.2.0
osm: /usr/local/lib/libopencv_cudev.so.3.2.0
osm: CMakeFiles/osm.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ariel/repos-git/OSM/src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Linking CXX executable osm"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/osm.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/osm.dir/build: osm

.PHONY : CMakeFiles/osm.dir/build

CMakeFiles/osm.dir/requires: CMakeFiles/osm.dir/commandlinemanager.cpp.o.requires
CMakeFiles/osm.dir/requires: CMakeFiles/osm.dir/frame.cpp.o.requires
CMakeFiles/osm.dir/requires: CMakeFiles/osm.dir/main.cpp.o.requires
CMakeFiles/osm.dir/requires: CMakeFiles/osm.dir/measurer.cpp.o.requires
CMakeFiles/osm.dir/requires: CMakeFiles/osm.dir/pathmanager.cpp.o.requires
CMakeFiles/osm.dir/requires: CMakeFiles/osm.dir/methodresolver.cpp.o.requires

.PHONY : CMakeFiles/osm.dir/requires

CMakeFiles/osm.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/osm.dir/cmake_clean.cmake
.PHONY : CMakeFiles/osm.dir/clean

CMakeFiles/osm.dir/depend:
	cd /home/ariel/repos-git/OSM/src/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ariel/repos-git/OSM/src /home/ariel/repos-git/OSM/src /home/ariel/repos-git/OSM/src/build /home/ariel/repos-git/OSM/src/build /home/ariel/repos-git/OSM/src/build/CMakeFiles/osm.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/osm.dir/depend
