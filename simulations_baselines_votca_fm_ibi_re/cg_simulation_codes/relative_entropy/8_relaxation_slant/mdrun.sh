#!/usr/bin/sh

gmx_name=$1
ntmpi_number=$2
ntomp_number=$3
mpirun_prefix=""
grompp_appendix=""
mdrun_appendix="-table ../table.xvg -tableb ../table_b1.xvg ../table_b2.xvg ../table_b3.xvg ../table_a1.xvg ../table_a2.xvg ../table_a3.xvg ../table_a4.xvg ../table_a5.xvg ../table_a6.xvg ../table_d1.xvg ../table_d2.xvg ../table_d3.xvg"

$gmx_name grompp -f relaxation-1-1.mdp -c em.gro -r em.gro -p topol.top -n index.ndx -o relaxation-1-1.tpr $grompp_appendix


