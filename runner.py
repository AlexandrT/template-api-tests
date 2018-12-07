import subprocess
import json


pytest_run_arr = ['py.test', '-v', '-l', '--html=report.html','--json=report.json']

tests_proc = subprocess.run(pytest_run_arr)

# with open('report.json') as f:
    # data = json.load(f)

if tests_proc.returncode != 0:
    raise Exception('Some tests is failed.')
