import numpy
import os
import subprocess
import sys

import multiprocessing
import pathlib
import shutil
import time
import traceback

lammps_executive_name = 'lmp'
lammps_backend_switch = 'omp'
coarse_grained_cellulose_computation_timeout = 600.0

max_cpu_logical_processor_no = multiprocessing.cpu_count()-1

def determine_base_directories_to_run(lammps_results_overwrite_switch):

    current_user_main_directory = str(pathlib.Path.home())+'/'
    try:
        coarse_grained_cellulose_computation_home_directory = os.getenv('CLL_CG_HOME')+'/'
    except:
        coarse_grained_cellulose_computation_home_directory = current_user_main_directory

    code_directory = sys.path[0]+'/'

    run_mode = 'debug'

    if len(sys.argv) > 1:
        run_mode = sys.argv[1]

    if run_mode == 'debug':
        working_directory = sys.path[0]+'/debug/'
    else:
        working_directory_base = coarse_grained_cellulose_computation_home_directory+'coarse_grained_cellulose_parameters_data/physics_computations/manual/coarse_grained_cellulose_computations/coarse_grained_cellulose_computation'
        if lammps_results_overwrite_switch == True:
            working_directory = working_directory_base+'/'
        else:
            current_time = time.strftime('%Y-%m-%d-%H:%M:%S')
            working_directory = working_directory_base+'-'+current_time+'/'

    try:
        pathlib.Path(working_directory).mkdir(parents=True,exist_ok=True)
        shutil.rmtree(working_directory)
    except:
        current_time = time.strftime('%Y-%m-%d-%H:%M:%S')
        working_directory = working_directory+current_time+'/'

    return code_directory,working_directory

def processing_before_computation_task_scheduling(task_number,code_directory,working_directory,computation_queue_list,computation_process_list,computation_class,interaction_coefficients):

    code_inputs_directory_list = []
    for i in range(0,task_number):
        temp_code_inputs_directory = code_directory+'physics_computation_'+str(i+1)+'/inputs/'
        code_inputs_directory_list.append(temp_code_inputs_directory)

    try:
        pathlib.Path(working_directory).mkdir(parents=True,exist_ok=True)
        shutil.rmtree(working_directory)
    except:
        current_time = time.strftime('%Y-%m-%d-%H:%M:%S')
        working_directory = working_directory+current_time+'/'

    computation_inputs_directory_list = []
    computation_results_directory_list = []
    for i in range(0,task_number):
        temp_computation_inputs_directory = working_directory+'physics_computation_'+str(i+1)+'/inputs/'
        temp_computation_results_directory = working_directory+'physics_computation_'+str(i+1)+'/results/'
        computation_inputs_directory_list.append(temp_computation_inputs_directory)
        computation_results_directory_list.append(temp_computation_results_directory)

    pathlib.Path(working_directory).mkdir(parents=True,exist_ok=True)
    for directory_list in (computation_inputs_directory_list,computation_results_directory_list):
        for directory in directory_list:
            pathlib.Path(directory).mkdir(parents=True,exist_ok=True)

    for i in range(0,task_number):
        for file_name in ('in_file_constant_head.txt','in_file_constant_tail.txt','coarse_grained_cellulose.data'):
            shutil.copyfile(code_inputs_directory_list[i]+file_name,computation_inputs_directory_list[i]+file_name)

    for i in (1,2,3):
        for file_name in ('compute_persistence_length_from_lammps_dump','compute_end_to_end_distance_from_lammps_dump'):
            shutil.copyfile(code_inputs_directory_list[i]+file_name,computation_inputs_directory_list[i]+file_name)

    if task_number == 7:
        for i in (4,5,6):
            for file_name in ('compute_average_direction_angle_from_lammps_dump',):
                shutil.copyfile(code_inputs_directory_list[i]+file_name,computation_inputs_directory_list[i]+file_name)

    for i in range(0,task_number):
        computation_queue_list.append(multiprocessing.Queue())
    for queue in computation_queue_list:
        queue.put(False)

    for i in range(0,task_number):
        computation_process_list.append(multiprocessing.Process(target=computation_class.physics_computation,daemon=True,args=(i,computation_queue_list[i],)))

    computation_class.in_file_generation(interaction_coefficients)

