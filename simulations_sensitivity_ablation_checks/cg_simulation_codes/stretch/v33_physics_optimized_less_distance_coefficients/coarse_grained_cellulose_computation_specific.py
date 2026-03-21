import numpy

relative_hb_r_in = 1.00
relative_hb_r_cut = 1.30
relative_lj_r_in = 2.00
relative_lj_r_cut = 2.10

#estimated_interaction_coefficients = (65.00,83.63,113.95,30.00,37.57,29.56,26.43,25.16,21.72,0.20,0.18,0.20,1.4,6.0,1.4,6.0,0.8,5.1,0.8,4.1,0.8,4.0,0.8,5.1,0.8,3.7,0.8,5.1)

estimated_interaction_coefficients = (64.06,82.42,112.3,30.97,38.79,30.52,27.28,25.97,22.42,0.1702,0.1555,0.1698,1.404,4.814,1.404,4.814,0.9031,4.081,0.9031,3.361,0.9031,3.281,0.9031,4.081,0.5031,3.266,0.9031,4.081)

interaction_coefficients_header = 'bc_1,bc_2,bc_3,ac_1,ac_2,ac_3,ac_4,ac_5,ac_6,ic_1,ic_2,ic_3,pc_1_2_1_hb,pc_1_2_2_hb,pc_1_3_1_hb,pc_1_3_2_hb,pc_1_1_1,pc_1_1_2,pc_1_2_1,pc_1_2_2,pc_1_3_1,pc_1_3_2,pc_2_2_1,pc_2_2_2,pc_2_3_1,pc_2_3_2,pc_3_3_1,pc_3_3_2'

coarse_grained_cellulose_coefficients_pool_header = 'step_count,'+interaction_coefficients_header

