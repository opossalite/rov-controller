from setuptools import setup

setup(name='rov-client',
      version='0.1',
      description='Client for interacting with the ROV',
      url='http://github.com/TheTerrior/rov-controller',
      author='TheTerrior',
      author_email='werbird10@gmail.com',
      license='GPLv3',
      packages=['rov-client'],
      install_requires=[
          'opencv-python',
      ],
      zip_safe=False)