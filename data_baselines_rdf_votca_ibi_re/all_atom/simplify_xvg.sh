#!/usr/bin/bash

python_name=python3
if [ $# -gt 0 ];then
python_name=$1
fi
echo "Python name: $python_name"

rm ./*.txt

for i in 1 2 3;do
for ((j=i;j<=3;j++));do

$python_name simplify_xvg.py rdf_cl"$i"_cl"$j".xvg 25

done
done


