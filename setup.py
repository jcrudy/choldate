import os
import warnings
from setuptools import setup, Extension
import numpy

pyx_path = "choldate/_choldate.pyx"
c_path = "choldate/_choldate.c"

try:
    from Cython.Build import cythonize
    has_cython = True
except ImportError:
    has_cython = False

if has_cython and os.path.exists(pyx_path):
    ext_modules = cythonize(
        [Extension("choldate._choldate", [pyx_path], include_dirs=[numpy.get_include()])]
    )
else:
    ext_modules = [
        Extension("choldate._choldate", [c_path], include_dirs=[numpy.get_include()])
    ]
    if has_cython and not os.path.exists(pyx_path):
        warnings.warn("_choldate.pyx not found; using pre-generated _choldate.c")
    elif not has_cython:
        warnings.warn("Cython not available; using pre-generated _choldate.c")

setup(
    name="choldate",
    version="0.1.0",
    description="Cholesky update/downdate routines",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jason Rudy",
    packages=["choldate", "choldate.test"],
    ext_modules=ext_modules,
    python_requires=">=3.8",
    install_requires=["numpy"],
    extras_require={
        "build": ["cython"],
    },
    zip_safe=False,
)
