import io
import os

from setuptools import setup

DESCRIPTION = 'Benchmark script for numpy ndarray access.'
here = os.path.abspath(os.path.dirname(__file__))
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# load __version__
exec(open(os.path.join(here, 'ndarray_access_benchmark', '_version.py')).read())

setup(
    name='ndarray_access_benchmark',
    version=__version__,
    description='Benchmark script for numpy ndarray access.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kazuhiro Serizawa',
    author_email='nserihiro@gmail.com',
    url='https://github.com/serihiro/ndarray_access_benchmark',
    license='MIT',
    packages=[
        'ndarray_access_benchmark',
        'ndarray_access_benchmark.benchmarks'
    ],
    install_requires=['numpy>=1.15.0', 'memory_profiler>=0.52'],
    entry_points={
        'console_scripts': ['nabm=ndarray_access_benchmark.cli:main']
    }
)
