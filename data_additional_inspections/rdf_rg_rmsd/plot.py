import matplotlib.pyplot as plt
import numpy
import sys

current_path = sys.path[0]+'/'
first_data_file_name = sys.argv[1]
first_data_file_location = current_path+first_data_file_name
second_data_file_name = sys.argv[2]
second_data_file_location = current_path+second_data_file_name
chart_title = sys.argv[3]
chart_xlable = sys.argv[4]
chart_ylable = sys.argv[5]
first_scale_factor = float(sys.argv[6])
second_scale_factor = float(sys.argv[7])
legend_array = (sys.argv[8],sys.argv[9])
first_plot_color = sys.argv[10]
second_plot_color = sys.argv[11]
output_image_file_name = sys.argv[12]

try:
    image_file_extension = sys.argv[13]
except:
    image_file_extension = 'png'

output_image_file_location = output_image_file_name+'.'+image_file_extension

raw_first_data = numpy.loadtxt(first_data_file_location)
raw_second_data = numpy.loadtxt(second_data_file_location)

first_data = raw_first_data*first_scale_factor
second_data = raw_second_data*second_scale_factor

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.ylim(-0.1,1.6*numpy.max((numpy.max(first_data[:,1]),numpy.max(second_data[:,1]))))

plt.plot(first_data[:,0],first_data[:,1], color=first_plot_color)
plt.plot(second_data[:,0],second_data[:,1], color=second_plot_color)

plt.title(chart_title, fontsize=20)
plt.legend(legend_array, fontsize=20)
plt.xlabel(chart_xlable, fontsize=20)
plt.ylabel(chart_ylable, fontsize=20)
plt.tick_params(labelsize=20)
plt.savefig(output_image_file_location)
