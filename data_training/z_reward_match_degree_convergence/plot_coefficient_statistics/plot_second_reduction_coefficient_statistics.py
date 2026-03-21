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
chart_ylable = r'$\rm{kcal/mol/\AA}$'

x1 = (1,2,3,4,5,6)
x1ticks = (r'$\epsilon_{p11}$',r'$\epsilon_{p12}$',r'$\epsilon_{p13}$',r'$\epsilon_{p22}$',r'$\epsilon_{p23}$',r'$\epsilon_{p33}$')

y1 = numpy.array(((1.0000,1.0000,1.0000,1.0000,1.0000,1.0000),
                  (0.5936,0.6656,0.5233,0.5422,0.5065,1.3480),
                  (0.5333,0.5046,1.2950,0.7784,0.5378,0.5887),
                  (0.5047,0.6459,0.5825,0.5122,0.5026,0.9955),
                  (0.8337,0.5662,0.5721,0.6500,0.5733,1.0800),
                  (0.5189,0.7708,0.6890,0.5328,0.6166,1.0100),
                  (0.5095,1.0360,0.7219,0.5028,0.7150,0.9519),
                  (0.5289,0.9557,0.6400,0.5189,0.5233,0.8390),
                  (0.5391,0.9796,0.6193,0.5107,0.5226,0.7518),
                  (0.5169,0.8131,0.7793,0.5466,0.5904,0.9424),
                  (0.5650,0.9424,0.7679,0.5203,0.5186,0.9741),
                  (0.6112,0.6891,0.7130,0.5346,0.5541,0.9190)))

#legend_array = ('','','')

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xticks(x1,x1ticks)

plt.fill_between(x1,0.50*y1[0],1.50*y1[0],color='lightgrey')

for i in range(1,len(y1)):
    plt.plot(x1,y1[i])
    plt.scatter(x1,y1[i])

plt.title(chart_title)

#plt.legend(legend_array, fontsize=20)
plt.tick_params(labelsize=20)
plt.xlabel(chart_xlable, fontsize=20)
plt.ylabel(chart_ylable, fontsize=20)

plt.savefig(current_path+'second_reduction_coefficient_statistics.'+image_file_extension)

