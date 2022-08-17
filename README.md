# 3D Discrete Morse Graph Reconstruction Python Package

DiMo3d is a python package meant for executing the discrete Morse graph reconstruction algorithm on 3D imaging data. - designed with full mouse brain imaging data in mind.  The package includes functions which allow users to divide the domain into overlapping subregions, compute persistence diagrams of each subregion, generate a discrete Morse graph reconstruction for each subregion, and merge the graphs together into a final graph reconstruction of the full domain.

* [Installation Intructions](#installation-instructions)
  * [System Requirements](#system-requirements)
  * [Required Python Libraries](#required-python-libraries)
  * [Compiling Code](#compiling-code)
  * [MATLAB Scripts](#matlab-scripts)
* [DiMo3D Functions](#dimo3d-functions)
* [Separate Programs](#separate-programs)
* [MATLAB Scripts](#matlab-scripts)
* [Example Use of Pipeline](#example-use-of-pipeline)  

## Installation Instructions
### System Requirements
- Python 3.8.8 (or newer)
- g++ 9.4.0 (or newer)
- cmake 3.16.3 (or newer)

### Required Python Libraries
- cv2 - pip install opencv-python (https://pypi.org/project/opencv-python/)
- PIL - pip install pillow (https://pypi.org/project/Pillow/)
- vtk - pip install vtk (https://pypi.org/project/vtk/)

### Compiling Code

Dipha Persistence Module

    > cd ./DiMo3d/code/dipha-3d/
    > mkdir build
    > cd build
    > cmake ../
    > make

Discrete Morse Graph Reconstruction Module

    > cd ./DiMo3d/code/dipha-output/
    > g++ ComputeGraphReconstruction.cpp
    
Merge Complex Module
		> cd DiMo3d/code/merge/
    > g++ combine.cpp

Complex Persistence + Discrete Morse Graph Reconstruction Module
		> cd DiMo3d/code/spt_cpp/
    > g++ DiMoSC.cpp -I./phat/include -std=c++11 -o spt_cpp
    
### MATLAB Scripts

    > cp ./DiMo3d/code/matlab/* ./

## DiMo3d Functions

###DiMo3d.split_domain(input_dir, output_dir, x_len, y_len, z_len, overlap=5i)

#### Description
Divide the input domain into overlapping sub-rectangular prisms.

#### Input
- Input_dir - path to input image stack
- output_dir - path to dir containing results for each subregion
- x_len - x-axis length of each subregion
- y_len - y-axis length of each subregion
- z_len - z-axis length of each subregion
- overlap - pixel overlap for each axis between adjacent subregions

#### Output

Output dir is made containing subdirectories for each region.  Each region contains an image stack and its startings x,y,z coordinates
Returns nx, ny, nz, and overlap - the x/y/z dimensions of the image stack and the overlap for each axis

#### Example

    >import DiMo3d as dm

    >image_stack_dir = “data/image_stack/”
    >morse_dir = “results/image_stack_morse/”
    >dm.split_domain(image_stack_dir, morse_dir, 64, 64, 64, 5)

