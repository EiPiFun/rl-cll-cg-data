# Reference
# https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy
import sys

current_path = sys.path[0]+'/'
x_data_file_name = sys.argv[1]
x_data_file_location = current_path+x_data_file_name
y_data_file_name = sys.argv[2]
y_data_file_location = current_path+y_data_file_name
chart_title = sys.argv[3]
chart_xlable = sys.argv[4]
chart_ylable = sys.argv[5]
scale_factor_x = float(sys.argv[6])
scale_factor_y = float(sys.argv[7])

try:
    plot_color = sys.argv[8]
except:
    plot_color = 'black'

try:
    image_file_extension = sys.argv[9]
except:
    image_file_extension = 'png'

output_image_file_location = current_path+y_data_file_name+'-'+x_data_file_name+'.'+image_file_extension

x_data = numpy.loadtxt(x_data_file_location)
y_data = numpy.loadtxt(y_data_file_location)

x_data = x_data*scale_factor_x
y_data = y_data*scale_factor_y

if x_data.ndim > 1:

    total_data_number = x_data.shape[0]
    max_y_array = numpy.zeros(total_data_number)

    fig = plt.figure()
    gs = fig.add_gridspec(1, 3, hspace=0.3, wspace=0.3)
    ax1 = fig.add_subplot(gs[0,0:2])
    ax2 = fig.add_subplot(gs[0,2:3])
    ax1.set_xlim(-0.1, 1.2)
    ax1.set_ylim(-0.2, 1.7)
    ax2.sharey(ax1)
    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position('right')
    for ax in fig.get_axes():
        ax.label_outer()
    
    ax1_box_position = ax1.get_position()
    x_axis_offset = 0.06
    y_axis_offset = 0.04
    ax1.set_position((ax1_box_position.x0+x_axis_offset,ax1_box_position.y0+y_axis_offset,ax1_box_position.width-x_axis_offset,ax1_box_position.height-y_axis_offset))

    ax2_box_position = ax2.get_position()
    x_axis_offset = 0.06
    y_axis_offset = 0.04
    ax2.set_position((ax2_box_position.x0,ax2_box_position.y0+y_axis_offset,ax2_box_position.width-x_axis_offset,ax2_box_position.height-y_axis_offset))

    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    ax2.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

    for i in range(0,total_data_number):

        temp_x_data = x_data[i,:]
        temp_y_data = y_data[i,:]
        ax1.plot(temp_x_data, temp_y_data, color=plot_color, alpha=0.1)
        max_y_array[i] = numpy.max(temp_y_data)
    
    #base_interval = 0.1*int(numpy.max(max_y_array)+1)
    base_interval = 0.3
    ax1.yaxis.set_major_locator(plt.MultipleLocator(base=base_interval))
    
    total_bin_number = 6

    y_frequency, xticks = numpy.histogram(max_y_array, bins=total_bin_number)
    y_density, _ = numpy.histogram(max_y_array, bins=total_bin_number, density=True)
    y_relative_frequency = y_frequency/numpy.sum(y_frequency)

    x_tick_width = xticks[1]-xticks[0]
    x_ticks = (xticks[0:total_bin_number]+xticks[1:total_bin_number+1])*0.5

    ax2.barh(x_ticks, width=y_relative_frequency, height=x_tick_width, color=plot_color, alpha=0.8)
    
    ax1.set_xlabel(chart_xlable, fontsize=20)
    ax1.set_ylabel(chart_ylable, fontsize=20)
    ax1.tick_params(labelsize=20)
    ax2.set_xlabel('Frequency', fontsize=20)
    ax2.set_ylabel('Max '+chart_ylable, fontsize=20)#, rotation=270)
    ax2.tick_params(labelsize=20)


else:
    plt.plot(x_data,y_data)

plt.title(chart_title, fontsize=20)
plt.savefig(output_image_file_location)


