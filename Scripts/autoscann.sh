#!/bin/bash
echo "Insira um Ranger:"
read RANGE

nmap -sP $RANGE | grep for | cut -d " " -f5

echo "Está aí man!!"
