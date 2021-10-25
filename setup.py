# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in kautenburger_it/__init__.py
from kautenburger_it import __version__ as version

setup(
	name="kautenburger_it",
	version=version,
	description="Anpassungen für Kautenburger IT",
	author="Kautenburger IT",
	author_email="contact@kautenburger-it.de",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
