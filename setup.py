from setuptools import setup

def readme():
	with open('README.rst') as f:
		return (f.read())

def requirements():
	with open('requirements.txt') as f:
		return (f.read().split('\n'))

setup(name='deltascope',
	version='0.2.4',
	description='Python package to quantify biological structure',
	long_description=readme(),
	keywords='biology image analysis quantification',
	url='https://github.com/msschwartz21/deltascope',
	author='Morgan Schwartz',
	author_email='msschwartz21@gmail.com',
	license='GNU GPL',
	packages=['deltascope'],
	install_requires=requirements(),
	include_package_data=True
	)
