import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

chart_title = ''
chart_xlabel = 'Length and width'
chart_ylabel = 'Computational efficiency (nm/ns)'

x1 = numpy.array(
     (numpy.log(6)/numpy.log(2.0)-3.0,
      numpy.log(9)/numpy.log(2.0)-3.0,
      numpy.log(12)/numpy.log(2.0)-3.0,
      numpy.log(18)/numpy.log(2.0)-3.0,
      numpy.log(24)/numpy.log(2.0)-3.0,
      numpy.log(36)/numpy.log(2.0)-3.0,
      numpy.log(48)/numpy.log(2.0)-3.0,
      numpy.log(64)/numpy.log(2.0)-3.0))
x1ticks = (6,9,12,18,24,36,48,64)

legend_array = ('AA(CPU)','AA(CPU+GPU)','CG(CPU)')

y1 = numpy.array((  51.3, 23.0, 13.5,  6.0,  3.4,  1.5,  0.8,  0.5))
y2 = numpy.array(( 378.6,182.2,112.2, 54.4, 31.1, 13.8,  7.6,  4.1))
y3 = numpy.array((1187.8,574.7,318.9,145.9, 81.6, 35.1, 19.2, 11.8))

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.ylim(0, 1400)

plt.bar(x1-0.1, y1, width=0.1)
plt.bar(x1+0.0, y2, width=0.1)
plt.bar(x1+0.1, y3, width=0.1)

#plt.title(chart_title)
plt.legend(legend_array, fontsize=20)
plt.xticks(x1, x1ticks)
plt.xlabel(chart_xlabel, fontsize=20)
plt.ylabel(chart_ylabel, fontsize=20)
plt.tick_params(labelsize=20)

plt.savefig(current_path+'computational_efficiency.'+image_file_extension)

