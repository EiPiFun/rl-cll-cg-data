python_name=python3
if [ $# -gt 0 ];then
python_name=$1
fi
echo "Python name: $python_name"

# Stretch

$python_name simplify_xvg.py stretch_pullx.xvg 17
$python_name simplify_xvg.py stretch_pullf.xvg 17


