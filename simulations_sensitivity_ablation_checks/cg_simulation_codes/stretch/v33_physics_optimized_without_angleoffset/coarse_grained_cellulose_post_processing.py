import numpy
import os
import pandas
import scipy
import subprocess

default_fitted_elastic_modulus = 0.0

# Only consider one periodic chain for axial stretch when training

#reference_elastic_modulus_with_nonbonded = 134670.0
reference_elastic_modulus_with_nonbonded = 2600.0
reference_elastic_modulus_without_nonbonded = 2600.0
elastic_modulus_difference_threshold = 50
default_elastic_modulus_match_degree = -1.0

default_average_bond_length = 0.0
default_average_persistence_length = 0.0
default_average_end_to_end_distance = 0.0

# Persistence length is similar when coupled with nonbonded interactions

reference_persistence_length_with_nonbonded = (9.755+9.815+9.716)/3.0
reference_persistence_length_without_nonbonded = (9.755+9.815+9.716)/3.0
persistence_length_difference_threshold = 4.0
default_persistence_length_match_degree = -1.0

reference_physics_computation_2_end_to_end_distance =  4.523
reference_physics_computation_3_end_to_end_distance =  9.355
reference_physics_computation_4_end_to_end_distance = 13.536
end_to_end_distance_difference_threshold = 0.40
default_end_to_end_distance_match_degree = -1.0

average_rmsd_threshold = 3.0
average_box_volume_change_threshold = 0.15
reference_physics_computation_5_relaxation_average_direction_angle = 1.57
reference_physics_computation_6_relaxation_average_direction_angle = 0.00
reference_physics_computation_7_relaxation_average_direction_angle = 2.29
relaxation_average_direction_angle_difference_threshold = 0.15
default_system_stable_enough_switch = -1.0

reference_physics_computation_5_fracture_average_direction_angle = 1.57
reference_physics_computation_6_fracture_average_direction_angle = 0.00
reference_physics_computation_7_fracture_average_direction_angle = 1.92
fracture_average_direction_angle_difference_threshold = 0.15
default_fracture_average_direction_angle_match_degree = 0.0

reference_physics_computation_5_fracture_rotation_angle = reference_physics_computation_5_relaxation_average_direction_angle-reference_physics_computation_5_fracture_average_direction_angle
reference_physics_computation_6_fracture_rotation_angle = reference_physics_computation_6_relaxation_average_direction_angle-reference_physics_computation_6_fracture_average_direction_angle
reference_physics_computation_7_fracture_rotation_angle = reference_physics_computation_7_relaxation_average_direction_angle-reference_physics_computation_7_fracture_average_direction_angle
fracture_rotation_angle_difference_threshold = 0.15
default_fracture_rotation_angle_match_degree = 0.0

reference_physics_computation_5_max_stress = 1224.00
reference_physics_computation_5_max_strain_energy = 110.98
reference_physics_computation_5_equivalent_strain = reference_physics_computation_5_max_strain_energy/reference_physics_computation_5_max_stress
reference_physics_computation_6_max_stress = 638.20
reference_physics_computation_6_max_strain_energy = 77.91
reference_physics_computation_6_equivalent_strain = reference_physics_computation_6_max_strain_energy/reference_physics_computation_6_max_stress
reference_physics_computation_7_max_stress = 467.04
reference_physics_computation_7_max_strain_energy = 190.07
reference_physics_computation_7_equivalent_strain = reference_physics_computation_7_max_strain_energy/reference_physics_computation_7_max_stress

max_stress_match_degree_threshold = 0.67
max_strain_energy_match_degree_threshold = 0.67

default_max_stress = 0.0
default_max_stress_match_degree = 0.0
default_max_strain_energy = 0.0
default_max_strain_energy_match_degree = 0.0
default_equivalent_strain = 0.0
default_equivalent_strain_match_degree = 0.0

average_orthogonal_direction_box_size_change_threshold = 0.1

def smooth_data(original_data):
    smooth_window_size = numpy.max((numpy.min((int(len(original_data)/15),15)),1))
    smoothed_data = pandas.Series(original_data).rolling(smooth_window_size,min_periods=1).mean().tolist()
    return smoothed_data

