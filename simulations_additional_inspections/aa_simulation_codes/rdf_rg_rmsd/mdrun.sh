#!/usr/bin/sh

gmx_name=$1
ntmpi_number=$2
ntomp_number=$3
mpirun_prefix=""
grompp_appendix=""
mdrun_appendix=""

$gmx_name grompp -f em.mdp -c cellulose.gro -r cellulose.gro -p topol.top -n index.ndx -o em.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm em -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix

$gmx_name grompp -f relaxation-1-1.mdp -c em.gro -r em.gro -p topol.top -n index.ndx -o relaxation-1-1.tpr $grompp_appendix
$mpirun_prefix $gmx_name mdrun -deffnm relaxation-1-1 -ntmpi $ntmpi_number -ntomp $ntomp_number $mdrun_appendix

