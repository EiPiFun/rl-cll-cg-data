import sys
import time

lammps_results_overwrite_switch = True

with_threshold_switch = True

def determine_computation_working_directory(computation_home_directory,physics_version):
    computation_working_directory_base = computation_home_directory+'coarse_grained_cellulose_coefficients_data/physics_computations/training/'+physics_version+'_physics_computations/'+physics_version+'_physics_computation'
    if lammps_results_overwrite_switch == True:
        computation_working_directory = computation_working_directory_base+'/'
    else:
        current_time = time.strftime('%Y-%m-%d-%H:%M:%S')
        computation_working_directory = computation_working_directory_base+'-'+current_time+'/'
    return computation_working_directory

class CoarseGrainedCelluloseCoefficientsEnvCommon():

    def __init__(self,coarse_grained_cellulose_computation_home_directory,coarse_grained_cellulose_computation_code_directory,physics_version):

        sys.path.append(coarse_grained_cellulose_computation_code_directory)

        from coarse_grained_cellulose_computation_common import lammps_backend_switch

        from coarse_grained_cellulose_computation_common import processing_before_computation_task_scheduling
        from coarse_grained_cellulose_computation_common import computation_task_scheduling_bonded
        from coarse_grained_cellulose_computation_common import computation_task_scheduling_bonded_and_nonbonded
        from coarse_grained_cellulose_computation_common import processing_after_computation_task_scheduling

        from coarse_grained_cellulose_computation import CoarseGrainedCelluloseComputation

        self.processing_before_computation_task_scheduling = processing_before_computation_task_scheduling
        self.computation_task_scheduling_bonded = computation_task_scheduling_bonded
        self.computation_task_scheduling_bonded_and_nonbonded = computation_task_scheduling_bonded_and_nonbonded
        self.processing_after_computation_task_scheduling = processing_after_computation_task_scheduling

        self.coarse_grained_cellulose_computation_code_directory = coarse_grained_cellulose_computation_code_directory

        coarse_grained_cellulose_computation_working_directory = determine_computation_working_directory(coarse_grained_cellulose_computation_home_directory,physics_version)
        self.coarse_grained_cellulose_computation_working_directory = coarse_grained_cellulose_computation_working_directory

        self.coarse_grained_cellulose_computation_queue_list = []
        self.coarse_grained_cellulose_computation_process_list = []

        self.coarse_grained_cellulose_computation_class = CoarseGrainedCelluloseComputation(coarse_grained_cellulose_computation_working_directory)

    def processing_bonded(self,interaction_coefficients):

        task_number = 4

        self.processing_before_computation_task_scheduling(task_number,self.coarse_grained_cellulose_computation_code_directory,self.coarse_grained_cellulose_computation_working_directory,self.coarse_grained_cellulose_computation_queue_list,self.coarse_grained_cellulose_computation_process_list,self.coarse_grained_cellulose_computation_class,interaction_coefficients)

        self.computation_task_scheduling_bonded(self.coarse_grained_cellulose_computation_process_list)

        coarse_grained_cellulose_computation_return = self.processing_after_computation_task_scheduling(task_number,self.coarse_grained_cellulose_computation_queue_list,self.coarse_grained_cellulose_computation_process_list)

        fitted_elastic_modulus,elastic_modulus_match_degree,average_bond_length,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree = self.coarse_grained_cellulose_computation_class.post_processing(coarse_grained_cellulose_computation_return)

        reward_value = 5.0*(elastic_modulus_match_degree+persistence_length_match_degree+end_to_end_distance_match_degree)

        return fitted_elastic_modulus,elastic_modulus_match_degree,average_bond_length,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree,reward_value

    def processing_bonded_and_nonbonded(self,interaction_coefficients):

        task_number = 7

        self.processing_before_computation_task_scheduling(task_number,self.coarse_grained_cellulose_computation_code_directory,self.coarse_grained_cellulose_computation_working_directory,self.coarse_grained_cellulose_computation_queue_list,self.coarse_grained_cellulose_computation_process_list,self.coarse_grained_cellulose_computation_class,interaction_coefficients)

        self.computation_task_scheduling_bonded_and_nonbonded(self.coarse_grained_cellulose_computation_process_list)

        coarse_grained_cellulose_computation_return = self.processing_after_computation_task_scheduling(task_number,self.coarse_grained_cellulose_computation_queue_list,self.coarse_grained_cellulose_computation_process_list)

        fitted_elastic_modulus,elastic_modulus_match_degree,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree,system_stable_enough_switch,fracture_average_direction_angle_match_degree,fracture_rotation_angle_match_degree,max_stress_match_degree,max_strain_energy_match_degree,equivalent_strain_match_degree = self.coarse_grained_cellulose_computation_class.post_processing(coarse_grained_cellulose_computation_return)

        if with_threshold_switch == True:
            reward_value = 5.0*(elastic_modulus_match_degree+persistence_length_match_degree+end_to_end_distance_match_degree+system_stable_enough_switch+fracture_average_direction_angle_match_degree+fracture_rotation_angle_match_degree+14.0*min(max_stress_match_degree,max_strain_energy_match_degree)+equivalent_strain_match_degree)
        else:
            reward_value = 5.0*(elastic_modulus_match_degree+persistence_length_match_degree+end_to_end_distance_match_degree+system_stable_enough_switch+fracture_average_direction_angle_match_degree+fracture_rotation_angle_match_degree+7.0*(max_stress_match_degree+max_strain_energy_match_degree)+equivalent_strain_match_degree)

        return fitted_elastic_modulus,elastic_modulus_match_degree,average_persistence_length,persistence_length_match_degree,average_end_to_end_distance,end_to_end_distance_match_degree,system_stable_enough_switch,fracture_average_direction_angle_match_degree,fracture_rotation_angle_match_degree,max_stress_match_degree,max_strain_energy_match_degree,equivalent_strain_match_degree,reward_value


