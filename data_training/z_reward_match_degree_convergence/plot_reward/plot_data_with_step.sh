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

$python_name plot_reward_with_training_loop.py training_loop_statistic_info_pool.txt $image_file_extension

for i in first last;do

$python_name plot_reward_with_step.py ./"$i"_loop.txt $image_file_extension

$python_name plot_data_with_step.py ./"$i"_loop.txt 2 'Elastic modulus Match' $image_file_extension

$python_name plot_data_with_step.py ./"$i"_loop.txt 4 'Persistence length Match' $image_file_extension

$python_name plot_data_with_step.py ./"$i"_loop.txt 6 'End to end distance Match' $image_file_extension

$python_name plot_data_with_step.py ./"$i"_loop.txt 11 'Strength Match' $image_file_extension

$python_name plot_data_with_step.py ./"$i"_loop.txt 12 'Toughness Match' $image_file_extension

done


