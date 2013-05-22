#!/bin/bash

echo "Compiling AlarmClock..."

cd ~/raspberry-pi-bicolor-matrix-example/
rm Print.o Wire.o WString.o main.o Adafruit_LEDBackpack.o Adafruit_GFX.o twi.o
make
./bicolor8x8