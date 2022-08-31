import sys
from pathlib import Path

from setuptools import setup, find_packages

CURRENT_DIRECTORY = Path(__file__).parent.absolute()

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)
VER_ERR_MSG = """
==========================
Unsupported Python version
==========================
This version of iblutil requires Python {}.{}, but you're trying to
install it on Python {}.{}.
"""
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(VER_ERR_MSG.format(*REQUIRED_PYTHON + CURRENT_PYTHON))
    sys.exit(1)

with open("README.md", "r") as f:
    long_description = f.read()

# TODO: flesh out requirement file
# with open("requirements.txt") as f:
#     require = [x.strip() for x in f.readlines() if not x.startswith('git+')]


def read(rel_path):
    here = Path(__file__).parent.absolute()
    with open(here.joinpath(rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='iblpybpod',
    version=get_version(Path("iblpybpod").joinpath("__init__.py")),
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    description='IBL implementation of pybpod software',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='IBL Staff',
    url='https://github.com/int-brain-lab/iblpybpod/',
    packages=find_packages(exclude=['scratch', 'tests']),  # same as name
    include_package_data=True,
    # external packages as dependencies
    # install_requires=require,
    entry_points={},
    scripts=[]
)
