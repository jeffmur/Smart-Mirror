# Live Facial Recognition
With [DLIB](https://github.com/davisking/dlib.git) and [Face-Recognition](https://pypi.org/project/face-recognition).

At the time of development, November 16th, 2021, DLIB cannot be successfully installed with Conda or Pip, thus requiring a patch for the Jetson Nano 2GB. \
You may skip these steps if dlib and face_recognition lib in Python3 work for you. 

Otherwise, this [tutorial](https://sparkle-mdm.medium.com/python-real-time-facial-recognition-identification-with-cuda-enabled-4819844ffc80) on Medium helped me achieve a successful install. \
I've extended the tutorial to create an isolated enviornment with Anaconda to prevent <span style="color: red">dependency hell.</span>

## Installing dependences
``` bash
$ sudo apt-get update
$ sudo apt-get install python3-dev
$ sudo apt-get install build-dep python3
$ sudo apt-get install libblas-dev liblapack-dev libatlas-base-dev
$ sudo apt-get upgrade
```

## Conda Enviornment 
Note: I used [Miniconda](https://docs.conda.io/en/latest/miniconda.html#linux-installers) for venv
``` bash
$ cd face_recog/
$ conda create --name face_recon --file envs/conda-env.txt
$ conda activate face_recon
```

## Nvidia Jetson Patch for DLIB
Note the version number here...
``` bash
$ git clone -b v19.21 https://github.com/davisking/dlib.git
$ cd dlib/
$ git am 0001-arch-for-Nano.patch
$ make
```
[Patch](https://forums.developer.nvidia.com/t/issue-with-dlib/158818/5) on nvidia developer forums.


## Compile and Install
Take note of your gcc version, mine is gcc version 7.5.0. Can be found via: 
``` sh
$ gcc -v
```

Enter the foler dlib and find setup.py file. This contains all the stuff describing how to install it. \
Open it, and add the following line in it:
``` python
os.environ["CC"] = "gcc-7"
```

## Building on Jetson
```
$ mkdir build && cd build
$ cmake --build . --config Release
$ sudo ldconfig
```

## Installing Dependencies
For [recog_known.py](./recog_known.py). \
<span style="color: red">Important:</span> Must in an active conda enviornment!
```
(face_recon) $ pip install -r envs/pip-req.txt
(face_recon) $ python3 recog_known.py
```
