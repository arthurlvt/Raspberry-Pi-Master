# JOY PI IT - HOW TO USE IT ?

> [!IMPORTANT]
> **You can only use Joy Pi It with Raspberry Pi 3B+ and 4B !**

## Hello Guys !!

--> A few years ago, I got the Joy Pi by Joy It wich is an educational suitcase with a lot of electronic sensors and components !
--> You should keep a laptop with you if you don't want to lose your time !
        
## First, Download and Getting Started

1. Firstly, you need to install any OS on your Raspberry Pi ! Personaly, I chose [**Raspbian**](https://www.raspberrypi.com/software/), the easiest to use !
|-> Go on [**Raspbian.com**](https://www.raspberrypi.com/software/) and download Raspberry Pi Imager on your PC
        -> When installed, select your Raspberry model, the OS you want (Raspberry Pi OS for my part) and finally chose when you want to install it (SD Card)
        -> Then, put your SD Card in Raspberry Pi and let's start !

2. Connect your Raspberry Pi to Joy It by the HDMI, the GPIO and the last cable on any USB port
3. To don't get in trouble, you need to also install some libraries on your Raspberry Pi. First, go on the command prompt, and type this :
   
```python
sudo get-apt install python-pip3'
```
> It'll allow to use 'pip3 install...' instead of 'sudo apt get install...'
> Next, you have to install RPi.GPIO library this way:

```python
sudo apt-get install rpi.gpio
```

--> Do it again for these libraries : **time** ; **datetime** ; **warnings** ; **mfrc522** ;

## Now, let's start to code

--> On the Raspberry Pi, you have 2 softwares to code : Thonny and Geany. We'll use Thonny for this tutorial ! To open Thonny, go on top left and corner on raspbian 
    icon, select coding (first one) and then Thonny.

--> Now, you are ready to code ! I was inspired by [Pascal from Gagnebin.tech](https://gagnebin.tech/joy-pi/) to make this tutorial so don't hesitate to go on it.

> [!IMPORTANT]
> **To use all of sensors and components, you need to use the switch according to the sensor because they use different ones but I'll tell you when you'll to move it !**

# I hope you'll have fun !!
