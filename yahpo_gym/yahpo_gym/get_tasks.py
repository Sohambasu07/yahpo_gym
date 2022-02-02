from pandas import read_json
from yahpo_gym.local_config import local_config

def get_tasks(type:str, version:int =0):
    """
    Interface for benchmark scenario meta information. 
    Abstract base class used to instantiate configurations that contain all
    relevant meta-information about a specific benchmark scenario.

    Parameters
    ----------
    type: str
        The type of benchmark to be used. Can be either 'single' (single-objective) or 'multi' (multi-objective).
    version: int
        The version of the benchmark to be used.
    """
    assert type in ['single', 'multi'], "type must be either 'single' or 'multi'"
    assert _data_has_version(version), "version must coincide with version in `local_config.data_path`"
    # Get file
    fp = local_config.data_path.joinpath("benchmark_tasks").joinpath(f"{type}_v{version}.json")
    # Read json
    with open(fp, "r") as f:
        data = read_json(f, orient='records')
    return data

def _data_has_version(version: int):
    fp = local_config.data_path.joinpath("VERSION")
    with open(fp, "r") as f:
        for line in f:
            if line.startswith(f'VERSION:{version}'):
                return True
