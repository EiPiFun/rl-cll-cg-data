import numpy
import sys

data_file_name = sys.argv[1]

data = numpy.loadtxt(data_file_name)

data_length = int(data.shape[0]/2)

ste_coefficient = 1.0/numpy.sqrt(data_length)

output_data_file_name_list = (('vertical_max_stress.txt','horizontal_max_stress.txt','slant_max_stress.txt'),
                              ('vertical_max_strain_energy.txt','horizontal_max_strain_energy.txt','slant_max_strain_energy.txt'))

print(data_length)

for i in range(0,2):
    for j in range(0,3):

        target_data = numpy.zeros(data_length)

        for k in range(0,data_length):
            target_data[k] = data[2*k+i][j]

        numpy.savetxt(output_data_file_name_list[i][j], target_data)

        print(numpy.mean(target_data),numpy.std(target_data)*ste_coefficient)

