# Smart-Mirror
Google Assistant + Facial Recognition

**Todo: insert demo video with UI and interactions**

## Hardware Configuration
| Device | Operating System | Components | Getting Started |
| --- | --- | --- | --- | 
| Jetson Nano 2GB | Linux4Tegra (Ubuntu 18.04) | Python3, DLIB, CUDA | [setup + install](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit), [README](./face_recog/README.md) |
| Raspberry Pi 4 | Debian 11 (bullseye) | MagicMirror + Modules | [generic setup](https://www.raspberrypi.com/documentation/computers/getting-started.html), [README](./firebase-smarthome/README.md)

## Device Packages + Organization
For the Jetson Nano 2GB, setup the following: 
| Directory | Purpose |
| --- | --- |
| face_recog/ | Google Pub/Sub publisher when known face is detected <br> Local Face Encodings from user-uploaded .jpgs

For the Raspberry Pi 4, setup the following:
| Repository | Purpose |
| --- | --- |
| firebase-smarthome/ | Firebase Function + Testing user-interface
| [Magic Mirror](https://github.com/MichMich/MagicMirror) | MagicMirror User Interface
| [MMM-DeviceControl](https://github.com/jeffmur/MMM-DeviceControl) | Smart TV - Volume & Display control
| [MMM-GoogleAssistant](https://github.com/jeffmur/MMM-GoogleAssistant) | Embedded Assistant api v2
| [MMM-ProfileSwitcher](https://github.com/jeffmur/MMM-ProfileSwitcher) | Google Pub/Sub subscriber for events
