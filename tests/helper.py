from pathlib import Path
import subprocess

PARENT_PATH = str(Path(__file__).resolve().parents[1])

SCRIPT_PATH = PARENT_PATH + "/connectz.py"
TESTS_PATH = PARENT_PATH + "/tests/test_cases/"


def run_connectz(test_file_path=None):

    params = ['python3', SCRIPT_PATH]

    if test_file_path is not None:
        params.append(TESTS_PATH + test_file_path)

    result = subprocess.check_output(
        params,
        stderr=subprocess.STDOUT
    ).decode('ASCII')

    return result
