from setuptools import setup, find_packages

setup(
	name = "dreload",
	version = "0.0.2",
	author = "Aaron I Rabinowitz",
	description = "Reload structured modules in IPython in one command",
	packages = find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
	python_requires = ">=3.6",
	)