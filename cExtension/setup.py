from distutils.core import setup, Extension
import numpy as np
module1 = Extension('demo',
                    sources = ['demomodule.c'],
                    include_dirs=[numpy.get_include()]
                    )

setup (name = 'a demo extension module',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1]
       )