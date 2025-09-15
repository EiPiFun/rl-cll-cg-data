import numpy
import sys

current_path = sys.path[0]+'/'
centroid_of_mass_vector_data_file_name = sys.argv[1]
centroid_of_mass_vector_data_file_location = current_path+centroid_of_mass_vector_data_file_name
output_displacement_data_file_name = sys.argv[2]
output_displacement_data_file_location = current_path+output_displacement_data_file_name

centroid_of_mass_vector_data = numpy.loadtxt(centroid_of_mass_vector_data_file_location)
output_displacement_data = centroid_of_mass_vector_data.copy()
output_displacement_data[:,1] = abs(centroid_of_mass_vector_data[:,1]-centroid_of_mass_vector_data[0,1])

numpy.savetxt(output_displacement_data_file_location, output_displacement_data)
