import optuna
import numpy
import sys
import os
import pathlib

physics_version = sys.argv[1]
optuna_sampler_name = sys.argv[2]
optuna_training_steps = int(sys.argv[3])

physics_version_specific_code_directory = sys.path[0]+'/physics_version_specific/'+physics_version+'/'
sys.path.append(physics_version_specific_code_directory)

from coarse_grained_cellulose_coefficients_optuna_training_specific import code_version
from coarse_grained_cellulose_coefficients_optuna_training_specific import indepedent_variable_total_number
from coarse_grained_cellulose_coefficients_optuna_training_specific import generate_interaction_coefficients

coefficient_precision_format = '%.4g'

current_user_main_directory = str(pathlib.Path.home())+'/'
try:
    coarse_grained_cellulose_computation_home_directory = os.getenv('CLL_CG_HOME')+'/'
except:
    coarse_grained_cellulose_computation_home_directory = current_user_main_directory

coarse_grained_cellulose_computation_code_directory = coarse_grained_cellulose_computation_home_directory+'coarse_grained_cellulose_coefficients_code/physics_computation_pool/'+code_version+'_physics/'

sys.path.append(coarse_grained_cellulose_computation_code_directory)

from coarse_grained_cellulose_coefficients_env_common import CoarseGrainedCelluloseCoefficientsEnvCommon

from coarse_grained_cellulose_computation import post_processing_version

def optuna_objective(trial):

    unscaled_parameter_array = [trial.suggest_float(f"x{i}", -1, 1) for i in range(indepedent_variable_total_number)]

    interaction_coefficients = generate_interaction_coefficients(coefficient_precision_format,unscaled_parameter_array)

    coarse_grained_cellulose_coefficients_env_common_class = CoarseGrainedCelluloseCoefficientsEnvCommon(coarse_grained_cellulose_computation_home_directory,coarse_grained_cellulose_computation_code_directory,physics_version)

    if post_processing_version == 3:
        physics_computation_return = coarse_grained_cellulose_coefficients_env_common_class.processing_bonded_and_nonbonded(interaction_coefficients)
    else:
        physics_computation_return = coarse_grained_cellulose_coefficients_env_common_class.processing_bonded(interaction_coefficients)

    score = physics_computation_return[-1]

    return score

training_data_directory = sys.path[0]+'/'+'../coarse_grained_cellulose_coefficients_optuna_data/'+physics_version+'_training_data/'
pathlib.Path(training_data_directory).mkdir(parents=True,exist_ok=True)

optuna_study_name = physics_version+'_coarse_grained_cellulose_coefficients_optuna_'+optuna_sampler_name
optuna_log_path = training_data_directory+optuna_study_name+'.log'
optuna_trial_steps_file_location = training_data_directory+optuna_study_name+'_trial_steps.txt'
optuna_trial_best_file_location = training_data_directory+optuna_study_name+'_trial_best.txt'

if optuna_sampler_name == 'cmaes':
    optuna_sampler = optuna.samplers.CmaEsSampler()
else:
    optuna_sampler = optuna.samplers.TPESampler()

optuna_storage = optuna.storages.JournalStorage(optuna.storages.journal.JournalFileBackend(optuna_log_path))

optuna_study = optuna.create_study(study_name=optuna_study_name, sampler=optuna_sampler, storage=optuna_storage, load_if_exists=True, direction="maximize")

optuna_study.optimize(optuna_objective, n_trials=optuna_training_steps)

print(optuna_study.best_trial.value, optuna_study.best_trial.params)

trials_dataframe = optuna_study.trials_dataframe()

trials_dataframe_completed_raw = trials_dataframe[trials_dataframe["state"] == "COMPLETE"].drop(columns=['datetime_start','datetime_complete','duration','state'])

cols_to_keep = [c for c in trials_dataframe_completed_raw.columns if "system_attrs" not in c]
trials_dataframe_completed = trials_dataframe_completed_raw[cols_to_keep]

param_cols = [c for c in trials_dataframe_completed.columns if c.startswith('params_x')]
other_cols = [c for c in trials_dataframe_completed.columns if not c.startswith('params_x')]

param_cols.sort(key=lambda x: int(x.split('x')[-1]))

trials_dataframe_completed = trials_dataframe_completed[other_cols+param_cols]

header_string = "#"+",".join(trials_dataframe_completed.columns)+"\n"

with open(optuna_trial_steps_file_location, "w") as f:
    f.write(header_string)
    trials_dataframe_completed.to_csv(f, float_format='%.6e', header=False, index=False)

trial_dataframe_best = trials_dataframe_completed[trials_dataframe_completed["number"] == optuna_study.best_trial.number]

with open(optuna_trial_best_file_location, "w") as f:
    f.write(header_string)
    trial_dataframe_best.to_csv(f, header=False, index=False)

