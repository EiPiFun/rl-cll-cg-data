import numpy
import pandas
import sys
import matplotlib.pyplot

current_path = sys.path[0]+'/'

strain_column_dict = {'x':1,'y':2,'z':3}
stress_column_dict = {'x':4,'y':5,'z':6}

computation_index_dict = {'vertical':'5','horizontal':'6','slant':'7'}

strain_stress_data_file_directory = sys.argv[1]+'/'
load_direction = sys.argv[2]
model_direction = sys.argv[3]

output_strain_collection_file_location = current_path+model_direction+'_strain_collection.txt'
output_stress_collection_file_location = current_path+model_direction+'_stress_collection.txt'

strain_column = strain_column_dict[load_direction]
stress_column = stress_column_dict[load_direction]

computation_index = computation_index_dict[model_direction]

strain_collection = []
stress_collection = []

for i in range(0,100):

    temp_strain_stress_data_file_location = strain_stress_data_file_directory+'debug-'+str(i)+'/'+'physics_computation_'+computation_index+'/'+'results/box_size-pressure_stretch'

    temp_box_size_pressure_data = numpy.loadtxt(temp_strain_stress_data_file_location)
    temp_strain_data = abs(temp_box_size_pressure_data[:,strain_column]/temp_box_size_pressure_data[0,strain_column]-1.0)
    temp_stress_data = temp_box_size_pressure_data[:,stress_column]

    strain_collection.append(temp_strain_data)
    stress_collection.append(temp_stress_data)

numpy.savetxt(output_strain_collection_file_location,strain_collection)
numpy.savetxt(output_stress_collection_file_location,stress_collection)



