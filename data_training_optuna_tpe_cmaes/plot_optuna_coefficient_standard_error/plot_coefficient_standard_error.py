import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

x1 = range(1,17)
x1sparse = range(4,17,4)
x1ticks = range(4,17,4)

y0 = (1.509,6.098,1.509,6.098, 0.647,5.098,0.089,3.935,0.700,4.352,0.683,5.098,0.611,3.901,0.661,5.098)
y1 = (1.561,5.785,1.561,5.785, 0.969,4.987,0.694,4.324,0.668,4.058,0.959,4.987,0.720,3.851,1.090,4.987)

z0 = (0.014,0.039,0.014,0.039, 0.043,0.032,0.058,0.038,0.050,0.035,0.043,0.032,0.033,0.047,0.040,0.032)
z1 = (0.004,0.013,0.004,0.013, 0.020,0.010,0.016,0.012,0.024,0.015,0.010,0.010,0.028,0.007,0.025,0.010)

bar_color = ('dodgerblue','orangered')
legend_array = ('RL','CMAES')

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.ylim((-0.2, 9.0))

plt.plot(x1, y0, color='dodgerblue')
plt.plot(x1, y1, color='orangered')
plt.scatter(x1, y0, color='dodgerblue')
plt.scatter(x1, y1, color='orangered')

plt.legend(legend_array, fontsize=20)
plt.xlabel('Coefficient Number', fontsize=20)
plt.ylabel('Average Coefficient', fontsize=20)
plt.tick_params(labelsize=20)
plt.xticks(x1sparse, x1ticks)

plt.savefig(current_path+'coefficients.'+image_file_extension)

plt.cla()

plt.ylim((-0.01, 0.10))

plt.plot(x1, z0, color='dodgerblue')
plt.plot(x1, z1, color='orangered')
plt.scatter(x1, z0, color='dodgerblue')
plt.scatter(x1, z1, color='orangered')

plt.legend(legend_array, fontsize=20)
plt.xlabel('Coefficient Number', fontsize=20)
plt.ylabel('Standard Error', fontsize=20)
plt.tick_params(labelsize=20)
plt.xticks(x1sparse, x1ticks)

plt.savefig(current_path+'coefficient_standard_errors.'+image_file_extension)

