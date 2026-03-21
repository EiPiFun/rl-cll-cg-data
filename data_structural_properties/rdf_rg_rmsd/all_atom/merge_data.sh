#!/usr/bin/sh

for i in all layer interlayer;do

rm rdf_$i.xvg.txt
cat rdf_cl1_$i.xvg.txt > rdf_$i.xvg.txt

rm rg_$i.xvg.txt
awk '{printf "%e %s\n",10*(NR-1),$2}' rg_cl1_$i.xvg.txt > rg_$i.xvg.txt

rm rmsd_$i.xvg.txt
awk '{printf "%e %s\n",10*(NR-1),$2}' rmsd_cl1_$i.xvg.txt > rmsd_$i.xvg.txt

done

