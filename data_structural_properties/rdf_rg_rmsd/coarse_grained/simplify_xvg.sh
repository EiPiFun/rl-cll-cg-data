#!/usr/bin/sh

python_name=python3
if [ $# -gt 0 ];then
python_name=$1
fi
echo "Python name: $python_name"

rm ./*.txt

for i in all layer interlayer;do

$python_name simplify_xvg.py rdf_cl1_$i.xvg 25
$python_name simplify_xvg.py rg_cl1_$i.xvg 27
$python_name simplify_xvg.py rmsd_cl1_$i.xvg 18

done

