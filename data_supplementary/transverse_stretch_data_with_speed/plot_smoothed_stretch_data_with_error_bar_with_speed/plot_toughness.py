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
chart_ylable = 'Toughness (GPa)'

x1 = (numpy.log(0.1)/numpy.log(2.0)+4.0,
      numpy.log(1.0)/numpy.log(2.0)+4.0,
      numpy.log(2.0)/numpy.log(2.0)+4.0,
      numpy.log(4.0)/numpy.log(2.0)+4.0,
      numpy.log(10.0)/numpy.log(2.0)+4.0,
      numpy.log(20.0)/numpy.log(2.0)+4.0,
      numpy.log(40.0)/numpy.log(2.0)+4.0)
x1ticks = (0.1,1.0,2.0,4.0,10.0,20.0,40.0)

y1 = numpy.array((101.90,110.99,108.69,110.65,110.98,127.76,144.03))*0.001
y2 = numpy.array(( 65.13, 80.22, 80.60, 84.18, 77.91, 81.29, 92.67))*0.001
y3 = numpy.array((205.75,195.73,204.29,206.11,190.07,197.31,218.96))*0.001

y1e= numpy.array((  5.09,  2.70,  2.28,  3.32,  2.47,  2.72,  3.23))*0.001
y2e= numpy.array((  1.84,  3.89,  3.97,  4.66,  2.75,  2.61,  2.22))*0.001
y3e= numpy.array(( 20.60,  5.77,  5.20,  5.49,  4.56,  5.13,  4.72))*0.001

legend_array = ('Vertical','Horizontal','Slant')

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.10
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xticks(x1,x1ticks,rotation=30)
plt.ylim((0.0, 0.5))

#plt.plot(x1,y1)
#plt.plot(x1,y2)
#plt.plot(x1,y3)
#plt.scatter(x1,y1)
#plt.scatter(x1,y2)
#plt.scatter(x1,y3)
plt.errorbar(x1,y1,fmt=':',yerr=y1e,elinewidth=6,capsize=9)
plt.errorbar(x1,y2,fmt=':',yerr=y2e,elinewidth=6,capsize=9)
plt.errorbar(x1,y3,fmt=':',yerr=y3e,elinewidth=6,capsize=9)

plt.title(chart_title)

plt.legend(legend_array, fontsize=20)
plt.tick_params(labelsize=20)
plt.xlabel(chart_xlable, fontsize=20)
plt.ylabel(chart_ylable, fontsize=20)

plt.savefig(current_path+'toughness.'+image_file_extension)

