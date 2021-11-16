## So far...

Using: https://sparkle-mdm.medium.com/python-real-time-facial-recognition-identification-with-cuda-enabled-4819844ffc80

## Installing dependences
```
$ sudo apt-get update
$ sudo apt-get install python3-dev
$ sudo apt-get install build-dep python3
$ sudo apt-get install libblas-dev liblapack-dev libatlas-base-dev
$ sudo apt-get upgrade
```

## Conda Enviornment
Note: Use Miniconda for venv
```
$ conda create -n face_recon
$ conda activate face_recon
```

## Nvidia Jetson Patch for DLIB

```
$ git clone -b v19.21 https://github.com/davisking/dlib.git
$ cd dlib/
```

DOWNLOAD ...patch.txt from website [https://forums.developer.nvidia.com/t/issue-with-dlib/158818/5]
```
$ git am 0001-arch-for-Nano.patch
$ make
```

## Modifying GCC setup.py
``` python
os.environ["CC"] = "gcc-7"
```

## Building on Jetson
```
$ mkdir build && cd build
$ cmake --build . --config Release
$ sudo ldconfig
```clear
