#!/usr/bin/sh

python_name=python3
plot_color=black
image_file_extension=png

if [ $# -gt 0 ];then
python_name=$1
fi
if [ $# -gt 1 ];then
plot_color=$2
fi
if [ $# -gt 2 ];then
image_file_extension=$3
fi

echo "Python name: $python_name"
echo "Plot color: $plot_color"
echo "Image file extension: $image_file_extension"

# Stretch

$python_name generate_displacement.py stretch_pullx.xvg.txt stretch_pull_displacement.xvg.txt

$python_name plot.py stretch_pull_displacement.xvg.txt stretch_pullf.xvg.txt "" "Displacement (nm)" "Force (nN)" "1.0" "0.00166" $plot_color $image_file_extension
$python_name plot_and_save_the_smoothed.py stretch_pull_displacement.xvg.txt stretch_pullf.xvg.txt "" "Displacement (nm)" "Force (nN)" "1.0" "0.00166" $plot_color $image_file_extension
$python_name plot_and_save_the_sorted_smoothed.py stretch_pull_displacement.xvg.txt stretch_pullf.xvg.txt "" "Displacement (nm)" "Force (nN)" "1.0" "0.00166" $plot_color $image_file_extension

