code_version = 'v31'
indepedent_variable_total_number = 3

def generate_interaction_coefficients(coefficient_precision_format,unscaled_parameter_array):

    bc_1 = float(coefficient_precision_format % (10.0*unscaled_parameter_array[0]+70.0))
    bc_2 = float(coefficient_precision_format % (1.2866*bc_1))
    bc_3 = float(coefficient_precision_format % (1.7531*bc_1))
    ac_1 = float(coefficient_precision_format % (5.0*unscaled_parameter_array[1]+30.0))
    ac_2 = float(coefficient_precision_format % (1.2524*ac_1))
    ac_3 = float(coefficient_precision_format % (0.9854*ac_1))
    ac_4 = float(coefficient_precision_format % (0.8809*ac_1))
    ac_5 = float(coefficient_precision_format % (0.8386*ac_1))
    ac_6 = float(coefficient_precision_format % (0.7240*ac_1))
    ic_1 = float(coefficient_precision_format % (0.35*unscaled_parameter_array[2]+0.50))
    ic_2 = float(coefficient_precision_format % (0.9139*ic_1))
    ic_3 = float(coefficient_precision_format % (0.9979*ic_1))

    interaction_coefficients = (bc_1,bc_2,bc_3,ac_1,ac_2,ac_3,ac_4,ac_5,ac_6,ic_1,ic_2,ic_3)

    return interaction_coefficients

