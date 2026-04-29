import numpy
import scipy
import sys

potential_file_name = sys.argv[1]

total_number_of_knot = int(sys.argv[2])

output_parameter_file_name = sys.argv[3]

raw_potential_data = numpy.loadtxt(potential_file_name, usecols=(0,1), skiprows=4)

potential_distance_array = raw_potential_data[:,0]
potential_data_array = raw_potential_data[:,1]

potential_distance_extended_array = numpy.linspace(numpy.min(potential_distance_array),numpy.max(potential_distance_array),total_number_of_knot)[2:-2]

cubic_spline = scipy.interpolate.LSQUnivariateSpline(potential_distance_array, potential_data_array, potential_distance_extended_array, k=3)

parameter_array = cubic_spline.get_coeffs()

parameter_table = numpy.zeros((total_number_of_knot,2))

parameter_table[:,0] = range(total_number_of_knot)
parameter_table[:,1] = parameter_array

'''
with open(output_parameter_file_name, 'w') as f:
    for i, c in enumerate(parameters):
        # Format: Index  Value  Flag(i for active)
        f.write(f"{i:<5} {c:>12.6f}\n")
'''

#print(parameters)

numpy.savetxt(output_parameter_file_name, parameter_table, fmt=('%d','%.6f'))


