import numpy
import sys

current_path = sys.path[0]+'/'

cellulose_box_size_pressure_data_file_name = sys.argv[1]

cellulose_box_size_pressure_data_file_location = current_path+cellulose_box_size_pressure_data_file_name

box_size_pressure_data = numpy.loadtxt(cellulose_box_size_pressure_data_file_location)
strain_data = abs(box_size_pressure_data[:,3]/box_size_pressure_data[0,3]-1.0)
stress_data = -0.1*box_size_pressure_data[:,6]
fitted_elastic_modulus = numpy.dot(strain_data,stress_data)/numpy.dot(strain_data,strain_data)

print(fitted_elastic_modulus)
