import numpy
import sys

xvg_file_name = sys.argv[1]
skip_row_number = int(sys.argv[2])
simplified_txt_file_name = xvg_file_name+'.txt'

xvg_data = numpy.loadtxt(xvg_file_name, skiprows=skip_row_number)
numpy.savetxt(simplified_txt_file_name, xvg_data)