def compute_linear_match_degree(value,reference_value):
    match_degree = 1.0/(abs(value/reference_value-1.0)+1.0)
    return match_degree

def compute_square_match_degree(value,reference_value):
    match_degree = 1.0/(numpy.square(value/reference_value-1.0)+1.0)
    return match_degree

def compute_square_root_match_degree(value,reference_value):
    match_degree = 1.0/(numpy.sqrt(abs(value/reference_value-1.0))+1.0)
    return match_degree

def compute_log_match_degree(value,reference_value):
    match_degree = 1.0/(abs(numpy.log(value/reference_value))+1.0)
    return match_degree

def compute_persistence_length_match_degree(persistence_length_data,average_bond_length,average_persistence_length,reference_persistence_length):
    fit_x = persistence_length_data[:,0]
    fit_error = abs(numpy.exp(-average_bond_length/average_persistence_length*fit_x)-persistence_length_data[:,1])
    fit_error_integral = scipy.integrate.simpson(fit_error,fit_x)
    fit_quality = 1.0/(numpy.log(fit_error_integral+1.0)+1.0)
    match_degree = numpy.sqrt(compute_linear_match_degree(average_persistence_length,reference_persistence_length)*fit_quality)
    return match_degree

class CoarseGrainedCellulosePostProcessing():

    def __init__(self,working_directory):

        self.working_directory = working_directory

        self.physics_computation_1_inputs_directory = working_directory+'physics_computation_1/inputs/'
        self.physics_computation_1_results_directory = working_directory+'physics_computation_1/results/'
        self.physics_computation_2_inputs_directory = working_directory+'physics_computation_2/inputs/'
        self.physics_computation_2_results_directory = working_directory+'physics_computation_2/results/'
        self.physics_computation_3_inputs_directory = working_directory+'physics_computation_3/inputs/'
        self.physics_computation_3_results_directory = working_directory+'physics_computation_3/results/'
        self.physics_computation_4_inputs_directory = working_directory+'physics_computation_4/inputs/'
        self.physics_computation_4_results_directory = working_directory+'physics_computation_4/results/'
        self.physics_computation_5_inputs_directory = working_directory+'physics_computation_5/inputs/'
        self.physics_computation_5_results_directory = working_directory+'physics_computation_5/results/'
        self.physics_computation_6_inputs_directory = working_directory+'physics_computation_6/inputs/'
        self.physics_computation_6_results_directory = working_directory+'physics_computation_6/results/'
        self.physics_computation_7_inputs_directory = working_directory+'physics_computation_7/inputs/'
        self.physics_computation_7_results_directory = working_directory+'physics_computation_7/results/'

    def post_processing_axial_stretch(self,results_directory,reference_elastic_modulus):
        
        try:

            cellulose_box_size_pressure_data_file_location = results_directory+'box_size-pressure_stretch'

            box_size_pressure_data = numpy.loadtxt(cellulose_box_size_pressure_data_file_location)
            strain_data = abs(box_size_pressure_data[:,3]/box_size_pressure_data[0,3]-1.0)
            stress_data = -0.1*box_size_pressure_data[:,6]
            fitted_elastic_modulus = numpy.dot(strain_data,stress_data)/numpy.dot(strain_data,strain_data)

            elastic_modulus_difference = abs(fitted_elastic_modulus-reference_elastic_modulus)
            elastic_modulus_match_degree = default_elastic_modulus_match_degree
            if elastic_modulus_difference <= elastic_modulus_difference_threshold:
                elastic_modulus_match_degree = compute_square_root_match_degree(fitted_elastic_modulus,reference_elastic_modulus)

        except:
            fitted_elastic_modulus = default_fitted_elastic_modulus
            elastic_modulus_match_degree = default_elastic_modulus_match_degree

        return fitted_elastic_modulus,elastic_modulus_match_degree

    def post_processing_polymer_stiffness(self,inputs_directory,results_directory,reference_persistence_length,reference_end_to_end_distance):
        
        try:

            lammps_relaxation_dump_file_location = results_directory+'cl_relaxation'
            cellulose_persistence_length_file_location = results_directory+'cl_persistence_length.txt'
            cellulose_end_to_end_distance_file_location = results_directory+'cl_end_to_end_distance.txt'

            persistence_length_computation_program_location = inputs_directory+'compute_persistence_length_from_lammps_dump'
            os.chmod(persistence_length_computation_program_location,0o777)
            subprocess.run([persistence_length_computation_program_location,lammps_relaxation_dump_file_location,'1','1',cellulose_persistence_length_file_location],cwd=results_directory,stdout=subprocess.DEVNULL,check=True)

            end_to_end_distance_computation_program_location = inputs_directory+'compute_end_to_end_distance_from_lammps_dump'
            os.chmod(end_to_end_distance_computation_program_location,0o777)
            subprocess.run([end_to_end_distance_computation_program_location,lammps_relaxation_dump_file_location,'1',cellulose_end_to_end_distance_file_location],cwd=results_directory,stdout=subprocess.DEVNULL,check=True)

            raw_cellulose_persistence_length_data = numpy.loadtxt(cellulose_persistence_length_file_location)
            raw_cellulose_end_to_end_distance_data = numpy.loadtxt(cellulose_end_to_end_distance_file_location)

            average_bond_length = raw_cellulose_persistence_length_data[-1,0]
            average_persistence_length = raw_cellulose_persistence_length_data[-1,-1]
            average_end_to_end_distance = raw_cellulose_end_to_end_distance_data[-1,-1]

            persistence_length_difference = abs(average_persistence_length-reference_persistence_length)
            persistence_length_match_degree = default_persistence_length_match_degree
            if persistence_length_difference <= persistence_length_difference_threshold:
                persistence_length_match_degree = compute_square_root_match_degree(average_persistence_length,reference_persistence_length)

            end_to_end_distance_difference = abs(average_end_to_end_distance-reference_end_to_end_distance)
            end_to_end_distance_match_degree = default_end_to_end_distance_match_degree
            if end_to_end_distance_difference <= end_to_end_distance_difference_threshold:
                end_to_end_distance_match_degree = compute_square_root_match_degree(average_end_to_end_distance,reference_end_to_end_distance)

        except:
            average_bond_length = default_average_bond_length
            average_persistence_length = default_average_persistence_length
            persistence_length_match_degree = default_persistence_length_match_degree
            average_end_to_end_distance = default_average_end_to_end_distance
            end_to_end_distance_match_degree = default_end_to_end_distance_match_degree

        return average_bond_length,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree

    def post_processing_transverse_stretch(self,inputs_directory,results_directory,reference_relaxation_average_direction_angle,reference_fracture_average_direction_angle,reference_fracture_rotation_angle,reference_max_stress,reference_max_strain_energy,reference_equivalent_strain):
        
        try:

            cellulose_relaxation_msd_data_file_location = results_directory+'cl_msd_relaxation'
            cellulose_box_size_pressure_relaxation_data_file_location = results_directory+'box_size-pressure_relaxation'

            average_direction_angle_computation_program_location = inputs_directory+'compute_average_direction_angle_from_lammps_dump'
            lammps_relaxation_dump_file_location = results_directory+'cl_relaxation'
            lammps_stretch_dump_file_location = results_directory+'cl_stretch'
            cellulose_relaxation_average_direction_angle_file_location = results_directory+'cl_average_direction_angle_relaxation.txt'
            cellulose_stretch_average_direction_angle_file_location = results_directory+'cl_average_direction_angle_stretch.txt'
            os.chmod(average_direction_angle_computation_program_location,0o777)
            subprocess.run([average_direction_angle_computation_program_location,lammps_relaxation_dump_file_location,'1','2',cellulose_relaxation_average_direction_angle_file_location],cwd=results_directory,stdout=subprocess.DEVNULL,check=True)
            subprocess.run([average_direction_angle_computation_program_location,lammps_stretch_dump_file_location,'1','2',cellulose_stretch_average_direction_angle_file_location],cwd=results_directory,stdout=subprocess.DEVNULL,check=True)

            cellulose_box_size_pressure_stretch_data_file_location = results_directory+'box_size-pressure_stretch'

            cellulose_msd_data = numpy.loadtxt(cellulose_relaxation_msd_data_file_location)
            cellulose_rmsd_data = numpy.sqrt(cellulose_msd_data)
            box_size_pressure_relaxation_data = numpy.loadtxt(cellulose_box_size_pressure_relaxation_data_file_location)
            box_volume = box_size_pressure_relaxation_data[:,1]*box_size_pressure_relaxation_data[:,2]*box_size_pressure_relaxation_data[:,3]
            relaxation_average_direction_angle_data = numpy.loadtxt(cellulose_relaxation_average_direction_angle_file_location)[:,-1]
            stretch_average_direction_angle_data = numpy.loadtxt(cellulose_stretch_average_direction_angle_file_location)[:,-1]

            box_size_pressure_stretch_data = numpy.loadtxt(cellulose_box_size_pressure_stretch_data_file_location)
            strain_data = abs(box_size_pressure_stretch_data[:,2]/box_size_pressure_stretch_data[0,2]-1.0)
            stress_data = smooth_data(-0.1*box_size_pressure_stretch_data[:,5])

            average_rmsd_data = numpy.mean(cellulose_rmsd_data[-1,-1])
            average_box_volume_change = numpy.mean(abs(box_volume/box_volume[0]-1.0)[-1])
            relaxation_average_direction_angle = relaxation_average_direction_angle_data[-1]
            relaxation_average_direction_angle_difference = abs(relaxation_average_direction_angle-reference_relaxation_average_direction_angle)
            system_stable_enough_switch = default_system_stable_enough_switch
            if average_rmsd_data <= average_rmsd_threshold and average_box_volume_change <= average_box_volume_change_threshold and relaxation_average_direction_angle_difference <= relaxation_average_direction_angle_difference_threshold:
                system_stable_enough_switch = 1.0

            fracture_average_direction_angle = stretch_average_direction_angle_data[-1]
            fracture_average_direction_angle_difference = abs(fracture_average_direction_angle-reference_fracture_average_direction_angle)
            fracture_average_direction_angle_match_degree = default_fracture_average_direction_angle_match_degree
            if fracture_average_direction_angle_difference <= fracture_average_direction_angle_difference_threshold:
                fracture_average_direction_angle_match_degree = 1.0

            fracture_rotation_angle = abs(relaxation_average_direction_angle-fracture_average_direction_angle)
            fracture_rotation_angle_difference = abs(fracture_rotation_angle-reference_fracture_rotation_angle)
            fracture_rotation_angle_match_degree = default_fracture_rotation_angle_match_degree
            if fracture_rotation_angle_difference <= fracture_rotation_angle_difference_threshold:
                fracture_rotation_angle_match_degree = 1.0

            max_stress = numpy.max(stress_data)
            max_strain_energy = scipy.integrate.simpson(y=stress_data,x=strain_data)
            equivalent_strain = max_strain_energy/max_stress

            max_stress_match_degree = compute_linear_match_degree(max_stress,reference_max_stress)
            max_strain_energy_match_degree = compute_linear_match_degree(max_strain_energy,reference_max_strain_energy)
            equivalent_strain_match_degree = compute_square_match_degree(equivalent_strain,reference_equivalent_strain)

        except:
            system_stable_enough_switch = default_system_stable_enough_switch
            fracture_average_direction_angle_match_degree = default_fracture_average_direction_angle_match_degree
            fracture_rotation_angle_match_degree = default_fracture_rotation_angle_match_degree
            max_stress = default_max_stress
            max_stress_match_degree = default_max_stress_match_degree
            max_strain_energy = default_max_strain_energy
            max_strain_energy_match_degree = default_max_strain_energy_match_degree
            equivalent_strain = default_equivalent_strain
            equivalent_strain_match_degree = default_equivalent_strain_match_degree

        return system_stable_enough_switch,fracture_average_direction_angle_match_degree,fracture_rotation_angle_match_degree,max_stress,max_stress_match_degree,max_strain_energy,max_strain_energy_match_degree,equivalent_strain,equivalent_strain_match_degree

    def post_processing_1(self,reference_elastic_modulus):
        
        fitted_elastic_modulus,elastic_modulus_match_degree = self.post_processing_axial_stretch(self.physics_computation_1_results_directory,reference_elastic_modulus)

        return fitted_elastic_modulus,elastic_modulus_match_degree

    def post_processing_2(self,reference_persistence_length):
        
        average_bond_length,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree = self.post_processing_polymer_stiffness(self.physics_computation_2_inputs_directory,self.physics_computation_2_results_directory,reference_persistence_length,reference_physics_computation_2_end_to_end_distance)

        return average_bond_length,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree

    def post_processing_3(self,reference_persistence_length):
        
        average_bond_length,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree = self.post_processing_polymer_stiffness(self.physics_computation_3_inputs_directory,self.physics_computation_3_results_directory,reference_persistence_length,reference_physics_computation_3_end_to_end_distance)

        return average_bond_length,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree

    def post_processing_4(self,reference_persistence_length):
        
        average_bond_length,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree = self.post_processing_polymer_stiffness(self.physics_computation_4_inputs_directory,self.physics_computation_4_results_directory,reference_persistence_length,reference_physics_computation_4_end_to_end_distance)

        return average_bond_length,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree

    def post_processing_5(self):

        system_stable_enough_switch,fracture_average_direction_angle_match_degree,fracture_rotation_angle_match_degree,max_stress,max_stress_match_degree,max_strain_energy,max_strain_energy_match_degree,equivalent_strain,equivalent_strain_match_degree = self.post_processing_transverse_stretch(self.physics_computation_5_inputs_directory,self.physics_computation_5_results_directory,reference_physics_computation_5_relaxation_average_direction_angle,reference_physics_computation_5_fracture_average_direction_angle,reference_physics_computation_5_fracture_rotation_angle,reference_physics_computation_5_max_stress,reference_physics_computation_5_max_strain_energy,reference_physics_computation_5_equivalent_strain)

        max_strain_energy_match_degree = compute_linear_match_degree(max_strain_energy, 0.9*reference_physics_computation_5_max_strain_energy)

        if max_strain_energy < 0.9*reference_physics_computation_5_max_strain_energy:
            max_strain_energy_match_degree = 1.0

        cellulose_box_size_pressure_stretch_data_file_location = self.physics_computation_5_results_directory+'box_size-pressure_stretch'
        box_size_pressure_stretch_data = numpy.loadtxt(cellulose_box_size_pressure_stretch_data_file_location)
        orthogonal_direction_box_size = box_size_pressure_stretch_data[:,1]
        average_orthogonal_direction_box_size_change = numpy.mean(abs(orthogonal_direction_box_size/orthogonal_direction_box_size[0]-1.0)[-1])
        if average_orthogonal_direction_box_size_change > average_orthogonal_direction_box_size_change_threshold:
            fracture_average_direction_angle_match_degree = 0.5*fracture_average_direction_angle_match_degree
            fracture_rotation_angle_match_degree = 0.5*fracture_rotation_angle_match_degree

        return system_stable_enough_switch,fracture_average_direction_angle_match_degree,fracture_rotation_angle_match_degree,max_stress,max_stress_match_degree,max_strain_energy,max_strain_energy_match_degree,equivalent_strain,equivalent_strain_match_degree

    def post_processing_6(self):

        system_stable_enough_switch,fracture_average_direction_angle_match_degree,fracture_rotation_angle_match_degree,max_stress,max_stress_match_degree,max_strain_energy,max_strain_energy_match_degree,equivalent_strain,equivalent_strain_match_degree = self.post_processing_transverse_stretch(self.physics_computation_6_inputs_directory,self.physics_computation_6_results_directory,reference_physics_computation_6_relaxation_average_direction_angle,reference_physics_computation_6_fracture_average_direction_angle,reference_physics_computation_6_fracture_rotation_angle,reference_physics_computation_6_max_stress,reference_physics_computation_6_max_strain_energy,reference_physics_computation_6_equivalent_strain)

        max_strain_energy_match_degree = compute_linear_match_degree(max_strain_energy, 0.9*reference_physics_computation_6_max_strain_energy)

        if max_strain_energy < 0.9*reference_physics_computation_6_max_strain_energy:
            max_strain_energy_match_degree = 1.0

        cellulose_box_size_pressure_stretch_data_file_location = self.physics_computation_6_results_directory+'box_size-pressure_stretch'
        box_size_pressure_stretch_data = numpy.loadtxt(cellulose_box_size_pressure_stretch_data_file_location)
        orthogonal_direction_box_size = box_size_pressure_stretch_data[:,1]
        average_orthogonal_direction_box_size_change = numpy.mean(abs(orthogonal_direction_box_size/orthogonal_direction_box_size[0]-1.0)[-1])
        if average_orthogonal_direction_box_size_change > average_orthogonal_direction_box_size_change_threshold:
            fracture_average_direction_angle_match_degree = 0.5*fracture_average_direction_angle_match_degree
            fracture_rotation_angle_match_degree = 0.5*fracture_rotation_angle_match_degree

        return system_stable_enough_switch,fracture_average_direction_angle_match_degree,fracture_rotation_angle_match_degree,max_stress,max_stress_match_degree,max_strain_energy,max_strain_energy_match_degree,equivalent_strain,equivalent_strain_match_degree

    def post_processing_7(self):

        system_stable_enough_switch,fracture_average_direction_angle_match_degree,fracture_rotation_angle_match_degree,max_stress,max_stress_match_degree,max_strain_energy,max_strain_energy_match_degree,equivalent_strain,equivalent_strain_match_degree = self.post_processing_transverse_stretch(self.physics_computation_7_inputs_directory,self.physics_computation_7_results_directory,reference_physics_computation_7_relaxation_average_direction_angle,reference_physics_computation_7_fracture_average_direction_angle,reference_physics_computation_7_fracture_rotation_angle,reference_physics_computation_7_max_stress,reference_physics_computation_7_max_strain_energy,reference_physics_computation_7_equivalent_strain)

        max_stress_match_degree = compute_linear_match_degree(max_stress, 0.9*reference_physics_computation_7_max_stress)

        if max_stress < 0.9*reference_physics_computation_7_max_stress:
            max_stress_match_degree = 1.0

        max_strain_energy_match_degree = compute_linear_match_degree(max_strain_energy, 1.3*reference_physics_computation_7_max_strain_energy)

        if max_strain_energy > 1.3*reference_physics_computation_7_max_strain_energy:
            max_strain_energy_match_degree = 1.0

        return system_stable_enough_switch,fracture_average_direction_angle_match_degree,fracture_rotation_angle_match_degree,max_stress,max_stress_match_degree,max_strain_energy,max_strain_energy_match_degree,equivalent_strain,equivalent_strain_match_degree

    # Bundle v1 does not consider nonbonded interactions, uses estimated axial elastic modulus and persistence length

    def post_processing_bundle_v1(self):

        fitted_elastic_modulus,elastic_modulus_match_degree = self.post_processing_1(reference_elastic_modulus_without_nonbonded)
        average_bond_length_2,average_persistence_length_2,persistence_length_match_degree_2,average_end_to_end_distance_2,end_to_end_distance_match_degree_2 = self.post_processing_2(reference_persistence_length_without_nonbonded)
        average_bond_length_3,average_persistence_length_3,persistence_length_match_degree_3,average_end_to_end_distance_3,end_to_end_distance_match_degree_3 = self.post_processing_3(reference_persistence_length_without_nonbonded)
        average_bond_length_4,average_persistence_length_4,persistence_length_match_degree_4,average_end_to_end_distance_4,end_to_end_distance_match_degree_4 = self.post_processing_4(reference_persistence_length_without_nonbonded)

        ##print(average_persistence_length_2,average_persistence_length_3,average_persistence_length_4)
        ##print(average_end_to_end_distance_2,average_end_to_end_distance_3,average_end_to_end_distance_4)

        average_bond_length = numpy.mean((average_bond_length_2,average_bond_length_3,average_bond_length_4))
        average_persistence_length = numpy.mean((average_persistence_length_2,average_persistence_length_3,average_persistence_length_4))
        persistence_length_match_degree = numpy.min((persistence_length_match_degree_2,persistence_length_match_degree_3,persistence_length_match_degree_4))
        average_end_to_end_distance = numpy.mean((average_end_to_end_distance_2,average_end_to_end_distance_3,average_end_to_end_distance_4))
        end_to_end_distance_match_degree = numpy.min((end_to_end_distance_match_degree_2,end_to_end_distance_match_degree_3,end_to_end_distance_match_degree_4))

        return fitted_elastic_modulus,elastic_modulus_match_degree,average_bond_length,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree

    def post_processing_bundle_v2(self):

        system_stable_enough_switch_5,fracture_average_direction_angle_match_degree_5,fracture_rotation_angle_match_degree_5,max_stress_5,max_stress_match_degree_5,max_strain_energy_5,max_strain_energy_match_degree_5,equivalent_strain_5,equivalent_strain_match_degree_5 = self.post_processing_5()
        system_stable_enough_switch_6,fracture_average_direction_angle_match_degree_6,fracture_rotation_angle_match_degree_6,max_stress_6,max_stress_match_degree_6,max_strain_energy_6,max_strain_energy_match_degree_6,equivalent_strain_6,equivalent_strain_match_degree_6 = self.post_processing_6()
        system_stable_enough_switch_7,fracture_average_direction_angle_match_degree_7,fracture_rotation_angle_match_degree_7,max_stress_7,max_stress_match_degree_7,max_strain_energy_7,max_strain_energy_match_degree_7,equivalent_strain_7,equivalent_strain_match_degree_7 = self.post_processing_7()

        #print(max_stress_5,max_stress_6,max_stress_7)
        #print(max_strain_energy_5,max_strain_energy_6,max_strain_energy_7)

        system_stable_enough_switch = numpy.min((system_stable_enough_switch_5,system_stable_enough_switch_6,system_stable_enough_switch_7))
        fracture_average_direction_angle_match_degree = numpy.min((fracture_average_direction_angle_match_degree_5,fracture_average_direction_angle_match_degree_6,fracture_average_direction_angle_match_degree_7))
        fracture_rotation_angle_match_degree = numpy.min((fracture_rotation_angle_match_degree_5,fracture_rotation_angle_match_degree_6,fracture_rotation_angle_match_degree_7))

        max_stress_match_degree = numpy.min((max_stress_match_degree_5,max_stress_match_degree_6,max_stress_match_degree_7))
        if max_stress_match_degree < max_stress_match_degree_threshold:
            max_stress_match_degree = default_max_stress_match_degree
        elif max_stress_5 < 1.5*numpy.max((max_stress_6,max_stress_7)):
            max_stress_match_degree = 0.5*max_stress_match_degree

        max_strain_energy_match_degree = numpy.min((max_strain_energy_match_degree_5,max_strain_energy_match_degree_6,max_strain_energy_match_degree_7))
        if max_strain_energy_match_degree < max_strain_energy_match_degree_threshold:
            max_strain_energy_match_degree = default_max_strain_energy_match_degree
        elif max_strain_energy_7 < 1.3*numpy.max((max_strain_energy_5,max_strain_energy_6)):
            max_strain_energy_match_degree = 0.5*max_strain_energy_match_degree
        
        equivalent_strain_match_degree = numpy.min((equivalent_strain_match_degree_5,equivalent_strain_match_degree_6,equivalent_strain_match_degree_7))

        return system_stable_enough_switch,fracture_average_direction_angle_match_degree,fracture_rotation_angle_match_degree,max_stress_match_degree,max_strain_energy_match_degree,equivalent_strain_match_degree

    def post_processing_bundle_v3(self):

        fitted_elastic_modulus,elastic_modulus_match_degree = self.post_processing_1(reference_elastic_modulus_with_nonbonded)
        average_bond_length_2,average_persistence_length_2,persistence_length_match_degree_2,average_end_to_end_distance_2,end_to_end_distance_match_degree_2 = self.post_processing_2(reference_persistence_length_with_nonbonded)
        average_bond_length_3,average_persistence_length_3,persistence_length_match_degree_3,average_end_to_end_distance_3,end_to_end_distance_match_degree_3 = self.post_processing_3(reference_persistence_length_with_nonbonded)
        average_bond_length_4,average_persistence_length_4,persistence_length_match_degree_4,average_end_to_end_distance_4,end_to_end_distance_match_degree_4 = self.post_processing_4(reference_persistence_length_with_nonbonded)

        ##print(average_persistence_length_2,average_persistence_length_3,average_persistence_length_4)
        ##print(average_end_to_end_distance_2,average_end_to_end_distance_3,average_end_to_end_distance_4)

        average_bond_length = numpy.mean((average_bond_length_2,average_bond_length_3,average_bond_length_4))
        average_persistence_length = numpy.mean((average_persistence_length_2,average_persistence_length_3,average_persistence_length_4))
        persistence_length_match_degree = numpy.min((persistence_length_match_degree_2,persistence_length_match_degree_3,persistence_length_match_degree_4))
        average_end_to_end_distance = numpy.mean((average_end_to_end_distance_2,average_end_to_end_distance_3,average_end_to_end_distance_4))
        end_to_end_distance_match_degree = numpy.min((end_to_end_distance_match_degree_2,end_to_end_distance_match_degree_3,end_to_end_distance_match_degree_4))

        system_stable_enough_switch_5,fracture_average_direction_angle_match_degree_5,fracture_rotation_angle_match_degree_5,max_stress_5,max_stress_match_degree_5,max_strain_energy_5,max_strain_energy_match_degree_5,equivalent_strain_5,equivalent_strain_match_degree_5 = self.post_processing_5()
        system_stable_enough_switch_6,fracture_average_direction_angle_match_degree_6,fracture_rotation_angle_match_degree_6,max_stress_6,max_stress_match_degree_6,max_strain_energy_6,max_strain_energy_match_degree_6,equivalent_strain_6,equivalent_strain_match_degree_6 = self.post_processing_6()
        system_stable_enough_switch_7,fracture_average_direction_angle_match_degree_7,fracture_rotation_angle_match_degree_7,max_stress_7,max_stress_match_degree_7,max_strain_energy_7,max_strain_energy_match_degree_7,equivalent_strain_7,equivalent_strain_match_degree_7 = self.post_processing_7()

        #print(max_stress_5,max_stress_6,max_stress_7)
        #print(max_strain_energy_5,max_strain_energy_6,max_strain_energy_7)

        system_stable_enough_switch = numpy.min((system_stable_enough_switch_5,system_stable_enough_switch_6,system_stable_enough_switch_7))
        fracture_average_direction_angle_match_degree = numpy.min((fracture_average_direction_angle_match_degree_5,fracture_average_direction_angle_match_degree_6,fracture_average_direction_angle_match_degree_7))
        fracture_rotation_angle_match_degree = numpy.min((fracture_rotation_angle_match_degree_5,fracture_rotation_angle_match_degree_6,fracture_rotation_angle_match_degree_7))

        max_stress_match_degree = numpy.min((max_stress_match_degree_5,max_stress_match_degree_6,max_stress_match_degree_7))
        if max_stress_match_degree < max_stress_match_degree_threshold:
            max_stress_match_degree = default_max_stress_match_degree
        elif max_stress_5 < 1.5*numpy.max((max_stress_6,max_stress_7)):
            max_stress_match_degree = 0.5*max_stress_match_degree

        max_strain_energy_match_degree = numpy.min((max_strain_energy_match_degree_5,max_strain_energy_match_degree_6,max_strain_energy_match_degree_7))
        if max_strain_energy_match_degree < max_strain_energy_match_degree_threshold:
            max_strain_energy_match_degree = default_max_strain_energy_match_degree
        elif max_strain_energy_7 < 1.3*numpy.max((max_strain_energy_5,max_strain_energy_6)):
            max_strain_energy_match_degree = 0.5*max_strain_energy_match_degree
        
        equivalent_strain_match_degree = numpy.min((equivalent_strain_match_degree_5,equivalent_strain_match_degree_6,equivalent_strain_match_degree_7))

        return fitted_elastic_modulus,elastic_modulus_match_degree,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree,system_stable_enough_switch,fracture_average_direction_angle_match_degree,fracture_rotation_angle_match_degree,max_stress_match_degree,max_strain_energy_match_degree,equivalent_strain_match_degree

if __name__=='__main__':

    import sys

    working_directory = sys.argv[1]

    post_processing_version = sys.argv[2]

    if post_processing_version == 'v1':
        print(CoarseGrainedCellulosePostProcessing(working_directory).post_processing_bundle_v1())
    elif post_processing_version == 'v2':
        print(CoarseGrainedCellulosePostProcessing(working_directory).post_processing_bundle_v2())
    elif post_processing_version == 'v3':
        print(CoarseGrainedCellulosePostProcessing(working_directory).post_processing_bundle_v3())
