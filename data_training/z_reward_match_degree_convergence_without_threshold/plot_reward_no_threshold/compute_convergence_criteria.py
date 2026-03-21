import numpy
import sys

data_file_name = sys.argv[1]

average_reward_array = numpy.loadtxt(data_file_name)[1:,1]
max_reward_array = numpy.loadtxt(data_file_name)[1:,2]

effective_data_length = len(average_reward_array)

average_reward_convergence_criteria = numpy.zeros(effective_data_length)

max_reward_convergence_criteria = numpy.zeros(effective_data_length)

for i in range(0,effective_data_length):

    average_reward_convergence_criteria[i] = average_reward_array[i]/numpy.max(average_reward_array[0:i+1])
    max_reward_convergence_criteria[i] = max_reward_array[i]/numpy.max(max_reward_array[0:i+1])

print(average_reward_convergence_criteria)
print(max_reward_convergence_criteria)

