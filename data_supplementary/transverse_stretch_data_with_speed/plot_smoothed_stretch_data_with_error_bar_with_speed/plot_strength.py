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
chart_ylable = 'Strength (GPa)'

x1 = (numpy.log(0.1)/numpy.log(2.0)+4.0,
      numpy.log(1.0)/numpy.log(2.0)+4.0,
      numpy.log(2.0)/numpy.log(2.0)+4.0,
      numpy.log(4.0)/numpy.log(2.0)+4.0,
      numpy.log(10.0)/numpy.log(2.0)+4.0,
      numpy.log(20.0)/numpy.log(2.0)+4.0,
      numpy.log(40.0)/numpy.log(2.0)+4.0)
x1ticks = (0.1,1.0,2.0,4.0,10.0,20.0,40.0)

y1 = numpy.array((1196.12,1086.85,1125.72,1152.76,1224.00,1247.71,1324.56))*0.001
y2 = numpy.array(( 687.84, 621.30, 620.47, 624.01, 638.20, 642.73, 643.01))*0.001
y3 = numpy.array(( 440.25, 407.99, 414.77, 431.46, 467.04, 491.12, 498.58))*0.001

y1e= numpy.array((  24.69,   7.36,   7.05,   8.33,   9.68,   7.71,  12.28))*0.001
y2e= numpy.array((  13.65,   3.71,   3.55,   4.00,   4.80,   5.50,   6.16))*0.001
y3e= numpy.array((   5.66,   2.60,   2.31,   2.94,   3.66,   4.17,   3.79))*0.001

legend_array = ('Vertical','Horizontal','Slant')

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.10
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xticks(x1,x1ticks,rotation=30)
plt.ylim((0.0, 2.7))

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

plt.savefig(current_path+'strength.'+image_file_extension)