def computation_task_scheduling_bonded(computation_process_list):

    last_computation_process = computation_process_list[-1]

    last_computation_process.start()

    computation_process_array = computation_process_list[0:3]
    for process in computation_process_array:
        process.start()
        process.join(timeout=coarse_grained_cellulose_computation_timeout)

    last_computation_process.join()

def computation_task_scheduling_bonded_and_nonbonded(computation_process_list):

    last_computation_process = computation_process_list[-1]

    last_computation_process.start()

    computation_process_array = computation_process_list[0:2]
    for process in computation_process_array:
        process.start()
    for process in computation_process_array:
        process.join(timeout=coarse_grained_cellulose_computation_timeout)

    computation_process_array = computation_process_list[2:4]
    for process in computation_process_array:
        process.start()
    for process in computation_process_array:
        process.join(timeout=coarse_grained_cellulose_computation_timeout)

    computation_process_array = computation_process_list[4:6]
    for process in computation_process_array:
        process.start()
        process.join(timeout=coarse_grained_cellulose_computation_timeout)
        
    last_computation_process.join(timeout=coarse_grained_cellulose_computation_timeout)

def processing_after_computation_task_scheduling(task_number,computation_queue_list,computation_process_list):

    computation_return_list = []
    for i in range(0,task_number):
        temp_computation_queue_result = computation_queue_list[i].get()
        computation_return_list.append(temp_computation_queue_result)

    for queue in computation_queue_list:
        queue.close()

    for process in computation_process_list:
        if process.is_alive() == True:
            process.kill()
        process.join()
        process.close()

    computation_return = True
    for i in range(0,task_number):
        if computation_return_list[i] == False:
            computation_return = False

    return computation_return

class CoarseGrainedCelluloseComputationCommon():

    def __init__(self,task_number,working_directory):

        self.working_directory = working_directory

        self.physics_computation_inputs_directory_list = []
        self.physics_computation_results_directory_list = []
        self.physics_computation_in_file_location_list = []
        self.lammps_physics_computation_command_list = []

        for i in range(0,task_number):
            temp_physics_computation_inputs_directory = working_directory+'physics_computation_'+str(i+1)+'/inputs/'
            temp_physics_computation_results_directory = working_directory+'physics_computation_'+str(i+1)+'/results/'
            temp_physics_computation_in_file_location = temp_physics_computation_inputs_directory+'coarse_grained_cellulose.in'
            temp_lammps_physics_computation_command = (lammps_executive_name,'-in',temp_physics_computation_in_file_location)
            self.physics_computation_inputs_directory_list.append(temp_physics_computation_inputs_directory)
            self.physics_computation_results_directory_list.append(temp_physics_computation_results_directory)
            self.physics_computation_in_file_location_list.append(temp_physics_computation_in_file_location)
            self.lammps_physics_computation_command_list.append(temp_lammps_physics_computation_command)

        self.post_processing_results_location = working_directory+'post_processing_results.txt'

    def physics_computation_exception_traceback_and_save(self,physics_computation_exception_type):

        Except_Error = traceback.format_exc()
        error_file = open(self.working_directory+''+physics_computation_exception_type+'_Except_Error.txt','w',encoding='utf-8')
        error_file.write(Except_Error)
        error_file.close()

    def physics_computation(self,target_number,queue):

        try:
            subprocess.run(self.lammps_physics_computation_command_list[target_number],cwd=self.physics_computation_results_directory_list[target_number],stdout=subprocess.DEVNULL,check=True)
            queue.get()
            queue.put(True)
            return True
        except:
            self.physics_computation_exception_traceback_and_save('Physics_Computation')
            queue.get()
            queue.put(False)
            return False

    def post_processing(self,physics_computation_return,version,post_processing_results_header,default_results_array,post_processing_class):

        post_processing_results_array = default_results_array
        if physics_computation_return == True:
            try:
                if version == 1:
                    post_processing_results_array = post_processing_class.post_processing_bundle_v1()
                else:
                    post_processing_results_array = post_processing_class.post_processing_bundle_v3()
            except:
                self.physics_computation_exception_traceback_and_save('Post_Processing')

        numpy.savetxt(self.post_processing_results_location,post_processing_results_array,header=post_processing_results_header,fmt='%.6f',delimiter=',')

        return post_processing_results_array


