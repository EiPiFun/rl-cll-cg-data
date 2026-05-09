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
first_scale_factor_x = float(sys.argv[6])
first_scale_factor_y = float(sys.argv[7])
second_scale_factor_x = float(sys.argv[8])
second_scale_factor_y = float(sys.argv[9])
legend_array = (sys.argv[10],sys.argv[11])
first_plot_color = sys.argv[12]
second_plot_color = sys.argv[13]
output_image_file_name = sys.argv[14]

try:
    image_file_extension = sys.argv[15]
except:
    image_file_extension = 'png'

output_image_file_location = output_image_file_name+'.'+image_file_extension

raw_first_data = numpy.loadtxt(first_data_file_location)
raw_second_data = numpy.loadtxt(second_data_file_location)

first_data_x = raw_first_data[:,0]*first_scale_factor_x
first_data_y = raw_first_data[:,1]*first_scale_factor_y

second_data_x = raw_second_data[:,0]*second_scale_factor_x
second_data_y = raw_second_data[:,1]*second_scale_factor_y

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plot_limit_max = numpy.max((numpy.max(first_data_y),numpy.max(second_data_y)))
plot_limit_min = numpy.min((0.0,numpy.min((numpy.min(first_data_y),numpy.min(second_data_y)))))
plt.ylim(plot_limit_min-0.1*plot_limit_max,1.6*plot_limit_max)

plt.plot(first_data_x,first_data_y, color=first_plot_color)
plt.plot(second_data_x,second_data_y, color=second_plot_color)

plt.title(chart_title, fontsize=20)
plt.legend(legend_array, fontsize=20)
plt.xlabel(chart_xlable, fontsize=20)
plt.ylabel(chart_ylable, fontsize=20)
plt.tick_params(labelsize=20)
plt.savefig(output_image_file_location)
