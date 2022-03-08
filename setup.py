from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name='Hello world 1',
    ext_modules=cythonize("convolve1.pyx", annotate=True),
    zip_safe=False,
)

setup(
    name='Hello world 2',
    ext_modules=cythonize("convolve2.pyx", annotate=True),
    include_dirs=[np.get_include()],
    zip_safe=False,
)
