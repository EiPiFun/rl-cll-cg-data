import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

x1 = (21,39,136,154)
x2 = (128,139,159)

x1sparse = range(40,201,40)
x1ticks = range(40,201,40)

y1 = (81.41,84.76,80.70,86.69)
y2 = (81.54,80.37,84.78)

bar_color = ('dodgerblue','orangered')
legend_array = ('With thresholds','Without thresholds')

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.ylim((-10.0, 100.0))

plt.plot(x1, y1, color='dodgerblue')
plt.plot(x2, y2, color='orangered')
plt.scatter(x1, y1, color='dodgerblue')
plt.scatter(x2, y2, color='orangered')

plt.legend(legend_array, fontsize=20)
plt.xlabel('Step', fontsize=20)
plt.ylabel('Reward', fontsize=20)
plt.tick_params(labelsize=20)
plt.xticks(x1sparse, x1ticks)

plt.savefig(current_path+'several_max_rewards_with_steps_early.'+image_file_extension)

