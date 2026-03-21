#!/usr/bin/sh

python_name=python3
image_file_extension=png

if [ $# -gt 0 ];then
python_name=$1
fi
if [ $# -gt 1 ];then
image_file_extension=$2
fi

echo "Python name: $python_name"
echo "Image file extension: $image_file_extension"

for i in $(ls ./*.txt);do

$python_name plot_optuna_reward_with_step.py $i $image_file_extension

done


