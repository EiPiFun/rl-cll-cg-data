import numpy
import pandas
import sys
import matplotlib.pyplot

def smooth_data(original_data):
    smooth_window_size = numpy.max((numpy.min((int(len(original_data)/15),15)),1))
    smoothed_data = pandas.Series(original_data).rolling(smooth_window_size,min_periods=1).mean().tolist()
    return smoothed_data

current_path = sys.path[0]+'/'

reference_displacement_data_file_name = sys.argv[1]
reference_force_data_file_name = sys.argv[2]

force_displacement_data_file_name = sys.argv[3]

try:
    image_file_extension = sys.argv[4]
except:
    image_file_extension = 'png'

reference_displacement_data_file_location = current_path+reference_displacement_data_file_name
reference_force_data_file_location = current_path+reference_force_data_file_name

force_displacement_data_file_location = current_path+force_displacement_data_file_name

output_image_file_location = current_path+'sorted_smoothed_'+force_displacement_data_file_name+'_with_reference.'+image_file_extension

reference_displacement_data = numpy.loadtxt(reference_displacement_data_file_location)
reference_force_data = numpy.loadtxt(reference_force_data_file_location)

force_displacement_data = numpy.loadtxt(force_displacement_data_file_location)

displacement_data = abs(force_displacement_data[:,6]-force_displacement_data[0,6])*0.1
force_data = (force_displacement_data[:,4])*0.06944

reference_x_data = reference_displacement_data[:,-1]*1.0
reference_y_data = reference_force_data[:,-1]*(0.00166)

x_data = displacement_data
y_data = force_data

x_sorted_indices = numpy.argsort(x_data)

x_data = x_data[x_sorted_indices]
y_data = smooth_data(y_data[x_sorted_indices])

plot_box_position = matplotlib.pyplot.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
matplotlib.pyplot.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

matplotlib.pyplot.ylim(-1.0, 10.0)

matplotlib.pyplot.xlabel('Displacement (nm)', fontsize=20)
matplotlib.pyplot.ylabel('Force (nN)', fontsize=20)
#matplotlib.pyplot.xlabel('Displacement (nm)', fontsize=20)
#matplotlib.pyplot.ylabel('Force (nN)', fontsize=20)
matplotlib.pyplot.tick_params(labelsize=20)

matplotlib.pyplot.plot(reference_x_data,reference_y_data, color='dodgerblue')
matplotlib.pyplot.plot(x_data,y_data, color='orangered')

matplotlib.pyplot.legend(('All atom','Coarse grained'), fontsize=20)

matplotlib.pyplot.savefig(output_image_file_location)

