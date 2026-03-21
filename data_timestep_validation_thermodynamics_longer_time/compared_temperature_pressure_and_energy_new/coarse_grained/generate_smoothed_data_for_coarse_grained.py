import numpy
import pandas
import sys

current_path = sys.path[0]+'/'
original_data_file_name = sys.argv[1]
original_data_file_location = current_path+original_data_file_name
output_smoothed_data_file_name = sys.argv[2]
output_smoothed_data_file_location = current_path+output_smoothed_data_file_name

target_column = -1
if len(sys.argv) > 3:
    target_column = int(sys.argv[3])

original_data = numpy.loadtxt(original_data_file_location)

target_data = original_data[:,-1]

window_size = numpy.max((numpy.min((int(len(target_data)/15),15)),1))
smoothed_data = original_data.copy()
smoothed_data[:,-1][0:len(original_data)] = pandas.Series(target_data).rolling(window_size,min_periods=1).mean().tolist()

numpy.savetxt(output_smoothed_data_file_location, smoothed_data)
