from setuptools import setup, find_packages
import sys, os

version = '0.2.0'

setup(name='pybufferbins',
      version=version,
      description="Fast routine to seemlessly classify and store incoming data into an infinite number Protocol Buffer files (\"bins\").",
      long_description="""\
Fast routine to seemlessly classify and store incoming data into an infinite number Protocol Buffer files ("bins"). Bins are grouped into directories by a specific field. Data can then be retrieved by the grouped-field's value. Virtually any data can be stored for fast retrieval by using a Bins instance as an index for each required configuration of data.
""",
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
      keywords='protocol buffers',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/PyBufferBins',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=['protobuf'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

