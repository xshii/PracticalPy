
1. [Install the Intel Distribution for Python with Anaconda](#install-the-intel-distribution-for-python-with-anaconda)
    1. [conda](#conda)
    2. [Keep the old environment and packages](#keep-the-old-environment-and-packages)
    3. [Install the Intel Performance Libraries](#install-the-intel-performance-libraries)
2. [Overview](#overview)
    1. [Numpy](#numpy)
    2. [Scipy](#scipy)
    3. [Configurstion](#configurstion)
    4. [Building and Installing](#building-and-installing)
3. [Testing](#testing)

# Install the Intel Distribution for Python with Anaconda

## conda
1. Update `Anaconda`
```bash
$ conda update conda
```

2. Tell conda to choose Intel packages over default packages, when available.
```bash
$ conda config --add channels intel
```

3. Create a separate environment and activate
```bash
$ conda create -n pymkl
$ source activate pymkl
```

4. In stall Intel core python3 environment
```bash
# for python3
$ conda install intelpython3_core python=3
# for python2
$ conda install intelpython2_core python=2
# Alternatively, install the full Intel distribution
$ conda install intelpython3_full python=3
```

5. there is no difference between install packages that are intel-version or not.
```bash
# sympy intel version
$ conda install sympy
# affine Non-intel version
$ conda install affine
```
* Available intel version packages: [link](https://anaconda.org/intel/packages)

## Keep the old environment and packages
1. Do **not** add the ```intel``` channel (skip `step 2`).
2. Rather, specify the `intel` channel on the command line with `-c intel` argument and the `--no-update-deps` flag to avoid switching other packages to Intel's builds.
```bash
$ conda install mkl -c install --no-update-deps
$ conda install numpy -c install --no-update-deps
```

## Install the Intel Performance Libraries
If you want to build a native extension that directly uses the performance libraries, then you will need to obtain a development package that contains header files and static libraries.

Make sure the Intel channel is added to your conda configuration (see above). 

available packages:

        mkl             Intel® Math Kernel Library (Intel® MKL) dynamic runtimes
        mkl-devel       Intel® MKL dynamic runtimes and headers for building software
        mkl-static      Intel® MKL static libraries and headers for building software
        mkl-include     Intel® MKL headers only. Automatically installed along with development packages 



# Overview
## Numpy
NumPy automatically maps operations on vectors and matrices to the `BLAS` and `LAPACK` functions wherever possible. Since Intel® MKL supports these de-facto interfaces, NumPy can benefit from Intel `MKL` optimizations through simple **modifications** to the NumPy scripts.

It consists of:
* a powerful N-dimensional array object
* sophisticated (broadcasting) functions
* tools for integrating `C/C++` and `Fortran` code
* useful linear algebra, Fourier transform, and random number capabilities
## Scipy
The SciPy library depends on `NumPy`, which provides convenient and fast N-dimensional array manipulation.

It includes modules for:
* statistics
* optimization
* integration
* linear algebra
* Fourier transforms
* signal and image processing
* ODE solvers
* ...

## Configurstion
## Building and Installing

# Testing
see `test_case.py`
```Python
# test_case.py
import numpy as np  
import time   
N = 6000  
M = 10000  
  
k_list = [64, 80, 96, 104, 112, 120, 128, 144, 160, 176, 192, 200, 208, 224, 240, 256, 384]  
  
def get_gflops(M, N, K):  
    return M*N*(2.0*K-1.0) / 1000**3  
  
np.show_config()  
  
for K in k_list:  
    a = np.array(np.random.random((M, N)), dtype=np.double, order='C', copy=False)  
    b = np.array(np.random.random((N, K)), dtype=np.double, order='C', copy=False)  
    A = np.matrix(a, dtype=np.double, copy=False)  
    B = np.matrix(b, dtype=np.double, copy=False)  
  
    C = A*B  
  
    start = time.time()  
  
    C = A*B  
    C = A*B  
    C = A*B  
    C = A*B  
    C = A*B  
  
    end = time.time()  
  
    tm = (end-start) / 5.0  
  
    print ('{0:4}, {1:9.7}, {2:9.7}'.format(K, tm, get_gflops(M, N, K) / tm))
                        
 
```
* output, the second term in each row is time cost.
```bash
  64,  0.105119,  72.48928
  80, 0.1209348,  78.88547
  96, 0.1395491,  82.12165
 104, 0.1484506,  83.66419
 112, 0.1608982,  83.15819
 120, 0.1681472,  85.28243
 128, 0.1767466,  86.56463
 144, 0.1948882,  88.35835
 160, 0.2169167,  88.23665
 176, 0.2393586,  87.98515
 192, 0.2651524,  86.66715
 200, 0.2898576,  82.59227
 208,  0.294023,  84.68724
 224,  0.320214,  83.75648
 240, 0.3300266,  87.08388
 256, 0.3603584,  85.08196
 384,  0.547723,  84.02057
```
* comparison to standard library

**!** Anaconda is installed with mkl! Use 
```bash
$ /usr/bin/python test_case.py
###### output
 64, 0.1193422,  63.85001
  80, 0.1430272,  66.70062
  96, 0.1570186,  72.98498
 104, 0.1763408,  70.43181
 112, 0.1822176,  73.42869
 120,   0.24721,  58.00737
 128, 0.2170244,  70.49898
 144, 0.2821276,  61.03621
 160, 0.2588208,  73.95079
 176, 0.2974686,  70.79738
 192, 0.2998518,  76.63786
 200, 0.3279876,  72.99056
 208, 0.3373948,  73.80078
 224, 0.3576888,  74.98138
 240,  0.393047,  73.12103
 256, 0.5408368,  56.68993
 384, 0.6812582,  67.55148
```

