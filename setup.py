from setuptools import setup, find_packages

setup(
    name='mwdgt',
    version='0.1',
    packages=find_packages(),
    install_requires=['xarray', 'numpy', 'h5py'],
    author='Mahesh Bakal',
    description='MaheshWindDataGettingThing: Extract and interpolate MERRA-2 wind data.',
)
