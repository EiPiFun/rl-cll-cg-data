#!/usr/bin/sh

rm rdf.xvg.txt
cat rdf_cl1.xvg.txt > rdf.xvg.txt

rm rg.xvg.txt
awk '{printf "%e %s\n",10*(NR-1),$2}' rg_cl1.xvg.txt > rg.xvg.txt

rm rmsd.xvg.txt
awk '{printf "%e %s\n",10*(NR-1),$2}' rmsd_cl1.xvg.txt > rmsd.xvg.txt

