#!/usr/bin/sh

for i in 1 2 3;do

rm acf_cl$i.txt
awk '{printf "%e %s\n",14.4*(NR-1),$2}' acf_cl$i.xvg.txt > acf_cl$i.txt

done

