#!/bin/bash

echo "Compiling AlarmClock..."

cp --remove-destination bicolor8x8.pde /home/pi/Adafruit-LED-Backpack-Library/examples/bicolor8x8/

cd /home/pi/raspberry-pi-bicolor-matrix-example/
rm Print.o Wire.o WString.o main.o Adafruit_LEDBackpack.o Adafruit_GFX.o twi.o
make
./bicolor8x8
