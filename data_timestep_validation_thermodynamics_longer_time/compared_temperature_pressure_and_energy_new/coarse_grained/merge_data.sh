#!/usr/bin/sh

for i in 36 81 144;do

rm temperature_$i.txt
awk '{printf "%e %s\n",0.012*$1,$2}' temperature_pressure_$i.txt > temperature_$i.txt

rm pressure_yy_$i.txt
awk '{printf "%e %s\n",0.012*$1,$7}' temperature_pressure_$i.txt > pressure_yy_$i.txt

done

