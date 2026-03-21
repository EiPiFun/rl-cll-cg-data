import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

chart_title = ''
chart_xlable = ''
chart_ylable = r'$\rm{\AA}$'

x1 = (1,2,3,4,5,6)
x1ticks = (r'$\sigma_{p11}$',r'$\sigma_{p12}$',r'$\sigma_{p13}$',r'$\sigma_{p12}$',r'$\sigma_{p13}$',r'$\sigma_{p13}$')

y1 = numpy.array(((5.100,4.200,4.100,5.100,3.700,5.100),
                  (5.269,4.356,4.486,5.269,3.902,5.269),
                  (5.332,3.747,4.014,5.332,4.094,5.332),
                  (5.339,3.780,4.164,5.339,4.040,5.339),
                  (5.186,3.746,3.910,5.186,4.101,5.186),
                  (5.147,3.916,4.077,5.147,4.090,5.147),
                  (5.026,3.868,4.403,5.026,3.820,5.026),
                  (4.997,4.043,4.186,4.997,3.957,4.997),
                  (5.084,4.217,4.288,5.084,3.874,5.084),
                  (5.116,4.210,4.246,5.116,4.035,5.116),
                  (5.052,4.163,4.312,5.052,3.896,5.052),
                  (5.056,4.123,4.396,5.056,3.977,5.056),
                  (5.049,4.106,4.373,5.049,3.972,5.049),
                  (5.054,4.081,4.435,5.054,3.965,5.054)))

#legend_array = ('','','')

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xticks(x1,x1ticks)

plt.fill_between(x1,0.89*y1[0],1.11*y1[0],color='lightgrey')

for i in range(1,len(y1)):
    plt.plot(x1,y1[i])
    plt.scatter(x1,y1[i])

plt.title(chart_title)

#plt.legend(legend_array, fontsize=20)
plt.tick_params(labelsize=20)
plt.xlabel(chart_xlable, fontsize=20)
plt.ylabel(chart_ylable, fontsize=20)

plt.savefig(current_path+'first_reduction_coefficient_statistics.'+image_file_extension)

