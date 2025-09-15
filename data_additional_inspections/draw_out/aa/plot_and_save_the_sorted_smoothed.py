import matplotlib.pyplot as plt
import numpy
import pandas
import sys

current_path = sys.path[0]+'/'
x_data_file_name = sys.argv[1]
x_data_file_location = current_path+x_data_file_name
y_data_file_name = sys.argv[2]
y_data_file_location = current_path+y_data_file_name
chart_title = sys.argv[3]
chart_xlable = sys.argv[4]
chart_ylable = sys.argv[5]
scale_factor_x = float(sys.argv[6])
scale_factor_y = float(sys.argv[7])

try:
    plot_color = sys.argv[8]
except:
    plot_color = 'black'

try:
    image_file_extension = sys.argv[9]
except:
    image_file_extension = 'png'

output_sorted_x_data_file_location = current_path+'sorted_'+x_data_file_name
output_sorted_y_data_file_location = current_path+'sorted_'+y_data_file_name
output_sorted_smoothed_y_data_file_location = current_path+'sorted_smoothed_'+y_data_file_name
output_image_file_location = current_path+'sorted_smoothed_'+y_data_file_name+'-'+x_data_file_name+'.'+image_file_extension

x_data = numpy.loadtxt(x_data_file_location)
y_data = numpy.loadtxt(y_data_file_location)

if x_data_file_location == y_data_file_location:
    x = x_data[:,0]
else:
    x = x_data[:,-1]

y = y_data[:,-1]

x_sorted_indices = numpy.argsort(x)

x = x[x_sorted_indices]
y = y[x_sorted_indices]

output_x = x_data.copy()
output_x[:,-1] = x
numpy.savetxt(output_sorted_x_data_file_location, output_x)
output_y = y_data.copy()
output_y[:,-1] = y
numpy.savetxt(output_sorted_y_data_file_location, output_y)

window_size = numpy.max((numpy.min((int(len(x_data)/30),30)),1))
ys = y.copy()
ys[0:len(y)] = pandas.Series(y).rolling(window_size,min_periods=1).mean().tolist()

output_ys = y_data.copy()
output_ys[:,-1] = ys
numpy.savetxt(output_sorted_smoothed_y_data_file_location, output_ys)

x = x*scale_factor_x
y = y*scale_factor_y
ys = ys*scale_factor_y

plot_box_position = plt.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
plt.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

plt.xlim(-0.1, 5.0)
plt.ylim(-1.0, 10.0)

#plt.scatter(x,y)
plt.plot(x,ys,color=plot_color)

plt.title(chart_title, fontsize=20)
plt.xlabel(chart_xlable, fontsize=20)
plt.ylabel(chart_ylable, fontsize=20)
plt.tick_params(labelsize=20)
plt.savefig(output_image_file_location)
