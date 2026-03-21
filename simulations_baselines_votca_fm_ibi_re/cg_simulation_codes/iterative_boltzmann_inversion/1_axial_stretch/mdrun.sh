#!/usr/bin/sh

gmx_name=$1
ntmpi_number=$2
ntomp_number=$3
mpirun_prefix=""
grompp_appendix=""
mdrun_appendix="-table ../table.xvg -tableb ../table_b1.xvg ../table_b2.xvg ../table_b3.xvg ../table_a1.xvg ../table_a2.xvg ../table_a3.xvg ../table_a4.xvg ../table_a5.xvg ../table_a6.xvg ../table_d1.xvg ../table_d2.xvg ../table_d3.xvg"

$gmx_name grompp -f relaxation-1-1.mdp -c em.gro -r em.gro -p topol.top -n index.ndx -o relaxation-1-1.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm relaxation-1-1 -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix
$gmx_name grompp -f relaxation-1-2.mdp -c relaxation-1-1.gro -r relaxation-1-1.gro -p topol.top -n index.ndx -o relaxation-1-2.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm relaxation-1-2 -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix
$gmx_name grompp -f relaxation-1-3.mdp -c relaxation-1-2.gro -r relaxation-1-2.gro -p topol.top -n index.ndx -o relaxation-1-3.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm relaxation-1-3 -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix
$gmx_name grompp -f relaxation-1-4.mdp -c relaxation-1-3.gro -r relaxation-1-3.gro -p topol.top -n index.ndx -o relaxation-1-4.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm relaxation-1-4 -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix

$gmx_name grompp -f stretch.mdp -c relaxation-1-4.gro -r relaxation-1-4.gro -p topol.top -n index.ndx -o stretch.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm stretch -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix


