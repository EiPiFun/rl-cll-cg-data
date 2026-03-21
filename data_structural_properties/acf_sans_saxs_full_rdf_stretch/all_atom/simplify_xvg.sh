#!/usr/bin/sh

python_name=python3
if [ $# -gt 0 ];then
python_name=$1
fi
echo "Python name: $python_name"

rm ./*.txt

for i in 1 2 3;do

$python_name simplify_xvg.py acf_cl$i.xvg 17
$python_name simplify_xvg.py sans_cl$i.xvg 17
$python_name simplify_xvg.py saxs_cl$i.xvg 17

for ((j=i;j<=3;j++));do

$python_name simplify_xvg.py rdf_cl"$i"_cl"$j".xvg 25

done

done


