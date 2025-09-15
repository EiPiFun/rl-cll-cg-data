import numpy
import sys
import matplotlib.pyplot

current_path = sys.path[0]+'/'

try:
    image_file_extension = sys.argv[1]
except:
    image_file_extension = 'png'

strain_column_dict = {'x':1,'y':2,'z':3}

reference_strain_data_file_name = sys.argv[1]
reference_direction_angle_data_file_name = sys.argv[2]

box_size_pressure_data_file_name = sys.argv[3]
direction = sys.argv[4]

angle_data_file_name = sys.argv[5]

try:
    image_file_extension = sys.argv[6]
except:
    image_file_extension = 'png'

reference_strain_data_file_location = current_path+reference_strain_data_file_name
reference_direction_angle_data_file_location = current_path+reference_direction_angle_data_file_name

box_size_pressure_data_file_location = current_path+box_size_pressure_data_file_name
angle_data_file_location = current_path+angle_data_file_name

output_image_file_location = angle_data_file_location+'_with_reference.'+image_file_extension

reference_strain_data = numpy.loadtxt(reference_strain_data_file_location)[:,-1]
reference_direction_angle_data = numpy.loadtxt(reference_direction_angle_data_file_location)[:,-1]

box_size_pressure_data = numpy.loadtxt(box_size_pressure_data_file_location)
raw_angle_data = numpy.loadtxt(angle_data_file_location)

strain_column = strain_column_dict[direction]

strain_data = abs(box_size_pressure_data[:,strain_column]/box_size_pressure_data[0,strain_column]-1.0)

angle_data = raw_angle_data[:,-1]

reference_x_data = reference_strain_data
reference_y_data = reference_direction_angle_data

x_data = strain_data
y_data = angle_data

plot_box_position = matplotlib.pyplot.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
matplotlib.pyplot.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

matplotlib.pyplot.xlim(-0.1, 1.2)

matplotlib.pyplot.plot(reference_x_data,reference_y_data,color='dodgerblue')
matplotlib.pyplot.plot(x_data,y_data,color='orangered')

matplotlib.pyplot.legend(('All atom','Coarse grained'), fontsize=20)
matplotlib.pyplot.tick_params(labelsize=20)
matplotlib.pyplot.xlabel('Strain', fontsize=20)
matplotlib.pyplot.ylabel('Direction angle', fontsize=20)
matplotlib.pyplot.savefig(output_image_file_location)

