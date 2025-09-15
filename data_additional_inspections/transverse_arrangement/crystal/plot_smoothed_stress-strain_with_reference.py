import numpy
import pandas
import sys
import matplotlib.pyplot

def smooth_data(original_data):
    smooth_window_size = numpy.max((numpy.min((int(len(original_data)/15),15)),1))
    smoothed_data = pandas.Series(original_data).rolling(smooth_window_size,min_periods=1).mean().tolist()
    return smoothed_data

current_path = sys.path[0]+'/'

strain_column_dict = {'x':1,'y':2,'z':3}
stress_column_dict = {'x':4,'y':5,'z':6}

reference_strain_data_file_name = sys.argv[1]
reference_stress_data_file_name = sys.argv[2]

strain_stress_data_file_name = sys.argv[3]
direction = sys.argv[4]

try:
    image_file_extension = sys.argv[5]
except:
    image_file_extension = 'png'

reference_strain_data_file_location = current_path+reference_strain_data_file_name
reference_stress_data_file_location = current_path+reference_stress_data_file_name

strain_stress_data_file_location = current_path+strain_stress_data_file_name

output_image_file_location = current_path+'smoothed_'+strain_stress_data_file_name+'_with_reference.'+image_file_extension

reference_strain_data = numpy.loadtxt(reference_strain_data_file_location)[:,-1]
reference_stress_data = numpy.loadtxt(reference_stress_data_file_location)[:,-1]

raw_strain_stress_data = numpy.loadtxt(strain_stress_data_file_location)

strain_column = strain_column_dict[direction]
stress_column = stress_column_dict[direction]

strain_data = abs(raw_strain_stress_data[:,strain_column]/raw_strain_stress_data[0,strain_column]-1.0)
stress_data = smooth_data(-0.0001*(raw_strain_stress_data[:,stress_column]))

reference_x_data = reference_strain_data*1.0
reference_y_data = reference_stress_data*(-0.0001)

x_data = strain_data
y_data = stress_data

plot_box_position = matplotlib.pyplot.gca().get_position()
x_axis_offset = 0.06
y_axis_offset = 0.04
matplotlib.pyplot.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

matplotlib.pyplot.xlim(-0.05, 0.7)
matplotlib.pyplot.ylim(-0.05, 0.8)

#matplotlib.pyplot.gca().xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=0.04))
matplotlib.pyplot.plot(reference_x_data,reference_y_data,color='dodgerblue')
matplotlib.pyplot.plot(x_data,y_data,color='orangered')

matplotlib.pyplot.legend(('All atom','Coarse grained'), fontsize=20)
matplotlib.pyplot.tick_params(labelsize=20)
matplotlib.pyplot.xlabel('Strain', fontsize=20)
matplotlib.pyplot.ylabel('Stress (GPa)', fontsize=20)
matplotlib.pyplot.savefig(output_image_file_location)

