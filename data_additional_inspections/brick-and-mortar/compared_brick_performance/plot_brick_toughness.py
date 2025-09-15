import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

chart_title = ''
chart_xlabel = 'Chain length (residue number)'
chart_ylabel = 'Max strain energy (GPa)'

x1 = numpy.array((10,20,40,60))
x2 = numpy.array((10,20,40,60,80))
x2ticks = (10,20,40,60,80)

legend_array = ('All atom','Coarse grained')

y1 = numpy.array((0.21,0.35,0.58,0.77))
y2 = numpy.array((0.19,0.28,0.54,0.96,1.14))

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.ylim(0, 1.6)

plt.plot(x1,y1,color='dodgerblue')
plt.plot(x2,y2,color='orangered')
plt.scatter(x1,y1,color='dodgerblue')
plt.scatter(x2,y2,color='orangered')

#plt.title(chart_title)
plt.legend(legend_array, fontsize=20)
plt.xticks(x2, x2ticks)
plt.xlabel(chart_xlabel, fontsize=20)
plt.ylabel(chart_ylabel, fontsize=20)
plt.tick_params(labelsize=20)

plt.savefig(current_path+'brick_toughness.'+image_file_extension)

