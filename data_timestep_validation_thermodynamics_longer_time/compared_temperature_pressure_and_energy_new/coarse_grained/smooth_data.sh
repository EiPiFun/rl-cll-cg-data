#!/usr/bin/sh

python_name=python3
if [ $# -gt 0 ];then
python_name=$1
fi
echo "Python name: $python_name"

rm ./smoothed*.txt

for i in 36 81 144;do
$python_name generate_smoothed_data_for_coarse_grained.py pressure_yy_$i.txt smoothed_pressure_yy_$i.txt
done


