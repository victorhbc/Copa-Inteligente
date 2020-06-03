#!/bin/bash

# Get packages required for OpenCV

sudo apt-get -y install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get -y install libxvidcore-dev libx264-dev
sudo apt-get -y install qt4-dev-tools libatlas-base-dev

pip3 install opencv-python==3.4.6.27
pip3 install firebase_admin==3.1.0
pip3 install psutil==5.6.3

# Get packages required for TensorFlow

# For now, downloading the TensorFlow builds from lhelontra's "TensorFlow on ARM" repository
# Thanks lhelontra for being super awesome!
# Will change to just 'pip3 install tensorflow' once newer versions of TF are added to piwheels

#pip3 install tensorflow

version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
arch=$(uname -i)

if [ "$arch" = 'armv*' ]  || [ "$arch" = 'unknown' ]
then
    if [ $version == "3.7" ]
     then
        wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.0.0/tensorflow-2.0.0-cp37-none-linux_armv7l.whl
        pip3 install tensorflow-2.0.0-cp37-none-linux_armv7l.whl
        rm tensorflow-2.0.0-cp37-none-linux_armv7l.whl
    fi

    if [ $version == "3.5" ]
    then
        wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v1.14.0/tensorflow-1.14.0-cp35-none-linux_armv7l.whl
        pip3 install tensorflow-1.14.0-cp35-none-linux_armv7l.whl
        rm tensorflow-1.14.0-cp35-none-linux_armv7l.whl
    fi
else 
    pip3 install tensorflow==1.14.0
fi

