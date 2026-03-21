import matplotlib.pyplot as plt
import numpy
import sys

current_path=sys.path[0]+"/"

chart_title = ''
chart_xlable = 'Train loop'
chart_ylable = 'Reward'

data_file_name = sys.argv[1]

try:
    image_file_extension = sys.argv[2]
except:
    image_file_extension = 'png'

output_image_file_name = data_file_name+'.'+image_file_extension

legend_array = ('Average Reward','Max Reward')

y1 = numpy.loadtxt(data_file_name)[1:,1]
y2 = numpy.loadtxt(data_file_name)[1:,-1]

x1 = numpy.arange(0,len(y1))+1

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.ylim((-10.0, 110.0))

plt.plot(x1,y1,color='dodgerblue')
plt.plot(x1,y2,color='limegreen')
plt.scatter(x1,y1,color='dodgerblue')
plt.scatter(x1,y2,color='limegreen')

plt.title(chart_title)

plt.legend(legend_array, fontsize=20)
plt.tick_params(labelsize=20)
plt.xlabel(chart_xlable, fontsize=20)
plt.ylabel(chart_ylable, fontsize=20)

plt.savefig(current_path+output_image_file_name)

