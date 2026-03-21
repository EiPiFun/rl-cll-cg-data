import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

x1 = range(1,21)
x1sparse = range(4,21,4)
x1ticks = range(4,21,4)

y0 = (91.11,90.72,90.13,89.83,88.71,88.13,87.97,87.83,87.82,87.50,87.04,87.00,86.95,86.87,86.69,86.50,85.88,85.69,85.16,85.14)
y1 = (91.73,90.33,89.96,88.72,86.84,86.82,86.51,86.35,85.56,85.54,84.91,84.78,84.44,83.93,83.89,83.77,83.63,83.58,83.57,83.55)

bar_color = ('dodgerblue','orangered')
legend_array = ('With thresholds','Without thresholds')

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.ylim((-10.0, 100.0))

plt.plot(x1, y0, color='dodgerblue')
plt.plot(x1, y1, color='orangered')
plt.scatter(x1, y0, color='dodgerblue')
plt.scatter(x1, y1, color='orangered')

plt.legend(legend_array, fontsize=20)
plt.xlabel('Max rewards', fontsize=20)
plt.ylabel('Reward', fontsize=20)
plt.tick_params(labelsize=20)
plt.xticks(x1sparse, x1ticks)

plt.savefig(current_path+'several_max_rewards.'+image_file_extension)

