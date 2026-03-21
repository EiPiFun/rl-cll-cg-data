#!/usr/bin/sh

python_name=python3
if [ $# -gt 0 ];then
python_name=$1
fi
echo "Python name: $python_name"

rm ./*.txt

for i in 36 81 144;do
$python_name simplify_xvg.py temperature_$i.xvg 24
$python_name simplify_xvg.py pressure_yy_$i.xvg 24
$python_name generate_smoothed_data.py pressure_yy_$i.xvg.txt smoothed_pressure_yy_$i.xvg.txt
done


