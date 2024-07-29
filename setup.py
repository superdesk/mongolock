__version__ = '1.3.4'

import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()


setup(
    name='mongolock',
    version=__version__,
    description='Python Mongodb based Distributed Lock',
    long_description=README,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='lock mongodb',
    author="Lev Orekhov",
    author_email="lev.orekhov@gmail.com",
    url="https://github.com/lorehov/mongolock",
    license="BSD",
    package_dir={'': 'src'},
    py_modules=['mongolock'],
    include_package_data=True,
    zip_safe=False,
    install_requires=["pymongo>=2.6.0"]
)
