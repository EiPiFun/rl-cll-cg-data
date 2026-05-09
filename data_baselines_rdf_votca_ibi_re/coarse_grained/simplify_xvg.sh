#!/usr/bin/bash

python_name=python3
if [ $# -gt 0 ];then
python_name=$1
fi
echo "Python name: $python_name"

rm ./*.txt

for i in ibi re;do
for j in 1 2 3;do
for ((k=j;k<=3;k++));do

$python_name simplify_xvg.py "$i"_rdf_cl"$j"_cl"$k".xvg 25

done
done
done


