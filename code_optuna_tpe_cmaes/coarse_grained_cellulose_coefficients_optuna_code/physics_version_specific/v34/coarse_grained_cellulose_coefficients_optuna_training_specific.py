code_version = 'v33'
indepedent_variable_total_number = 12

def generate_interaction_coefficients(coefficient_precision_format,unscaled_parameter_array):

    bc_1 =  64.06 #  65.00
    bc_2 =  82.42 #  83.63
    bc_3 = 112.30 # 113.95
    ac_1 =  30.97 #  30.00
    ac_2 =  38.79 #  37.57
    ac_3 =  30.52 #  29.56
    ac_4 =  27.28 #  26.43
    ac_5 =  25.97 #  25.16
    ac_6 =  22.42 #  21.72
    ic_1 = 0.1702 #   0.20
    ic_2 = 0.1555 #   0.17
    ic_3 = 0.1698 #   0.19
    pc_1_2_1_hb = float(coefficient_precision_format % (0.10*unscaled_parameter_array[0]+1.50))
    pc_1_2_2_hb = float(coefficient_precision_format % (0.3*unscaled_parameter_array[1]+6.0))
    pc_1_3_1_hb = float(coefficient_precision_format % (0.10*unscaled_parameter_array[0]+1.50))
    pc_1_3_2_hb = float(coefficient_precision_format % (0.3*unscaled_parameter_array[1]+6.0))
    pc_1_1_1 = float(coefficient_precision_format % (0.50*unscaled_parameter_array[2]+1.00))
    pc_1_1_2 = float(coefficient_precision_format % (0.561*unscaled_parameter_array[3]+5.1))
    pc_1_2_1 = float(coefficient_precision_format % (0.50*unscaled_parameter_array[4]+1.00))
    pc_1_2_2 = float(coefficient_precision_format % (0.462*unscaled_parameter_array[5]+4.2))
    pc_1_3_1 = float(coefficient_precision_format % (0.50*unscaled_parameter_array[6]+1.00))
    pc_1_3_2 = float(coefficient_precision_format % (0.451*unscaled_parameter_array[7]+4.1))
    pc_2_2_1 = float(coefficient_precision_format % (0.50*unscaled_parameter_array[8]+1.00))
    pc_2_2_2 = float(coefficient_precision_format % (0.561*unscaled_parameter_array[3]+5.1))
    pc_2_3_1 = float(coefficient_precision_format % (0.50*unscaled_parameter_array[9]+1.00))
    pc_2_3_2 = float(coefficient_precision_format % (0.407*unscaled_parameter_array[10]+3.7))
    pc_3_3_1 = float(coefficient_precision_format % (0.50*unscaled_parameter_array[11]+1.00))
    pc_3_3_2 = float(coefficient_precision_format % (0.561*unscaled_parameter_array[3]+5.1))

    interaction_coefficients = (bc_1,bc_2,bc_3,ac_1,ac_2,ac_3,ac_4,ac_5,ac_6,ic_1,ic_2,ic_3,pc_1_2_1_hb,pc_1_2_2_hb,pc_1_3_1_hb,pc_1_3_2_hb,pc_1_1_1,pc_1_1_2,pc_1_2_1,pc_1_2_2,pc_1_3_1,pc_1_3_2,pc_2_2_1,pc_2_2_2,pc_2_3_1,pc_2_3_2,pc_3_3_1,pc_3_3_2)

    return interaction_coefficients

