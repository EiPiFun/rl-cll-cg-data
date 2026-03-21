import numpy
import matplotlib.pyplot
import pandas
import sys

'''
def compute_normal_distribution_probability(x, most_probable_value, standard_deviation):
    probability = numpy.exp(-(x-most_probable_value)**2/(2*standard_deviation**2))/(numpy.sqrt(2*numpy.pi)*standard_deviation)
    return(probability)
'''

data_file_location_array = (sys.argv[1],sys.argv[2])
data_label = sys.argv[3]
data_rescale_factor = float(sys.argv[4])
legend_array = (sys.argv[5],sys.argv[6])
total_bin_number_array = (int(sys.argv[7]),int(sys.argv[8]))
output_image_file_name = sys.argv[9]

try:
    image_file_extension = sys.argv[10]
except:
    image_file_extension = 'png'

output_image_file_location = output_image_file_name+'.'+image_file_extension

ylim_high = 0.0

for i in (0,1):

    data_file_location = data_file_location_array[i]

    raw_data = numpy.loadtxt(data_file_location)*data_rescale_factor

    if raw_data.ndim > 1:
      data = raw_data[:,-1]
    else:
        data = raw_data

    average_value = numpy.mean(data)
    standard_error = numpy.std(data)/numpy.sqrt(len(data))

    if i == 1:
        if abs(average_value-numpy.pi) < 0.5*numpy.pi:
            data_deviation = abs(data-numpy.pi)
            data_deviation_within_three_sigma_indices = numpy.argwhere(data_deviation<0.01)
            data = data[data_deviation_within_three_sigma_indices]
        if abs(average_value-0.0) < 0.5*numpy.pi:
            data_deviation = abs(data-0.0)
            data_deviation_within_three_sigma_indices = numpy.argwhere(data_deviation<0.01)
            data = data[data_deviation_within_three_sigma_indices]

    total_bin_number = total_bin_number_array[i]

    y_frequency, x_ticks = numpy.histogram(data, bins=total_bin_number)
    y_density, _ = numpy.histogram(data, bins=total_bin_number, density=True)

    y_relative_frequency = y_frequency/numpy.sum(y_frequency)
    x_data = (x_ticks[0:total_bin_number]+x_ticks[1:total_bin_number+1])*0.5

    x_tick_width = x_ticks[1]-x_ticks[0]

    plot_box_position = matplotlib.pyplot.gca().get_position()
    x_axis_offset = 0.06
    y_axis_offset = 0.04
    matplotlib.pyplot.gca().set_position((plot_box_position.x0+x_axis_offset,plot_box_position.y0+y_axis_offset,plot_box_position.width-x_axis_offset,plot_box_position.height-y_axis_offset))

    ylim_high = numpy.max((ylim_high,2.0*numpy.max(y_relative_frequency)))
    matplotlib.pyplot.ylim(0.0, ylim_high)

    #matplotlib.pyplot.gca().yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))
    #matplotlib.pyplot.gca().yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=0.01))
    #matplotlib.pyplot.hist(data, bins=total_bin_number, density=True)
    #matplotlib.pyplot.bar(x_data, y_relative_frequency, width=x_tick_width, edgecolor='white')
    if i == 0:
        matplotlib.pyplot.plot(x_data, y_relative_frequency,color='black')
    if i == 1:
        matplotlib.pyplot.bar(x_data, y_relative_frequency, width=x_tick_width, color='dodgerblue', edgecolor='white')

    output_results_file_location = '{}.results'.format(data_file_location)
    #output_image_file_location = '{}.png'.format(data_file_location)

    numpy.savetxt(output_results_file_location,(average_value,standard_error))

#matplotlib.pyplot.xticks(x_ticks)
matplotlib.pyplot.legend(legend_array, fontsize=20)
matplotlib.pyplot.tick_params(labelsize=20)
matplotlib.pyplot.xlabel(data_label, fontsize=20)
matplotlib.pyplot.ylabel('Relative frequency', fontsize=20)
matplotlib.pyplot.savefig(output_image_file_location)

