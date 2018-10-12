# Install Kali Linux Tools Using Katoolin

## I have tested Katoolin in Ubuntu 16.04 LTS server edition. However, It should work on other Ubuntu derivatives.

## Since it is written using Python language, you need to install Python on your Linux box.

## To install python and other required prerequisites on DEB based systems, run:
> $ sudo apt-get install python git

## After installing the prerequisites, install Katoolin as shown below:

1. 
```
> $ sudo su
```
2. 
```
> $ git clone https://github.com/LionSec/katoolin.git && cp katoolin/katoolin.py /usr/bin/katoolin
```
3. 
```
> $ chmod +x /usr/bin/katoolin
```