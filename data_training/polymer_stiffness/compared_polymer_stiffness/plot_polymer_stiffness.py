import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

x1 = (10,20,30)
x1ticks = ('10','20','30')

y0 = ( 9.755, 9.815, 9.716)
y1 = ( 8.990,10.176,10.106)

z0 = ( 4.523, 9.535,13.536)
z1 = ( 4.529, 9.199,13.432)

bar_color = ('dodgerblue','orangered')
legend_array = ('All atom','Coarse grained')

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.ylim((0.0, 16.0))

plt.plot(x1, y0, color='dodgerblue')
plt.plot(x1, y1, color='orangered')
plt.scatter(x1, y0, color='dodgerblue')
plt.scatter(x1, y1, color='orangered')

plt.legend(legend_array, fontsize=20)
plt.xlabel('Chain length (residue number)', fontsize=20)
plt.ylabel('Persistence length (nm)', fontsize=20)
plt.tick_params(labelsize=20)
plt.xticks(x1, x1ticks)

plt.savefig(current_path+'persistence_length.'+image_file_extension)

plt.cla()

plt.ylim((0.0, 16.0))

plt.plot(x1, z0, color='dodgerblue')
plt.plot(x1, z1, color='orangered')
plt.scatter(x1, z0, color='dodgerblue')
plt.scatter(x1, z1, color='orangered')

plt.legend(legend_array, fontsize=20)
plt.xlabel('Chain length (residue number)', fontsize=20)
plt.ylabel('End-to-end distance (nm)', fontsize=20)
plt.tick_params(labelsize=20)
plt.xticks(x1, x1ticks)

plt.savefig(current_path+'end_to_end_distance.'+image_file_extension)


