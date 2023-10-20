""" Tasks to perform style, lint and test """
import os
from subprocess import call
from invoke import task

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(CURR_DIR, "signal_interpreter_server")
UNIT_TEST_DIR = os.path.join(CURR_DIR, "signal_interpreter_server")
COV_PATH = os.path.join(CURR_DIR, ".coveragerc")


@task
def style(_):
    """ Style check """
    _run_cmd(f"pycodestyle {SRC_DIR} --ignore=E501")


@task
def lint(_):
    """ Lint check """
    _run_cmd(f"pylint {SRC_DIR}")


@task
def unit_test(_):
    """ Run unit tests """
    _run_cmd(f"pytest {UNIT_TEST_DIR} --cov {SRC_DIR} --cov-config={COV_PATH} --verbose")


def _run_cmd(cmd):
    """ Run command in shell """
    return_value = call(cmd, shell=True)
    if return_value == 0:
        print("Success!")
    else:
        print(f'Failed to run:\n"{cmd}"\nwith exit code: {return_value}')