class CoarseGrainedCelluloseComputationSpecific():

    def __init__(self,working_directory):

        self.physics_computation_1_inputs_directory = working_directory+'physics_computation_1/inputs/'
        self.physics_computation_2_inputs_directory = working_directory+'physics_computation_2/inputs/'
        self.physics_computation_3_inputs_directory = working_directory+'physics_computation_3/inputs/'
        self.physics_computation_4_inputs_directory = working_directory+'physics_computation_4/inputs/'
        self.physics_computation_5_inputs_directory = working_directory+'physics_computation_5/inputs/'
        self.physics_computation_6_inputs_directory = working_directory+'physics_computation_6/inputs/'
        self.physics_computation_7_inputs_directory = working_directory+'physics_computation_7/inputs/'

        self.physics_computation_1_in_file_location = self.physics_computation_1_inputs_directory+'coarse_grained_cellulose.in'
        self.physics_computation_2_in_file_location = self.physics_computation_2_inputs_directory+'coarse_grained_cellulose.in'
        self.physics_computation_3_in_file_location = self.physics_computation_3_inputs_directory+'coarse_grained_cellulose.in'
        self.physics_computation_4_in_file_location = self.physics_computation_4_inputs_directory+'coarse_grained_cellulose.in'
        self.physics_computation_5_in_file_location = self.physics_computation_5_inputs_directory+'coarse_grained_cellulose.in'
        self.physics_computation_6_in_file_location = self.physics_computation_6_inputs_directory+'coarse_grained_cellulose.in'
        self.physics_computation_7_in_file_location = self.physics_computation_7_inputs_directory+'coarse_grained_cellulose.in'

        self.interaction_coefficients_location = working_directory+'interaction_coefficients.txt'

    def in_file_generation(self,interaction_coefficients):

        bc_1,bc_2,bc_3,ac_1,ac_2,ac_3,ac_4,ac_5,ac_6,ic_1,ic_2,ic_3,pc_1_2_1_hb,pc_1_2_2_hb,pc_1_3_1_hb,pc_1_3_2_hb,pc_1_1_1,pc_1_1_2,pc_1_2_1,pc_1_2_2,pc_1_3_1,pc_1_3_2,pc_2_2_1,pc_2_2_2,pc_2_3_1,pc_2_3_2,pc_3_3_1,pc_3_3_2 = interaction_coefficients

        inputs_directories = (self.physics_computation_1_inputs_directory,self.physics_computation_2_inputs_directory,self.physics_computation_3_inputs_directory,self.physics_computation_4_inputs_directory,self.physics_computation_5_inputs_directory,self.physics_computation_6_inputs_directory,self.physics_computation_7_inputs_directory)
        in_file_locations = (self.physics_computation_1_in_file_location,self.physics_computation_2_in_file_location,self.physics_computation_3_in_file_location,self.physics_computation_4_in_file_location,self.physics_computation_5_in_file_location,self.physics_computation_6_in_file_location,self.physics_computation_7_in_file_location)

        for i in (0,1,2,3,4,5,6):

            constant_head = open(inputs_directories[i]+'in_file_constant_head.txt').read()
            constant_tail = open(inputs_directories[i]+'in_file_constant_tail.txt').read()

            coeff_information = '\n\
bond_coeff 1 {0} 5.270 # CL1-CL1\n\
bond_coeff 2 {1} 2.493 # CL2-CL1\n\
bond_coeff 3 {2} 2.066 # CL3-CL1\n\
\n\
angle_coeff 1 {3} 163.5 # CL1-CL1-CL1\n\
angle_coeff 2 {4}  74.2 # CL2-CL1-CL1_1\n\
angle_coeff 3 {5}  93.2 # CL3-CL1-CL1_1\n\
angle_coeff 4 {6}  90.0 # CL2-CL1-CL1_2\n\
angle_coeff 5 {7} 102.0 # CL3-CL1-CL1_2\n\
angle_coeff 6 {8} 166.3 # CL2-CL1-CL3\n\
\n\
improper_coeff 1 {9} 178.0 # CL1-CL1-CL1-CL1\n\
improper_coeff 2 {10}   2.3 # CL2-CL1-CL1-CL3\n\
improper_coeff 3 {11}   2.9 # CL3-CL1-CL1-CL2\n\
\n\
pair_coeff 1 2 hbond/dreiding/lj/angleoffset 3 i {12} {13} 4 {14} {15} 135.0 173.1 # CL1-CL2\n\
pair_coeff 1 3 hbond/dreiding/lj/angleoffset 2 i {16} {17} 4 {18} {19} 135.0 173.1 # CL1-CL3\n\
pair_coeff 1 1 lj/smooth {20} {21} {22} {23}                     # CL1-CL1\n\
pair_coeff 1 2 lj/smooth {24} {25} {26} {27}                     # CL1-CL2\n\
pair_coeff 1 3 lj/smooth {28} {29} {30} {31}                     # CL1-CL3\n\
pair_coeff 2 2 lj/smooth {32} {33} {34} {35}                     # CL2-CL2\n\
pair_coeff 2 3 lj/smooth {36} {37} {38} {39}                     # CL2-CL3\n\
pair_coeff 3 3 lj/smooth {40} {41} {42} {43}                     # CL3-CL3\n\
\n'.format(bc_1,bc_2,bc_3,ac_1,ac_2,ac_3,ac_4,ac_5,ac_6,ic_1,ic_2,ic_3,pc_1_2_1_hb,pc_1_2_2_hb,relative_hb_r_in*pc_1_2_2_hb,relative_hb_r_cut*pc_1_2_2_hb,pc_1_3_1_hb,pc_1_3_2_hb,relative_hb_r_in*pc_1_3_2_hb,relative_hb_r_cut*pc_1_3_2_hb,pc_1_1_1,pc_1_1_2,relative_lj_r_in*pc_1_1_2,relative_lj_r_cut*pc_1_1_2,pc_1_2_1,pc_1_2_2,relative_lj_r_in*pc_1_2_2,relative_lj_r_cut*pc_1_2_2,pc_1_3_1,pc_1_3_2,relative_lj_r_in*pc_1_3_2,relative_lj_r_cut*pc_1_3_2,pc_2_2_1,pc_2_2_2,relative_lj_r_in*pc_2_2_2,relative_lj_r_cut*pc_2_2_2,pc_2_3_1,pc_2_3_2,relative_lj_r_in*pc_2_3_2,relative_lj_r_cut*pc_2_3_2,pc_3_3_1,pc_3_3_2,relative_lj_r_in*pc_3_3_2,relative_lj_r_cut*pc_3_3_2)

            in_file_content = constant_head+coeff_information+constant_tail
            in_file = open(in_file_locations[i],'w')
            in_file.write(in_file_content)
            in_file.close()

        numpy.savetxt(self.interaction_coefficients_location,interaction_coefficients,header=interaction_coefficients_header,fmt='%.6f',delimiter=',')

