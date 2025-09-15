import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

chart_title = ''
chart_xlable = 'Stretch speed (nm/ns)'
chart_ylable = 'Direction angle'

x1 = (numpy.log(0.1)/numpy.log(2.0)+4.0,
      numpy.log(1.0)/numpy.log(2.0)+4.0,
      numpy.log(2.0)/numpy.log(2.0)+4.0,
      numpy.log(4.0)/numpy.log(2.0)+4.0,
      numpy.log(10.0)/numpy.log(2.0)+4.0,
      numpy.log(20.0)/numpy.log(2.0)+4.0,
      numpy.log(40.0)/numpy.log(2.0)+4.0)
x1ticks = (0.1,1.0,2.0,4.0,10.0,20.0,40.0)

y1 = (2.29,2.29,2.29,2.29,2.29,2.29,2.29)
y2 = (1.79,1.86,1.85,1.86,1.92,1.94,1.95)

y1e= (0.0013,0.0007,0.0007,0.0007,0.0007,0.0007,0.0007)
y2e= (0.042,0.014,0.012,0.012,0.012,0.013,0.012)

legend_array = ('Relaxation','Fracture')

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.10
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xticks(x1,x1ticks,rotation=30)
plt.ylim((0.0, 3.0))

#plt.plot(x1,y1)
#plt.plot(x1,y2)
#plt.scatter(x1,y1)
#plt.scatter(x1,y2)
plt.errorbar(x1,y1,fmt=':',yerr=y1e,elinewidth=6,capsize=9)
plt.errorbar(x1,y2,fmt=':',yerr=y2e,elinewidth=6,capsize=9)

plt.title(chart_title)

plt.legend(legend_array, fontsize=20)
plt.tick_params(labelsize=20)
plt.xlabel(chart_xlable, fontsize=20)
plt.ylabel(chart_ylable, fontsize=20)

plt.savefig(current_path+'direction_angle.'+image_file_extension)

