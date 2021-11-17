## Smart Mirror Demo

<!-- ![Smart Mirror Demo](https://www.youtube.com/embed/5QshXc3VS9g) -->
![Thumbnail](https://img.youtube.com/vi/5QshXc3VS9g/0.jpg)(![Video](https://www.youtube.com/watch?v=5QshXc3VS9g) "Smart Mirror Demo - Click to Watch!")
## Wake Word
My wakeword is set to "jarvis", others include :
``` js
  ALEXA: ALEXA,
  AMERICANO: AMERICANO,
  BLUEBERRY: BLUEBERRY,
  BUMBLEBEE: BUMBLEBEE,
  COMPUTER: COMPUTER,
  GRAPEFRUIT: GRAPEFRUIT,
  GRASSHOPPER: GRASSHOPPER,
  HEY_GOOGLE: HEY_GOOGLE,
  HEY_SIRI: HEY_SIRI,
  JARVIS: JARVIS,
  OK_GOOGLE: OK_GOOGLE,
  PICOVOICE: PICOVOICE,
  PORCUPINE: PORCUPINE,
  TERMINATOR: TERMINATOR,
```
This is configurable in the config/config.js in MagicMirror directory. 

## User Intents
| Attribute | Query | Resource |
| --- | --- | --- |
| Volume | "Turn the volume up" <br> "Turn the volumn down" <br> "Set the volume to {VALUE} (0-100)" | [docs](https://developers.google.com/assistant/smarthome/traits/volume)
| OnOff | "Turn off the mirror" <br> "Turn on the mirror" | [docs](https://developers.google.com/assistant/smarthome/traits/onoff)

The current configuration is for a "Smart TV" which allows for even more configurations such as: Transport Control, App Selector, Input Selector, and more you can find [here](https://developers.google.com/assistant/smarthome/guides/tv)

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
